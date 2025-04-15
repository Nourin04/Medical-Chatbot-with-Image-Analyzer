import streamlit as st
import requests
import base64
from PIL import Image
from io import BytesIO
import os

from dotenv import load_dotenv
load_dotenv()


# Load GROQ API key from environment variable (recommended)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Or replace with your actual key (not recommended)
if not GROQ_API_KEY:
    st.error("🚨 GROQ_API_KEY not found. Please set it as an environment variable.")
    st.stop()

# Function to encode image to base64
def encode_image(img: Image.Image) -> str:
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# Function to send a request to a specified model
def make_api_request(image_base64: str, question: str, model_name: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model_name,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],
        "temperature": 0.2,
        "max_tokens": 1000
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"❌ Error: {response.status_code} - {response.text}"

# Streamlit UI
st.set_page_config(page_title="AI Doctor - Image Analyzer", layout="wide")
st.title("🧠 AI-Doctor: Medical Chatbot with Image Analyzer")

# File uploader
uploaded_image = st.file_uploader("📤 Upload a medical image", type=["png", "jpg", "jpeg"])

# Text input
question = st.text_area("💬 Ask a question related to the uploaded image:")

# Submit button
if st.button("🚀 Submit"):
    if uploaded_image and question:
        image = Image.open(uploaded_image)
        img_str = encode_image(image)

        with st.spinner("Analyzing with LLaMA 3.2 models... 🧠"):
            llama_response = make_api_request(img_str, question, "meta-llama/llama-4-scout-17b-16e-instruct")
            llava_response = make_api_request(img_str, question, "meta-llama/llama-4-scout-17b-16e-instruct")

        st.subheader("📸 Uploaded Image")
        st.image(image, use_container_width =True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🤖 Response from `meta-llama/llama-4-scout-17b-16e-instruct`")
            st.markdown(llama_response)

        with col2:
            st.markdown("### 🤖 Response from `meta-llama/llama-4-scout-17b-16e-instruct`")
            st.markdown(llava_response)

    else:
        st.warning("⚠️ Please upload an image and enter a question.")


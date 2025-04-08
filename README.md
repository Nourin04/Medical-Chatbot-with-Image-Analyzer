Got it! Let’s upgrade the README with **clean structure**, **rich formatting**, and **developer-friendly sections** — something that's **professional, engaging, and complete**. Here’s a much better version 👇

---

# 🧠 AI Doctor: Medical Chatbot with Image Analyzer

A powerful AI-powered medical assistant built with **Streamlit** and **GROQ’s LLaMA 3.2 Vision Models**, capable of analyzing uploaded medical images (like X-rays, MRIs) and answering questions related to them.

![banner](https://raw.githubusercontent.com/Nourin04/Medical-Chatbot-with-Image-Analyzer/main/assets/banner.png) <!-- Optional if you want a banner -->

---

## 🚀 Features

- 🖼️ Upload medical images (JPG, PNG, JPEG)
- 💬 Ask custom questions about the image
- ⚡ Dual responses from:
  - `llama-3.2-11b-vision-preview`
  - `llama-3.2-90b-vision-preview`
- 🔐 Secure API key via `.env` or GitHub Secrets
- 📦 Easy deployment via Streamlit Cloud or Hugging Face Spaces

---

## 📸 Demo

![demo]![Screenshot (94)](https://github.com/user-attachments/assets/6794e0c1-da47-4640-9533-07a200bd1e6f)
![Screenshot (95)](https://github.com/user-attachments/assets/ce4301d5-7335-4114-94ef-c5f15b8729dc)


Deployed link: https://medical-chatbot-new.streamlit.app/
---

## 🏗️ Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| **Streamlit** | Web app interface                |
| **GROQ API** | Access to LLaMA vision models     |
| **Pillow**   | Image handling & preprocessing   |
| **dotenv**   | Secure environment configuration |

---

## 🔧 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Nourin04/Medical-Chatbot-with-Image-Analyzer.git
cd Medical-Chatbot-with-Image-Analyzer
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure the API Key

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

> ⚠️ Never push `.env` to GitHub. Add it to `.gitignore`.

---

## 🔐 GitHub Deployment Secret

If you're deploying to **GitHub Actions** or **Streamlit Cloud**, store your key securely:

- GitHub → Repository → ⚙️ Settings → Secrets → **New repository secret**
- Name: `GROQ_API_KEY`  
- Value: `your_actual_groq_api_key_here`

---

## 💻 Run the App

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
📦Medical-Chatbot-with-Image-Analyzer
 ┣ 📄app.py
 ┣ 📄.env              # Not pushed to GitHub
 ┣ 📄requirements.txt
 ┗ 📄README.md
  
```


---

## 🧪 Example Questions

- What condition is visible in this X-ray?
- Does the MRI show any abnormal growth?
- Can you analyze for signs of pneumonia?

---

## ✨ Author

**Noureen**  
🌐 GitHub: [@Nourin04](https://github.com/Nourin04)  
📬 DM for collaborations, improvements or feedback!

---




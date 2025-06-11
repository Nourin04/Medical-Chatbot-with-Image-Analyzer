

# 🧠 AI Doctor: Medical Chatbot with Image Analyzer

A powerful AI-powered medical assistant built with **Streamlit** and **GROQ’s LLaMA 4 Vision Model**, capable of analyzing uploaded medical images and answering questions related to them.



---

## 🚀 Features

- 🖼️ Upload medical images (JPG, PNG, JPEG)
- 💬 Ask custom questions about the image
- ⚡ Responses from:
  - `meta-llama/llama-4-scout-17b-16e-instruct`
- 📦 Deployment via Streamlit Cloud 

---

## 📸 Demo

![image](https://github.com/user-attachments/assets/c454b981-249b-43f2-b350-63acfa1d7342)

![image](https://github.com/user-attachments/assets/e748f4c1-3d39-46ba-b441-2bf9c235c84e)

![image](https://github.com/user-attachments/assets/683c3450-4cdd-4dd3-b943-bf83c7f3537f)

## Demo 2


![image](https://github.com/user-attachments/assets/3081a17e-ce99-4022-bb6f-8204abc59154)

![image](https://github.com/user-attachments/assets/f30ba237-2489-4ea4-8483-dd112eaa96ab)
![image](https://github.com/user-attachments/assets/1ea2639d-32be-4b20-98c8-c79f47602d38)





Deployed link: https://medical-chatbot-new.streamlit.app/
---

## 🏗️ Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| **Streamlit** | Web app interface                |
| **GROQ API** | Access to LLaMA vision models     |
| **Pillow**   | Image handling & preprocessing   |


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

**Noureen AC**  
🌐 GitHub: [@Nourin04](https://github.com/Nourin04)  
📬 DM for collaborations, improvements or feedback!

---




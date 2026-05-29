# 🧭 AI Tourism Assistant

An intelligent AI-powered tourism assistant built using **Python, Flask, and Google Gemini API**.
The system helps tourists interact with Egyptian landmarks through a smart chatbot and generates personalized travel plans based on user interests.

---

# 🚀 Features

## 🤖 AI Tourist Chatbot

* Answers tourist questions using Google Gemini AI.
* Provides information about famous Egyptian landmarks.
* Uses a lightweight Retrieval-Augmented Generation (RAG) approach with a custom knowledge base.
* Supports Arabic interaction.

---

## 🗺️ Smart Tour Plan Generator

Generate personalized tourism plans based on:

* Destination
* Number of days
* User interests

The system creates:

* Daily schedules
* Suggested attractions
* Customized recommendations

---

# 🧠 Technologies Used

* Python
* Flask
* Google Gemini API
* HTML/CSS
* Jinja2 Templates

---

# 📂 Project Structure

```bash
project/
│
├── app.py                # Flask Application
├── base_code.py          # Core AI Logic
├── templates/
│   └── index.html        # Frontend UI
├── static/               # CSS / JS / Assets
└── README.md
```

---

# ⚙️ How It Works

## 1️⃣ Knowledge Retrieval

The chatbot first searches a local knowledge base for known tourist landmarks.

Example:

* أبو الهول
* قلعة قايتباي

If information exists:

* The retrieved context is injected into the prompt.
* Gemini generates a contextual AI response.

This creates a simple RAG-like architecture.

---

## 2️⃣ AI Response Generation

The system uses:

```python
gemini-2.5-flash
```

through the Google Generative AI SDK.

Main function:

```python
call_gemini_api()
```

Responsible for:

* Sending prompts
* Controlling temperature
* Handling API errors

---

## 3️⃣ Personalized Tour Planning

The function:

```python
generate_tour_plan_and_suggestions()
```

creates customized tourism plans based on:

* Location
* Duration
* Interests

Example Interests:

* Historical Places
* Food
* Museums
* Beaches
* Photography

---

# 🛠️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/ai-tourism-assistant.git
cd ai-tourism-assistant
```

---

## Install Dependencies

```bash
pip install flask google-genai
```

---

## Set Environment Variable

### Windows

```bash
set GOOGLE_API_KEY=your_api_key
```

### Linux / Mac

```bash
export GOOGLE_API_KEY=your_api_key
```

---

# ▶️ Run the Project

```bash
python app.py
```

Then open:

```bash
http://127.0.0.1:5000
```

---

# 📸 Example Use Cases

## Chatbot Questions

* ما معلومات عن أبو الهول؟
* أين تقع قلعة قايتباي؟
* ما أفضل أماكن سياحية في مصر؟

---

## Travel Planning

Input:

* Location: Cairo
* Duration: 3 Days
* Interests: History & Museums

Output:

* Complete AI-generated travel itinerary

---

# 🧩 Future Improvements

* Database Integration
* Real-time Maps API
* Voice Assistant Support
* Multilingual Support
* Hotel & Flight Recommendations
* User Authentication
* Vector Database for Advanced RAG
* AI Memory System

---

# 📈 AI Concepts Used

* Prompt Engineering
* Retrieval-Augmented Generation (RAG)
* Context Injection
* Generative AI
* Conversational AI

---

# 🧑‍💻 Author

Mostafa Nabil
AI & Software Engineering Enthusiast

---

# ⭐ Project Goal

This project was built to explore how Generative AI can improve tourism experiences through intelligent interaction and personalized recommendations.

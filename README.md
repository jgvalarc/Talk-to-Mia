## 📌 Project Overview
This project implements an **AI-powered chatbot** using **Machine Learning (ML)** and **Natural Language Processing (NLP)** to classify user intents and generate dynamic responses. The chatbot is designed to interact with users in **Portuguese** and can learn different intents through a trained **Support Vector Machine (SVM) model**.

## 🚀 Features
- **Intent Classification** using a trained **SVM model** (`LinearSVC`).
- **Natural Language Processing (NLP)** with **spaCy** (`pt_core_news_sm`).
- **Vectorization of Text Data** using **CountVectorizer**.
- **Dynamic Response Generation** with placeholders for personalized replies.
- **Randomized responses** for more natural interactions.
- **Interactive CLI-based chatbot** with real-time conversations.
- **Easily expandable knowledge base**.

## ⚙️ Technologies Used
- **Python** 🐍
- **spaCy** (for NLP processing)
- **scikit-learn** (for ML classification)
- **CountVectorizer** (for text feature extraction)
- **LinearSVC** (for intent classification)
- **Django** (Developing Framework and Local Server Hosting)

## 🔧 Setup & Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/jgvalarc/Talk-to-Mia.git
cd Talk-to-Mia
```

### 2️⃣ Create and Activate a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv

venv/scripts/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Chatbot
```bash
python manage.py runserver
```

## 📖 How It Works
1. The chatbot loads a **pretrained spaCy model** (`pt_core_news_sm`) for NLP processing.
2. The **intent classifier** is trained using **SVM (Support Vector Machine)** with **CountVectorizer**.
3. When a user inputs a message, the chatbot:
   - **Vectorizes the input** to match a trained intent.
   - **Predicts the intent** using the **SVM model**.
   - **Generates a response** from the **knowledge base**.
4. Responses are dynamically modified using predefined **placeholders**.

## 📌 Example Conversation
```
Oi, meu nome é Mia, como posso lhe ajudar?
> Qual é o seu nome?
Mia: Meu nome é Mia! Como posso te ajudar hoje?

> Como está o tempo hoje?
Mia: Eu ainda não sei consultar a previsão do tempo. Mas posso ajudar com outras dúvidas!
```

## 🔮 Future Improvements
✅ Implement **TF-IDF or Word2Vec** for better intent classification.
✅ Use a **Deep Learning model (e.g., LSTMs, BERT)** for better NLP performance.
✅ Expand integration with **APIs** (e.g., OpenWeather, Wikipedia, GPT models).
✅ Deploy chatbot via **Telegram, Discord, or WhatsApp**.

## 🤝 Contributing
Feel free to fork this repository, make improvements, and submit a pull request! Any contributions to improve this chatbot are welcome. 😊

## 📜 License
This project is licensed under the **MIT License**.

---
Made with ❤️ by jgvalarc(https://github.com/jgvalarc) 🚀

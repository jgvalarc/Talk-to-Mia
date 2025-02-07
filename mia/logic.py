import spacy
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from .knowledge_base import knowledge_base, placeholders
from .train_data import train_data

nlp = spacy.load("pt_core_news_sm")

# Extrair palavras dos dados de treino
X_train = [text for text, _ in train_data]
y_train = [intent for _, intent in train_data]

# Vectorizando dados com CountVectorizer
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)

# Treinador, ajuda a definir intenção
clf = LinearSVC()
clf.fit(X_train, y_train)

# Método para definir intenção (assunto)
def classify_intent(text):
    features = vectorizer.transform([text])
    intent = clf.predict(features)[0]
    return intent


# Função para gerar respostas com respostas dinamicas
def generate_response(intent):
    if intent in knowledge_base:
        responses = knowledge_base[intent]
        response = random.choice(responses)
        # Placeholders que substituem determinadas palavras nas respostas
        # Substitui placeholders por variações para uma conversa mais dinamica
        for placeholder, value in placeholders.items():
            if value:
                response = response.replace(placeholder, value)
        return response
    else:
        return random.choice(["Eu não entendi o que você disse :/", "Pode frasear de novo sua pergunta?","Fala direito porra"])
    
# Função que lida com a conversa
def chatbot():
    print("Oi, meu nome é Mia, como posso lhe ajudar?")
    while True:
        user_input = input("")
        intent = classify_intent(user_input)
        response = generate_response(intent)
        print(response)
                  
if __name__ == "__main__":
    chatbot()

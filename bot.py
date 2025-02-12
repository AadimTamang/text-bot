import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk import pos_tag

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')

def respond(text):
    pos_tags, stemmed_words = clean_text(text)
    responses = []

    greet_response = greet(stemmed_words)
    if greet_response:
        responses.append(greet_response)

    for stemmed_word, pos in pos_tags:
        if pos.startswith('NN'):
            responses.append(f"I don't know about '{stemmed_word}', can you help me understand it?")
        elif pos.startswith('VB'):
            responses.append(f"I would like to know about {stemmed_word}")

    if responses:
        return responses[0]
    return "I'm not sure how to respond to that."  # Default response if no conditions are met


def clean_text(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    pos_tags = pos_tag(filtered_words)
    return pos_tags, stemmed_words

def greet(greet):
    if 'hello' in greet:
        return "Hello!"
    elif 'goodmorning' in greet:
        return "Good morning!"
    elif 'goodevening' in greet:
        return "Good evening!"
    elif 'goodafternoon' in greet:
        return "Good afternoon!"
    elif 'goodby' in greet or 'bye' in greet:
        return "Goodbye!"
        
    return None

def start_bot():
    print("Bot is starting...")
    while True:
        text = input("What can I help with? ")
        if text.lower() in ['exit', 'quit', 'bye']:
            print("Good bye!")
            break
        responses = respond(text)
        if responses:
            print(responses)

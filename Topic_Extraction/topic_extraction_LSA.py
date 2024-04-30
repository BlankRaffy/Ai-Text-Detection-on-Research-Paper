import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import xml.etree.ElementTree as ET
import get_text



# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

path=r'C:\Users\Blank\Desktop\Ai-Text-Detection-on-Research-Paper\Topic_Extraction\PMC29044_plagiated.xml'
tree = ET.parse(path)

sentence = get_text.extract_intro(tree)
# Text preprocessing function
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenization and lowercasing
    tokens = [token for token in tokens if token.isalpha()]  # Keep alphabetic words
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]  # Lemmatization and remove stopwords
    return ' '.join(tokens)

# Preprocess the sentence
preprocessed_sentence = preprocess_text(sentence)

# Create TF-IDF matrix for the sentence
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([preprocessed_sentence])

# Apply Latent Semantic Analysis (LSA)
num_topics = 2  # Number of topics/components

lsa_model = TruncatedSVD(n_components=num_topics)
lsa_topic_matrix = lsa_model.fit_transform(tfidf_matrix)

# Display the top terms associated with the extracted topic
terms = tfidf_vectorizer.get_feature_names_out()
top_terms_idx = lsa_model.components_[0].argsort()[-5:]  # Get indices of top 5 terms
top_terms = [terms[idx] for idx in top_terms_idx]

print("Top terms associated with the topic:")
print(', '.join(top_terms))

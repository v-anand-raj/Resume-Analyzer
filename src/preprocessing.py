import re
import spacy


nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|\S+\.\S+", "", text)

    # Remove phone numbers
    text = re.sub(r"\+?\d[\d\s-]{8,}\d", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Process text using spaCy
    doc = nlp(text)

    cleaned_tokens = []

    for token in doc:
        if (
            token.is_alpha
            and not token.is_stop
            and not token.is_punct
        ):
            cleaned_tokens.append(token.lemma_)

    return cleaned_tokens
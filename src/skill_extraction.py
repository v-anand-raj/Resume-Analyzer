import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

def load_skills(skills_path):
    skills_df = pd.read_csv(skills_path)
    skills = set(skills_df["skill"].str.lower())
    return skills

def extract_skills(text, skills):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in skills]
    matcher.add("SKILLS", patterns)
    doc = nlp(text)
    matches = matcher(doc)
    extracted_skills = set()
    for match_id, start, end in matches:
        skill = doc[start:end].text.lower()
        extracted_skills.add(skill)
    return sorted(extracted_skills)
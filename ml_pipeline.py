# Example: Simple ML Pipeline using HuggingFace and PyTorch
import torch
from transformers import pipeline

def load_nlp_model():
    # Load a sentiment-analysis pipeline from HuggingFace
    nlp = pipeline('sentiment-analysis')
    return nlp

def process_data(data):
    nlp = load_nlp_model()
    return nlp(data)

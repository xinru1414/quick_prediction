from transformers import pipeline


def predict(seq):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli") 
    candidate_labels = ['travel', 'cooking', 'dancing']
    ans = classifier(seq, candidate_labels)
    return ans['labels'][ans['scores'].index(max(ans['scores']))]
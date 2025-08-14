from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def get_best_review(reviews):
    results = sentiment_model(reviews)

    best = None
    best_score = 0
    for review, result in zip(reviews, results):
        if result['label'] == 'POSITIVE' and result['score'] > best_score:
            best = review
            best_score = result['score']
    return best

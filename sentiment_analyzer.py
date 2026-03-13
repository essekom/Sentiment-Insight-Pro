from textblob import TextBlob
import pandas as pd

class SentimentAnalyzer:
    def __init__(self):
        self.results = []

    def analyze_text(self, text):
        """Analyze the sentiment of a given text."""
        analysis = TextBlob(text)
        sentiment = analysis.sentiment.polarity
        
        if sentiment > 0:
            category = 'Positive'
        elif sentiment == 0:
            category = 'Neutral'
        else:
            category = 'Negative'
            
        return {
            'text': text,
            'score': sentiment,
            'category': category
        }

    def process_batch(self, texts):
        """Process a list of texts and return a DataFrame."""
        self.results = [self.analyze_text(t) for t in texts]
        return pd.DataFrame(self.results)

if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    sample_data = [
        "I love this new AI tool!",
        "The weather is okay today.",
        "I'm very frustrated with the slow performance."
    ]
    df = analyzer.process_batch(sample_data)
    print("Sentiment Analysis Results:")
    print(df)

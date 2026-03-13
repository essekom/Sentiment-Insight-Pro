# Sentiment-Insight-Pro ðŸ“ŠðŸ§ 

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![NLTK](https://img.shields.io/badge/NLP-TextBlob-green.svg)](https://textblob.readthedocs.io/)
[![Pandas](https://img.shields.io/badge/Data-Pandas-red.svg)](https://pandas.pydata.org/)

An AI-powered sentiment analysis engine designed to extract emotional insights from text data. This tool is ideal for monitoring social media feedback, customer reviews, and market trends.

## ðŸš€ Features
- **Real-time Analysis:** Instant sentiment scoring for individual text inputs.
- **Batch Processing:** Efficiently analyze large datasets from CSV or lists.
- **Categorization:** Automatically labels text as *Positive*, *Neutral*, or *Negative*.
- **Data Visualization Ready:** Outputs structured data compatible with Seaborn and Matplotlib.

## ðŸ› ï¸ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/peter160789/Sentiment-Insight-Pro.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ðŸ’» Usage
```python
from sentiment_analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()
result = analyzer.analyze_text("The new update is absolutely fantastic!")
print(f"Sentiment: {result['category']} (Score: {result['score']})")
```

## ðŸ“‹ Requirements
- TextBlob
- Pandas

---
Developed by [Peter](https://github.com/peter160789)

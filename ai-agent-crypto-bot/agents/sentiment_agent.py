# agents/sentiment_agent.py

class SentimentAgent:
    def __init__(self):
        self.name = "Sentiment Agent"

    def analyze_sentiment(self, news_data):
        # 这里只是一个简单的示例，实际的情感分析逻辑会更复杂
        positive_words = ["good", "great", "positive"]
        negative_words = ["bad", "terrible", "negative"]

        sentiment_score = 0
        for news in news_data:
            for word in news.split():
                if word in positive_words:
                    sentiment_score += 1
                elif word in negative_words:
                    sentiment_score -= 1

        return sentiment_score

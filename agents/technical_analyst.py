# agents/technical_analyst.py

class TechnicalAnalyst:
    def __init__(self):
        self.name = "Technical Analyst"

    def perform_analysis(self, price_data):
        # 这里只是一个简单的示例，实际的技术分析逻辑会更复杂
        moving_average = sum(price_data) / len(price_data) if price_data else None
        return {"moving_average": moving_average}

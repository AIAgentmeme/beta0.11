# tests/test_agents.py

import unittest
from agents import ValuationAgent, SentimentAgent, FundamentalsAgent, TechnicalAnalyst, RiskManager, PortfolioManager

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.valuation_agent = ValuationAgent()
        self.sentiment_agent = SentimentAgent()
        self.fundamentals_agent = FundamentalsAgent()
        self.technical_analyst = TechnicalAnalyst()
        self.risk_manager = RiskManager()
        self.portfolio_manager = PortfolioManager()

    def test_valuation_agent(self):
        data = [10, 20, 30, 40, 50]
        self.assertEqual(self.valuation_agent.evaluate_value(data), 30)

    def test_sentiment_agent(self):
        news_data = ["This is good news", "This is bad news", "This is great news"]
        self.assertEqual(self.sentiment_agent.analyze_sentiment(news_data), 1)

    def test_fundamentals_agent(self):
        crypto_data = {
            "market_cap": [1000, 2000, 3000],
            "volume": [100, 200, 300],
        }
        self.assertEqual(self.fundamentals_agent.research_fundamentals(crypto_data), {"market_cap": 6000, "volume": 600})

    def test_technical_analyst(self):
        price_data = [10, 20, 30, 40, 50]
        self.assertEqual(self.technical_analyst.perform_analysis(price_data), {"moving_average": 30})

    def test_risk_manager(self):
        portfolio = [{"value": 1000}, {"value": 2000}]
        risk_tolerance = 0.1
        self.assertEqual(self.risk_manager.manage_risk(portfolio, risk_tolerance), {"risk_score": 300})

    def test_portfolio_manager(self):
        assets = [{"value": 1000}, {"value": 2000}]
        self.assertEqual(self.portfolio_manager.manage_portfolio(assets), {"total_value": 3000})

if __name__ == '__main__':
    unittest.main()

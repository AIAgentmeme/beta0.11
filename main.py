# main.py

from trading_manager import TradingManager

def main():
    trading_manager = TradingManager()

    # 模拟数据
    data = {
        "price_data": [10, 20, 30, 40, 50],
        "news_data": ["This is good news", "This is bad news", "This is great news"],
        "crypto_data": {
            "market_cap": [1000, 2000, 3000],
            "volume": [100, 200, 300],
        },
        "portfolio": [{"value": 1000}, {"value": 2000}],
        "risk_tolerance": 0.1,
    }

    # 执行交易
    decision = trading_manager.execute_trade(data)
    print(f"Trading decision: {decision}")

if __name__ == "__main__":
    main()

from Metrics.SharpeRatio import SharpeRatioMetric
from Strategies.PairsTrading import PairsTradingStrategy

if __name__ == "__main__":
	sharpe_ratio = SharpeRatioMetric()
	print(sharpe_ratio.name)

	pairs_trading = PairsTradingStrategy('AAPL', 'NVID')
	print(pairs_trading.name)
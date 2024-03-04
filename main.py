from Metrics.SharpeRatio import SharpeRatioMetric
from Strategies.PairsTrading import PairsTradingStrategy
from Ledger.Ledger import Ledger



if __name__ == "__main__":
	sharpe_ratio = SharpeRatioMetric()
	print(sharpe_ratio.name)

	pairs_trading = PairsTradingStrategy([('AAPL', 'NVID')])
	print(pairs_trading.name)
	


	ledger = Ledger([1,2,3], ['APPL'], 10)
	print(ledger.to_pandas().head())
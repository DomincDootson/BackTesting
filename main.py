from Metrics.SharpeRatio import SharpeRatioMetric
from Strategies.PairsTrading import PairsTradingStrategy
from Ledger.Ledger import Ledger
from BackTesting.BackTesting import BackTesting

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def test_pairs_trading():
	pairs_trading = PairsTradingStrategy('Data/trading_pairs_info_2023_Q34.csv')
	bt = BackTesting('Data/SP500_Close_Data_2023_Q34.csv')
	bt.back_test(pairs_trading)
	bt.ledger.print_metrics()


if __name__ == "__main__":
	test_pairs_trading()

	
	
	# ledger = Ledger([1,2,3], ['APPL'], 10)
	# print(pairs_trading.trade_strategy("s", ledger))

	

import pandas as pd
from Ledger.Ledger import Ledger
from Strategies.Strategy import Strategy

class BackTesting():
	"""This class runs the back testing for a given data set and strategy"""
	def __init__(self, market_data_filename : str) -> None:
		
		self.market_data = pd.read_csv(market_data_filename, index_col = 'Date')
		self.market_data.index = pd.to_datetime(self.market_data.index)
		self.ledger = None
	

	def back_test(self, strategy : Strategy) -> None: 
		"""
		Given a strategy, this will create a ledger of all the posititions taken while trading
		"""
		self.ledger = strategy.trade_strategy(self.market_data)
	


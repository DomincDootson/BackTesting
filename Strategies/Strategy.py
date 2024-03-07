from abc import ABC, abstractmethod
from Strategies.StrategyName import StrategyName

import pandas as pd

class Strategy():
	"""This ABC will implmenent a strading strategy"""
	def __init__(self, strategy_name : StrategyName):
		self.name : StrategyName = strategy_name

	@abstractmethod
	def trade_strategy(self, data : pd.DataFrame) -> pd.DataFrame:
		"""
		Generate trading signals based on the specific implimentation of a strategy. Will return 
		a data frame containing what to do at each time step 

		Parameters:
		- data: DataFrame containing historical data for both stocks.

		Returns:
		- DataFrame with trading signals (1 for long, -1 for short, 0 for hold).
		"""
		pass

	def check_stocks_in_data(self, data_stocks : list[str], strategy_stocks : list[str]) -> bool:
		'''
		Returns true if all the stocks that we for our strategy is in the data
		'''
		if all((s in data_stocks for s in strategy_stocks)):
			return True
		raise KeyError(f"The pairs trading stocks are not in the data") 

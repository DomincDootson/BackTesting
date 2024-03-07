from Ledger.Position import Position
from collections import defaultdict

import pandas as pd 
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

class Ledger():
	"""
	The ledger class will record our current positions. Each Strategy will contain a variety of stocks 
	that we are following, each one will have an ID. The ledger has a dict with the IDs as keys and a list
	of the positions that we have take in that stratgy.  
	"""
	def __init__(self, starting_cash : float = 0):
		self.ledger : dict[str, list[Position]] = defaultdict(list)

	def __repr__(self):
		"""Allows us to print a log of the trades"""
		return '\n'.join([str(p) for p in self.sorted_positions()])
			
	def is_position_open(self, key) -> bool:
		"""Checks to see if a position is open"""
		if len(self.ledger[key]) == 0:
			return False
		return self.ledger[key][-1].is_open()

	def close_position(self, key : str, end_date : date, stock_prices : list) -> None:
		"""Closes a position"""
		if key not in self.ledger:
			raise KeyError("The key is not in the ledeger.")
		self.ledger[key][-1].close_position(end_date, stock_prices)

	def create_new_position(self, key: str, start_date : date, amount : float, stocks : list[int]) -> None:
		"""Adds a new open position to the ledger"""
		self.ledger[key].append(Position(key, start_date, amount, stocks))

	def sorted_positions(self) -> list[Position]:
		"""Sorts the trades we make by their start date"""
		return sorted([p for positions in self.ledger.values() for p in positions] , key = lambda x : x.start_date)
	
	def get_all_returns(self) -> list[float]:
		"""Gets the returns from all the trades"""
		return [position.returns for position in self.sorted_positions() if position is not None]


	## Some Metrics ##
	## ------------ ##

	def get_volatility(self) -> float:
		return np.std(self.get_all_returns())

	def get_average_returns(self) -> float:
		return np.mean(self.get_all_returns())

	def get_annualised_returns(self) -> float:
		return 252*self.get_average_returns()

	def sharpe_ratio(self, risk_free_rate = 3.5):
		return np.sqrt(252) * (self.get_average_returns() - risk_free_rate/252)/self.get_volatility()

	def print_metrics(self):
		print(f"Annual Average Returns: {np.round(self.get_annualised_returns(),2)}%")
		print(f"Annual Volatility: {np.round(np.sqrt(252)*self.get_volatility(),2)}%")
		print(f"Sharpe Ratio: {np.round(self.sharpe_ratio(),2)}")
from Ledger.Position import Position
from collections import defaultdict

import pandas as pd 
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
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

	def print_moments(self):
		print(f"Daily Returns: {np.round(self.get_average_returns(), 3)}")
		print(f"Volatility: {np.round(self.get_volatility(), 3)}")
		print(f"Skew: {np.round(skew(self.get_all_returns()), 3)}")
		print(f"kurtosis: {np.round(kurtosis(self.get_all_returns()), 3)}")

	def get_annualised_returns(self) -> float:
		return 252*self.get_average_returns()

	def sharpe_ratio(self, risk_free_rate = 3.5):
		return np.sqrt(252) * (self.get_average_returns() - risk_free_rate/252)/self.get_volatility()

	def print_metrics(self):
		print(f"Annual Average Returns: {np.round(self.get_annualised_returns(),2)}%")
		print(f"Annual Volatility: {np.round(np.sqrt(252)*self.get_volatility(),2)}%")
		print(f"Sharpe Ratio: {np.round(self.sharpe_ratio(),2)}")


	def show_returns_hist(self):
		plt.hist(self.get_all_returns(), bins = 250, label = f"Mean: {np.round(self.get_average_returns(), 3)}\nVolatility: {np.round(self.get_volatility(), 3)}",
		 color = 'royalblue', alpha = 0)
		plt.hist(self.get_all_returns(), bins = 250, 
		 color = 'royalblue')
		plt.xlim([-.2, .4])
		plt.legend()
		plt.xlabel("Daily Returns")
		plt.title("Daily Returns for Pairs Trading Strategy")
		plt.show()

	def show_n_days_dist(self):
		fig, axs = plt.subplots(ncols = 2)
		returns, n_days = [p.returns for p in self.sorted_positions()], [len(p) for p in self.sorted_positions()]

		axs[0].hist([n for n,r in zip(n_days, returns) if r >0], bins = 25, color = 'royalblue', label = "Positive Returns")
		axs[0].hist([n for n,r in zip(n_days, returns) if r <0], bins = 25, color = 'firebrick', alpha = 0.8, label = "Negative Returns")

		axs[0].set_xlabel("Number of Days Position open")
		axs[0].set_title("Number of Days in Position")


		axs[1].hist([p.end_date for p in self.sorted_positions() if p.returns > 0], color = 'royalblue', bins = 100, label = "Positive Returns")
		axs[1].hist([p.end_date for p in self.sorted_positions() if p.returns < 0], color = 'firebrick', bins = 100, label = "Negative Returns")
		axs[1].legend()
		axs[1].set_xlabel("Position End Date")
		axs[1].set_title("P/L by Position End Date")
		axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation = 45)
		plt.show()

	def get_returns_excluding_final_day(self):
		max_day = max([p.end_date for p in self.sorted_positions()])
		returns = [p.returns for p in self.sorted_positions() if p.end_date != max_day]
		print(np.mean(returns))


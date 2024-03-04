import pandas as pd 
from datetime import date

class Ledger():
	"""
	The ledger class will record our current positions and the cash we have liquid. Instead
	of using a data frame and editing the values as we go (which is v. slow), we will use a 
	dict with the keys of our stocks. 
	"""
	def __init__(self, dates : list[date], equities : list[str], starting_cash : float):
		
		self.dates  : list[date] = dates
		self.ledger : dict[str, list[float]] = {eq : [0 for _ in self.dates] for eq in equities}

		self.cash : list[float] = [0 for _ in self.dates] # Keep the cash seperate
		self.cash[0] = starting_cash
		

	def __getitem__(self, key : tuple[str, int]) -> float:
		'''
		This method gets items from the ledge. Note that __getitem__ can only take one argument,
		so to get the value we want, we must pass it a tuple that contains (stock_id, time_index)
		'''
		key, index = key
		return self.ledger[key][index]

	def __setitem__(self, key : tuple[str, int], value : float) -> None:
		'''
		Same as the getter, but sets
		'''
		key, index = key
		self.ledger[key][index] = value


	def to_pandas(self) -> pd.DataFrame:
		return pd.DataFrame(data = {**self.ledger,
									'Cash' : self.cash}, index = self.dates)
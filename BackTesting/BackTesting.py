import pandas as pd

class BackTesting():
	"""This class runs the back testing for a given data set and strategy"""
	def __init__(self, market_data_filename : str) -> None:
		
		self.market_data = pd.read_csv(market_data_filename)
		self.transaction_history = None
	

	def back_test(self, strategy : list[Strategy]) -> None: 
		'''
		Given a list of strategies, it will calculate the buy an cell signals for each strategy in
		the portfolio
		'''
		pass

		# Update the transaction history 

	def calculate_metric(self, metric : Metric) -> float:
		'''Given a metric, it will return the score as calculated on the transaction history'''
		return metric.calculate_score(self.transaction_history)
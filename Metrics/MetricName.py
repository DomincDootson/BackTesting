from enum import Enum 


class MetricName(Enum):
	"""This enum will represent the names of the different metics that we want to calculate"""
	SHARPE_RATIO = 1
	AVERAGE_RETURN = 2
	MAX_DRAWDOWN = 3
	EXPECTANCY = 4
	# One to measure the number of profitable trades

	
	

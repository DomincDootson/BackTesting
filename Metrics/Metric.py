from abc import ABC, abstractmethod

from Metrics.MetricName import MetricName

class Metric(ABC):
	"""Abstract base class used to calculate different metrics"""
	def __init__(self, metric_name : MetricName) -> None:
		self.name : MetricName = metric_name # Get the name with metric_instance.name
	
	@abstractmethod
	def calculate_score(self) -> float:
		pass
		
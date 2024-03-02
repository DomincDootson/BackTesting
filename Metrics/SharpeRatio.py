from Metrics.Metric import Metric
from Metrics.MetricName import MetricName

class SharpeRatioMetric(Metric):
	"""docstring for SharpeRatioMetric"""
	def __init__(self):
		super(SharpeRatioMetric, self).__init__(MetricName.SHARPE_RATIO)

	def calculate_score(self) -> float:
		return 1
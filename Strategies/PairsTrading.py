from Strategies.Strategy import Strategy
from Strategies.StrategyName import StrategyName

import pandas as pd 

class PairsTradingStrategy(Strategy):
    def __init__(self, stock1 : str, stock2 : str, 
        entry_threshold : float =1.5, exit_threshold : float =0.5):
        super(PairsTradingStrategy, self).__init__(StrategyName.PAIRS_TRADING)

        self.stock1 : str = stock1
        self.stock2 : str = stock2
        self.entry_threshold : float = entry_threshold
        self.exit_threshold : float = exit_threshold

    def generate_signals(self, data : pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on the pairs trading strategy.

        Parameters:
        - data: DataFrame containing historical data for both stocks.

        Returns:
        - DataFrame with trading signals (1 for long, -1 for short, 0 for hold).
        """
        signals = pd.DataFrame(index=data.index)
        signals[self.stock1] = 0.0
        signals[self.stock2] = 0.0

        # Implement the strategy logic here

        return signals

    def check_stocks_in_data(self, data_stocks : list[str]) -> bool:
        if self.stock1 in data_stocks and self.stock2 in data_stocks:
            raise keyError(f"The pairs trading stocks ({self.stock1}, {self.stock2}) \
                are not in the data") 

        return True

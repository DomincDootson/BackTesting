from dataclasses import dataclass
from datetime import date, datetime

import numpy as np
@dataclass

class PositionOpen(Exception):
    """Custom error for indicating that a position is already open."""
    pass

@dataclass
class Position():
    ID : str 
    start_date : datetime # 
    amount : float # The amount that we want to put into the position
    stocks : list[int] 
    
    end_date : datetime | None = None # End date, will be set once the position is closed
    returns : float | None = None
    

    def __len__(self):
        if self.end_date is None:
            raise PositionOpen("Position must be closed to calculate len")       
        
        return np.busday_count(self.start_date.date(), self.end_date.date())
    
    def is_open(self) -> bool:
        """Returns true if the position is yet to be closed """
        return self.end_date is None

    def close_position(self, end_date : datetime, stock_prices : list) -> None:
        """Adds the closing position information"""
        self.end_date = end_date
        self.returns = self.calculate_returns(stock_prices)

    def calculate_returns(self, stock_prices : list) -> float:
        """Returns the returns of the strategy"""
        if self.end_date is None:
            raise PositionOpen("Position must be closed to calculate returns") 
              
        return (1/(self.amount * len(self))) * (sum((stock_prices[i][self.end_date]*self.stocks[i] for i in range(len(stock_prices)))) - 0*sum((stock_prices[i][self.start_date]*self.stocks[i] for i in range(len(stock_prices)))))
	
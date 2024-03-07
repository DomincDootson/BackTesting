from Strategies.Pair import Pair
from Strategies.Strategy import Strategy
from Strategies.StrategyName import StrategyName
from Ledger.Ledger import Ledger

from dataclasses import dataclass
import pandas as pd 
import csv

def number_of_stocks_2_buy(X, Y, position_size = 500):
    """
    This function returns the number of stocks to buy, given a initial position size
    """
    return (2*position_size)//X, (2*position_size)//Y

class PairsTradingStrategy(Strategy):
    def __init__(self, pairs_file : str, entry_threshold : float = 2.0, exit_threshold : float = 1.0):
        super(PairsTradingStrategy, self).__init__(StrategyName.PAIRS_TRADING)

        self.pairs : list[Pairs] = []
        with open(pairs_file, 'r', newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                self.pairs.append(Pair(line[0], line[1], float(line[2]), float(line[3])))

        self.alpha_E : float = entry_threshold
        self.alpha_L : float = exit_threshold
        self.position_size = 500

    def trade_strategy(self, stock_prices : pd.DataFrame) -> Ledger:
        """
        Given the stock_prices, this function creates all the positions that we would wish to take.

        Parameters:
        - data: DataFrame containing historical data for both stocks.

        Returns:
        - Ledger: A ledger object. 
        """
        self.check_stocks_in_data(stock_prices.columns, self.flatten_pairs())
        ledger = Ledger()
       
        for time in stock_prices.index:
            for pair in self.pairs:
                X, Y = stock_prices[pair.stock_X].loc[time], stock_prices[pair.stock_Y].loc[time]
                if (time < stock_prices.index[-10]) and pair.should_open_position(self.alpha_E, X, Y) and not ledger.is_position_open(pair.id()):
                    nX, nY = number_of_stocks_2_buy(X, Y, position_size = self.position_size)
                    nX, nY = (nX, -nY) if (Y - X * pair.beta) > 0 else (-nX, nY)
                    ledger.create_new_position(pair.id(), time, 500, [nX, nY])
                

                elif (pair.should_close_position(self.alpha_L, X, Y) or time == stock_prices.index[-1]) and ledger.is_position_open(pair.id()):
                    ledger.close_position(pair.id(), time, [stock_prices[pair.stock_X], stock_prices[pair.stock_Y]])
 
        return ledger


    ## Helper Functions ##
    ## ---------------- ##

    def flatten_pairs(self):
        '''
        Takes the list of pairs are removes all the inner brackets, e.g. [[1,2], [3,4]] ->[1,2,3,4]
        '''
        return [p.stock_X for p in self.pairs] + [p.stock_Y for p in self.pairs]


    

        

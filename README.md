# BackTesting 
The aim of this code is to implement different trading strategies and to backtest them to evaluate their results.  

## Backtesting Overview

### BackTesting 
This class pulls together a strategy and the stock data that is needed to evaluate it. Its key method runs the back testing and returns a ledger object. 

### Ledger 
The classes in this file allow us to track current open positions and past closed positions. There are two main classes:

- `Position`: This contains information about the position that we have taken out and the number of stocks that it contains
- `Ledger`: This is a dict, where the keys are stock IDs and they map to lists of positions taken out for a given ID. This is the object that tracks what the positions have been and contains methods to calculate interesting metrics, e.g. sharpe ratio.

### Strategies
This file contains the main code for different strategies we want to employ. There are two main files:
- `StrategyName.py`: An enum that names all the different strategies that we want to implement.
- `Strategy.py`: An ABC that has a name member variable (from the `StrategyName` enum) and implements an abstract method, `trade_strategy`, that calculates the position signals for a given data set.


## Implementation of Specific Strategies
Up to now, the code that we have described can work with any strategy. However we are interested in testing two specific strategies. 

### Pairs Trading 
We take the linear relationships and the pairs generated in https://github.com/DomincDootson/Pairs_Selection_with_Clustering. To implement the strategy we create a `Pair` class that holds information about each pair and implements methods of when to buy and sell. We buy when the absolute value of the spread is over 2 std from the mean and sell once the absolute value returns below 1 std. We obtain the following results:

- **Sharpe Ratio**: 2.04
- **Annual Returns**: 6.21%
- **Annual Volatility**: 1.33%

For more information about the algorithm, we prototype it in the linked repo. 

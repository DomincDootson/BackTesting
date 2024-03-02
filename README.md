# BackTesting 
The aim of this code is to implement different trading strategies and to backtest them to evaluate their results.  

## Code Overview
### BackTesting 

### Metrics 
This file contains the main code for calculating the different metrics of interest. There are two main files:
- `MetricName.py`: An enum that names all the different metrics that we want to implement
- `Metric.py`: An ABC that has a name member variable (from the `MetricName` enum) and implements an abstract method to calculate the metric given a trading history

The rest of the files inherit from `Metric` and implement the different metrics. 

### Strategies
This file contains the main code for different strategies we want to employ. There are two main files:
- `StrategyName.py`: An enum that names all the different strategies that we want to implement.
- `Strategy.py`: An ABC that has a name member variable (from the `StrategyName` enum) and implements an abstract method, `generate_signals`, that calculates the buy, sell and hold signals for a given data set.

The rest of the files are specific examples of strategies that inherit from `Strategy`


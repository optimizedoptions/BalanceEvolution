This package allows the user to estimate the evolution of a trading account after a prescribed 
number of trades using a Monte Carlo (MC) algorithm. The input of the algorithm is the winning ratio 
and the risk-reward relation associated with a trading plan, which supposedly has been extensively 
tested by the user.

The *mc* module implements a single class, *Simulation*, which should be instantiated by the user and 
which provides a number of methods and properties, such as the ones for calculating the average balance of the 
MC-generated trading paths, giving an estimate of the long run performance of a trading plan, and, perhaps 
more importantly, the probability of ruin, which is the probability of zeroing out a trading account when 
the trader strictly follows a trading plan.

### Basic Usage Example

---

    # Estimate of the probability of ruin of a trading strategy
    
    # Input variables
    winratio=0.40     # Winning ratio of the strategy (must be between 0 and 1)
    capital=1000.0    # Initial capital
    profit=20.0       # Profit per winning trade (must be a positive number)
    loss=-10.0        # Loss per losing trade (must be a negative number)
    npaths=1000       # Number of independent trading paths
    ntrades=1000      # Maximum number of trades per trading path

    # Run a Monte Carlo simulation
    from BalanceEvolution import mc

    s=mc.Simulation()
    s.setparams(winratio,capital,profit,loss,npaths,ntrades)
    s.run()

    # Plot trading paths
    s.plottradingpaths()

    # Plot histogram of final account balances
    s.plothist()

    # Average balance, standard devation, maximum and minimum
    s.getavgbalance()

    # Avgerage consecutive wins, stdandard deviation, maximum and minimum
    s.getavgconsecutivewins()

    # Avgerage consecutive losses, stdandard deviation, maximum and minimum
    s.getavgconsecutivelosses()

    # Probability of ruin
    print(s.ruinprob)


from setuptools import setup

setup(name='BalanceEvolution',
      version='0.1',
      description="It allows to perform Monte Carlo simulations of the evolution of a trading account based on the winning ratio of a trading strategy."
      requires=['scipy','numpy','matplotlib'],
      author='Optimized Options',
      url="https://github.com/optimizedoptions/BalanceEvolution",
      packages=['BalanceEvolution'])

from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(name='BalanceEvolution',
      version='0.1.1',
      description="Monte Carlo simulations of the trading account evolution based on the winning ratio and risk-reward relation of a trading plan.",
      long_description_content_type='text/markdown',
      long_description=read('Readme.MD'),
      requires=['scipy','numpy','matplotlib'],
      author='Optimized Options',
      url="https://github.com/optimizedoptions/BalanceEvolution",
      packages=['BalanceEvolution'])



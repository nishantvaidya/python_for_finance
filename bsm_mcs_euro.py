##
#Monte Carlo valuation of European call option
# in Black-Scholes-Merton model
# bsm_mcs_euro.py
##
import numpy as np

# Parameter values
s0= 100 # Initial index level
k=105 # Strike Price
T=1.0 # time to maturity
r = 0.5 # Riskless short rate 
sigma = 0.2 # Volatility

I= 100000  # Number of Simulation

# Valuation algorithm #pseduorandom number
z = np.random.standard_normal(I)
ST= s0 * np.exp(( r - 0.5 * sigma ** 2 ) * T + sigma * np.sqrt(T) * z)
# Index value at maturity
ht = np.maximum( ST - k, 0 ) # Inner value at maturity
c0 = np.exp(-r * T) * np.sum(ht)/ I  # Monte carlo estimator

#Result output

print("Value of the European Call Option %5.3f" %c0)
#_________ Importing required Libraries _________________
from cmath import log
from statistics import NormalDist as ND
import math

#_____________ Function Definition _____________________
def NormalMixDF(x, mu, sigma=[0,0], theta0=0.5, log_p=False):
    # Adjusting Sigma Values
    if sigma[0] <= 0.001 or sigma[1] <= 0.001:
        sigma[0] = 0.01 + abs(mu[0]) + abs(mu[1])
        sigma[1] = 0.01 + abs(mu[0]) + abs(mu[1])
    
    # Listing theta values
    theta = [theta0, 1-theta0]

    # To hold Summation
    sum_cdf=0

    # Using Loop, So that this function can be tweaked for higher k values
    for i in [0, 1]:
        # calculating normal distribution for given paramaters
        dist_cal = ND(mu=mu[i], sigma=sigma[i])
        # parameter for CDF
        param_cal = (x-mu[i]) / sigma[i]
        # Calculating the given function
        sum_cdf = sum_cdf + dist_cal.cdf(x=param_cal) * theta[i]
    
    # Checking Log_p
    if log_p is False:
        return round(sum_cdf, 5)
    else:
        return round(math.log(sum_cdf), 5)
    # results rounded to 5 digits.

# Example Case:
print(NormalMixDF(x=0, mu=[-1.0, 1.0], sigma=[0.5, 1.0]))

# Test Cases:
print(NormalMixDF(x=2, mu=[0, 1.5]))
print(NormalMixDF(x=2, mu=[0, 1.5], sigma=[1.0, 1.0]))
print(NormalMixDF(x=2, mu=[0, 1.5], sigma=[1.0, 1.0], theta0=0.8))
print(NormalMixDF(x=2, mu=[0, 1.5], theta0=0.8, log_p=True))
print(NormalMixDF(x=2, mu=[0, 1.5], sigma=[1.0, 1.0]))
print(NormalMixDF(x=1, mu=[-1.3, 2.5], sigma=[1.0, 1.0]))
print(NormalMixDF(x=1, mu=[-1.3, 2.5]))


# When I wrote this code, only God and I understood what I did. Now only God knows.
#______________ THANK YOU ____________________

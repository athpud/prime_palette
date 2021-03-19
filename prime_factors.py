import numpy as np
import pandas as pd

def prime_factors(number):
    """ Returns a list of prime factors of an input number. """
    
    prime_factors = []
    x = 333
    dividend = number
    divisor = 2
    
    while x == 333:
        if dividend == 1:
            return prime_factors
        else:    
            if dividend % divisor == 0:
                prime_factors.append(divisor)
                dividend = dividend/divisor 
            else:
                divisor += 1
                
def prime_df(number):
    """ Returns a list of prime factors of a range of numbers from 2 to the input number. """

    num_prime_array = np.array(([2, 2, 1]))

    if number > 2:    
        for this_num in range(3, number+1):
            num_primes = prime_factors(this_num)
    
            #saving out numbers' unique primes and their counts into a dataframe:
            if this_num > 1:
                unique, counts = np.unique(num_primes, return_counts=True)
                freq = np.asarray((list(unique), list(counts))).T
                num_id = np.array([[this_num] * len(freq)]).T
                num_id_unique_counts = np.hstack((num_id, freq))
                num_prime_array = np.vstack((num_prime_array, num_id_unique_counts))
        num_prime_df = pd.DataFrame(num_prime_array)
    else:
        num_prime_df = pd.DataFrame([num_prime_array], index=[0])
        
    num_prime_df.columns = ['Numbers', 'Primes', 'Powers']
    return num_prime_df
    
    
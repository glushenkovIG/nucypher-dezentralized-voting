import random
from umbral.utils import poly_eval, lambda_coeff

prime = 2**127 - 1
n_voters = 100
n_authorities = 10

choices = [1, -1]
votes = random.sample(choibces, n_voters)
polynoms = [[random.randint(prime) for _ in range(n_authorities - 1)] for _ in range(n_voters)]
for i in range(n_voters):
    polynoms[i] = [votes[i]] + polynoms[i]

autorities_keys = [random.randint(prime)]

vote_parts = [[poly_eval(polynom, key) for polynom in polynoms] for key in authority_keys]
    

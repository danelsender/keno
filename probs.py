from math import comb

def hypergeometric_probability(population_size, success_states, sample_size, desired_successes):
   """
   Calculates the probabilities of the hypergeometric distribution.
   
   Parameters:
   - population_size: the size of the population
   - success_states: the number of success states in the population
   - sample_size: the size of the sample drawn from the population
   - desired_successes: the number of desired successes in the sample
   
   Returns:
   - The probability of getting the desired number of successes in the sample
   """
   numerator = comb(success_states, desired_successes) * comb(population_size - success_states, sample_size - desired_successes)
   denominator = comb(population_size, sample_size)
   probability = numerator / denominator
   return probability

success_states = 10
desired_successes = [5,6,7,8,9,10]
population_size = 80
sample_size = 20
probability = []

for desired_success in desired_successes:
   probability.append(hypergeometric_probability(population_size, success_states, sample_size, desired_success))

print(probability)

# for desired_success, probability in zip(desired_successes, probability):   
#    # print(f"{desired_success} matches: {probability:.10f}")
#    print(f"{desired_success} matches: {probability:.10f}")

# Output:
# 5 matches: 0.0514276877
# 6 matches: 0.0114793946
# 7 matches: 0.0016111431
# 8 matches: 0.0001354194
# 9 matches: 0.0000061206
# 10 matches: 0.0000001122

def generate_fair_odds(probabilities):
   """
   Generates fair odds based on the given probabilities.
   
   Parameters:
   - probabilities: a list of probabilities
   
   Returns:
   - A list of fair odds corresponding to the given probabilities
   """
   fair_odds = [1 / probability for probability in probabilities]
   return fair_odds

fair_odds = generate_fair_odds(probability)
print(fair_odds)
for desired_success, fair_odd in zip(desired_successes, fair_odds):
   print(f"{desired_success} matches: {fair_odd/len(desired_successes):.10f}")

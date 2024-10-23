from math import comb

def calculate_probability(i, j):
   """calculate the probability of getting a match on the ith
   draw given j matches"""
   total_numbers = 80  # Total numbers in the game of keno
   drawn_numbers = 20  # Numbers drawn in each round of keno
   selected_numbers = 10  # Numbers selected by the player

   # Calculate the probability using the formula:
   probability = (comb(selected_numbers, j) * comb(total_numbers - selected_numbers, i - j)) / comb(total_numbers, i)

   return probability

def payout(matches, bet_amount = 1):
   """Pay tables for game"""
   if matches < 5:
      value = 0
   elif matches == 5:
      value = 3
   elif matches == 6:
      value = 15
   elif matches == 7:
      value = 100
   elif matches == 8:
      value = 1000
   elif matches == 9:
      value = 25000
   elif matches == 10:
      value = 2500000
      
   return bet_amount * value

for j in range(0,10):
   for i in range(0, 20):
      if j <= i: 
         probability = calculate_probability(i+1, j+1)
         print(f"{i,j} matches: {probability:.10f}/n Expected value: {probability * payout(j+1, 1):.10f}")
      else:
         pass
      
import random
import operator
from numba import njit
import numpy as np
import time

testing = False

#@njit()
def generate_numbers(N):
   """Generate n random numbers between 1 and 80."""
   numbers = np.arange(1, 81)
   np.random.shuffle(numbers)
   return numbers[:N]


#@njit()
def play_keno():
   """Simulate a game of Keno."""
   if not testing:
      print("Welcome to Keno!")
      print("You need to select 10 numbers between 1 and 80.")
      print("If your numbers match the randomly generated numbers, you win!")
      print("In this game payouts are as follows:")
      print("5 matches: 3x your bet")
      print("6 matches: 15x your bet")
      print("7 matches: 100x your bet")
      print("8 matches: 1000x your bet")
      print("9 matches: 25000x your bet")
      print("10 matches: 2500000x your bet")
      print("The stake is set to £1 per game.")
      print("Good luck!")

   
      # Get user's numbers
      user_numbers = set()
      while len(user_numbers) < 10:
         try:
            number = int(input("Enter a number between 1 and 80: "))
            if 1 <= number <= 80:
               if operator.contains(user_numbers, number):
                  print("Number already selected. Please try again.")
               else:   
                  user_numbers.add(number)
            else:
               print("Invalid number. Please try again.")
         except ValueError:
            print("Invalid input. Please enter a number.")

      bet_amount = 1
   else:
      # user_numbers = np.random.default_rng.integers(81, size=10, replace=False)
      user_numbers = generate_numbers(10)
      bet_amount = 1
   
   # Generate random numbers
   generated_numbers = generate_numbers(20)

   # Check for matches
   if testing:
      matches = np.intersect1d(user_numbers, generated_numbers)
   else:
      matches = user_numbers.intersection(generated_numbers)

   if not testing:
      # Print results
      print("Your numbers:", user_numbers)
      print("Generated numbers:", generated_numbers)
      print("Matches:", matches)
      print("You matched", len(matches), "numbers!")

      if len(matches) == 10:
         print("Congratulations! You won the jackpot!")
      
   return matches, bet_amount

if not testing:
   
   matches, bet_amount = play_keno()
   
   # Get user's bet amount
   if len(matches) < 5:
      print("You need to match at least 5 numbers to win.")

   # Calculate payout based on the number of matches
   if len(matches) == 10:
      payout = bet_amount * 2500000
   elif len(matches) == 9:
      payout = bet_amount * 25000
   elif len(matches) == 8:
      payout = bet_amount * 1000
   elif len(matches) == 7:
      payout = bet_amount * 100
   elif len(matches) == 6:
      payout = bet_amount * 15
   elif len(matches) == 5:
      payout = bet_amount * 3
   elif len(matches) < 5:
      payout = 0

   # Print payout
   if payout >= 5:
      print("Congratulations! You won $", payout)
   else:
      print("Better luck next time!")
   
else:
   
   # Simulate n games
   n_games = int(input("Enter the number of games to simulate: "))
   
   @njit()
   def multiple_games(n_games):
      total_wager = 0
      total_payout = 0
      for i in range(n_games):
         matches, bet_amount = play_keno()
      # Calculate total wager
         total_wager += bet_amount
         
         # Calculate total payout
         if len(matches) == 10:
            total_payout += bet_amount * 2500000
         elif len(matches) == 9:
            total_payout += bet_amount * 25000
         elif len(matches) == 8:
            total_payout += bet_amount * 1000
         elif len(matches) == 7:
            total_payout += bet_amount * 100
         elif len(matches) == 6:
            total_payout += bet_amount * 15
         elif len(matches) == 5:
            total_payout += bet_amount * 3
         else:
            pass
         
      print("Total wager:", total_wager)
      print("Total payout:", total_payout)
   if testing: start = time.time()
   multiple_games(n_games)
   if testing:
      end = time.time()
      print("Time taken:", end - start)
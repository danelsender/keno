#--------------------------------------------------#
# pointsTest.py                                    #
#--------------------------------------------------#
# Description:                                     #
#                                                  #
# Finds number of points in number.txt file that   #
# exist in each interval given in the extents.txt  #
# file. The number of points in each interval      #
# are written to the counts.txt file.              #
# The count.txt file is then cross referenced with #
# the expected.txt file.                           #
#                                                  #
# Author: Daniel Elsender                          #
# Date: 23.10.2024                                 #
#--------------------------------------------------#

import numpy as np
import timeit

def compare_counts_with_expected(counts_file, expected_file):
   """Function to compare counts.txt with expected.txt
   input: counts_file, expected_file
   
   output: success or fail message is returned"""
   with open(counts_file, 'r') as file:
      counts = [int(line.strip()) for line in file]
   
   with open(expected_file, 'r') as file:
      expected = [int(line.strip()) for line in file]
      
   for count, expected in zip(counts, expected):
      if count != expected:
         return print(f"Expected {expected}, got {count}")
      
   return print("All counts match expected values.")
   

def read_extents(file_path):
   """Function to read extents from file
   
   input: file_path
   
   output: extents as numpy array"""
   
   extents = []
   with open(file_path, 'r') as file:
      for line in file:
         a, b = map(int, line.split())
         extents.append((a, b))
   return np.array(extents)

def read_points(file_path):
   """Function to read points from file
   
   input: file_path
   
   output: points as numpy array"""
   
   points = []
   with open(file_path, 'r') as file:
      for line in file:
         points.append(int(line.strip()))
   return np.array(points)

def count_ranges_containing_points(extents, points):
   """Function to count the number of points in each interval
   
   input: extents, points
   
   output: counts as numpy array"""
   
   # initialise the counts array
   counts = np.zeros(len(points), dtype=int)
   
   # for each point sum the number of intervals within which
   # the point lies
   # leverage numpy broadcasting to perform the comparison
   # for each point with all intervals
   for i, point in enumerate(points):
      counts[i] = np.sum((extents[:, 0] <= point) & (extents[:, 1] >= point))
   return counts


def main():
   """Main function to read extents and points from file,
   count the number of points in each interval and write
   the counts to file"""
   
   # read extents and points from file
   extents = read_extents('extents.txt')
   # print(extents)
   points = read_points('numbers.txt')
   
   # perform the counts
   counts = count_ranges_containing_points(extents, points)

   # # write counts to file
   with open('counts.txt', 'w') as file:
      for count in counts:
         file.write(str(count) + '\n')

if __name__ == "__main__":
   
   # call main()
   start = timeit.default_timer()
   main()
   end = timeit.default_timer()
   print(f"Execution time: {end - start}")
   
   # compare counts.txt with expected.txt
   compare_counts_with_expected('counts.txt', 'expected.txt')
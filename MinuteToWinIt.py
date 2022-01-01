
'''
Submissions will no longer be placed on the leaderboard. You may still attempt this problem for practice.
In a new version of the game Minute to Win It, the math round involves manipulating arrays to meet the given condition. In the challenge, you are given an array of  numbers  and an integer . In one minute, you can change any element of the array to any integer you want. Find the minimum amount of time you have to spend so that the following condition is satisfied: for all  from  to , .

For example, consider the array  and . Then the condition can be satisfied in  minute by replacing the  with a .

image

Complete the function minuteToWinIt which accepts an array  of  integers and an integer  as input and returns the minimum amount of time in minutes.

Input Format

The first line contains two space-separated integers  and .

The second line contains the array in the form of  space-separated integers .

Constraints

Output Format

Print the minimum number of minutes needed to reorder the array.

Sample Input 0

6 2
1 2 5 7 9 85
'''
import pandas as pd
import time
import numpy as np

array = [1, 2, 5, 7, 9, 85]
array = np.random.randint(1,10000, 3000)


def shift_array(array, k=2):
    first_timestamp = time.time()
    for i in range(len(array)):
        # for the first number
        if i == 0:
            if array[i+1]-array[i]==k:
                pass
            else:
                array[i+1] = array[i]+k
        # for the rest of the numbers
        if i < len(array) and i != 0:
            if (array[i] - array[i-1] == k) and (array[i+1]-array[i]==k):
                pass
            else:
                array[i] = array[i-1]+k
    delta_time = time.time() - first_timestamp 
    return array, delta_time



array, delta_time = shift_array(array, k=3)
print(array, delta_time)

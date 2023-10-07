
# Mon Sep 26 00:44:17 2022
def run_length(input_string):
  """ return the run length encoding for a given input string
      aabcccd : 2a1b3c1d
      Corner cases: non adjacent repetition, case sensitive
      Error out with numeric inputs
  """
  output=""
  count=0
  if input_string is None:
    return 0
  size = len(input_string)
  for i in range(1,size):
    if input_string[i - 1]!=input_string[i] or i==size-1:
      count = count + (1 if input_string[i]==input_string[i-1] else 0)
      output+= str(count) + input_string[i-1]
      count=1
    else:
      count=count+1
    #print(input_string[i])
  print(output)



# amazon shiping will group packages according to weight
# ligher package canbe merged with heavcvier package 
# which eliimate the need for shipments

''' n packages
# packageWeights[i] represent weight of ith package
# combine ith with i+1th if pW[i]<pw[i+1]
then discard ith package. after this #packages
reduces by 1 and the packae weight increases by pw[i]
you can merge any number of times
'''

## Complete the 'getHeaviestPackage' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY packageWeights as parameter.
#

#!/opt/miniconda/bin/python 
import math
import os
import random
import re
import sys

def getHeaviestPackage(packageWeights):
    # A recursive approach may help here: 
    # Check if 1st and 2nd can be combined, if not move on to the next, combine them and call get Heaviest on the resulting array
    
    # check boundary conditions 
    if len(packageWeights)==1:
        return packageWeights[0]
    
    
    max_impact_index=-10
    max_weight =-10
    for i in range(len(packageWeights)-1):
        if packageWeights[i] < packageWeights [i+1]:
            tmp = packageWeights[i]+packageWeights[i+1]                          
            if max_weight < tmp:                
                max_impact_index = i
                max_weight = tmp             
    
    if max_impact_index !=-10:
        packageWeights[max_impact_index+1] += packageWeights[max_impact_index]                
        del[packageWeights[max_impact_index]]
    #print(packageWeights)   
    
    sorted_list = packageWeights.copy()
    reversed_list = packageWeights.copy()
    sorted_list.sort()
    reversed_list.reverse()
    print(sorted_list , reversed_list)
    if sorted_list == reversed_list:
        return max(packageWeights)
    else:
        return getHeaviestPackage(packageWeights)        


pw = [2, 9, 10,3,7]
#$pw = [20,13,8,9]
print("Heaviest package", getHeaviestPackage(pw))

'''
Several data center with multiple processors 
processor are placed ina sequence ID- 1, 2, 3.. n

Each processors  consumes power 
1. bootingPower[i]
2. processingPower[i] 

we want to cluster them for max utilzization
Clusters can be formed of processors located adjacent
2,3,4,5 can form cluster 1,3,4 cannot 

Net power of cluster of k processor(i,..i+k-1)
 max(bootingPower(i,...i+k=1_))
 + 
 k*Sum(processing power[j])

 bootingpower=[3,6,1,3,4]
 processingpower=[2,1,3,4,5]
 powerMax=25
 k = 2, 4+ (4+5)*2 = 22
 k = 3, 6+ (2+1+3)*3 = 24 
 format - 
 processing power size 
 followed by processing power
 botting power size 
 followed by bootuing power 
 powermax
'''

'''A cafeteria table consists of a row of NNN seats, numbered from 111 to NNN from
left to right. Social distancing guidelines require that every diner be seated
such that KKK seats their left and KKK seats to their right (or all the
remaining seats to that side if there are fewer than KKK) remain empty.
There are currently MMM diners seated at the table, the iiith of whom is in
seat SiS_iSi​. No two diners are sitting in the same seat, and the social
distancing guidelines are satisfied.  Determine the maximum number of
additional diners who can potentially sit at the table without social
distancing guidelines being violated for any new or existing diners, assuming
that the existing diners cannot move and that the additional diners will
cooperate to maximize how many of them can sit down.  Please take care to write
a solution which runs within the time limit.

Constraints outdoor
1≤N≤10151 \le N \le 10^{15}1≤N≤1015
1≤K≤N1 \le K \le N1≤K≤N
1≤M≤500,0001 \le M \le 500{,}0001≤M≤500,000
1≤Si≤N1 \le S_i \le N1≤Si​≤N}})
'''


N = 15
K = 2
M = 3 
S = [11,6,14]
N =10
K =1
M=2
S=[2,6]

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: list[int]) -> int:
  sum = 0;
  S.sort()
  for i in range(M-1):
    sum += (abs(S[i+1]-S[i])-3)//(2*K+1)
    print(S[i],"--", S[i+1]-S[i]-1, S[i]+K+1, sum)
    
  sum = sum + (N-S[-1]-1)//(K+1)
  print(sum, N-S[-1])
  sum = sum + (S[0]-1)//(K+1)
  print(sum, S[0]-1)
  return sum

getMaxAdditionalDinersCount(N,K,M,S)



'''

Consider following matrix M 
  0 1 2 
0 1 1 0
1 1 1 0
1 0 0 1

M[i]j[] determines if j was gifted a book by i
0 gifted 1 => connected
0 gifted 0 => connected
so two groups
'''

def countgrops( related array, related_arry_count):
    nop 
    #return related_groups



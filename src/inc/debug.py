
import sys
import re
import os
import subprocess
import shutil
import time
import timeit
import argparse
import glob
import signal
import shlex
import gzip
from datetime import datetime
from multiprocessing import Process
import getpass
import traceback
import logging
import fcntl
import errno
import stat
import random
import smtplib
#from email.mime.text import MIME

class MyClass():
  #constructor
  def __init__(self):
    self.a = None
    self.b = None

def  main():
  start =timeit.default_timer()

  try:
    return 1
  except Exception as e:
    traceback.print_exc()

# Usage of dict
def solution(data, n):
  frequency = {}
  if (n >=0):
    for i in data:
      getCount = frequency.setdefault(i,0)
      frequency[i] = frequency[i] + 1

    for key,value in frequency.items():
      print(key,value)
      if value > n:
        for i in range(value):
          data.remove(key)
data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
n=1
# solution(data,n)
# print(data)

# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes

def SieveOfEratosthenes(n):
  # Create a boolean array "prime[0..n]" and initialize
  # all entries it as true. A value in prime[i] will
  # finally be false if i is Not a prime, else true.
  prime = [True for i in range(n + 1)]
  p = 2
  while (p * p <= n):

    # If prime[p] is not changed, then it is a prime
    if (prime[p] == True):

      # Update all multiples of p
      for i in range(p * 2, n + 1, p):
        prime[i] = False
    p += 1

  # Print all prime numbers
  for p in range(2, n):
    if prime[p]:
      print
      p,


if __name__ == '__main__':
  main()

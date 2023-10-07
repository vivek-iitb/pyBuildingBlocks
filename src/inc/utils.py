import sys

def binary_repr()-> str:
  n = [13, 25,1,0]
  for num in n:
    while( num > 1 ):     
      bit = (num) % 2
      print( bit , end=" ")
      num=num//2
    print()

binary_repr()


def float_binary(val:float)->str:
  pass

def decimal_to_binary(num):
    # check if number is negative
    if num < 0:
        sign = "1"
        num = -num
    else:
        sign = "0"

    # separate integer and fractional parts
    integer_part = int(num)
    fractional_part = num - integer_part

    # convert integer part to binary
    binary = ""
    while integer_part > 0:
        binary = str(integer_part % 2) + binary
        integer_part //= 2

    # convert fractional part to binary
    binary += "."
    while fractional_part > 0:
        fractional_part *= 2
        if fractional_part >= 1:
            binary += "1"
            fractional_part -= 1
        else:
            binary += "0"

    # return binary representation
    return sign + binary

# example usage
print(decimal_to_binary(0.1))  # prints "0.0001100110011001100110011001100110011001100110011010"

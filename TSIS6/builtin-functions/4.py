from time import sleep
import math
def time_square(m, n):
  l = math.sqrt(n)
  sleep(m/1000)
  return("Square root of {} after {} miliseconds is {}".format(n, m, l))
n = float(input())
m = int(input())
print(time_square(m, n))
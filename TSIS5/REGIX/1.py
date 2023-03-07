import re

str = input() 
match = re.findall(r'ab' and 'a0', str)
# match = re.findall(r'a0' , str)
# If-statement after search() tests if it succeeded
if match:
  print('found: ', match) 
else:
  print('did not find')

nric = input('Enter an NRIC number: ')
# validation
valid = True
if len(nric) != 9:
  valid = False
elif not nric[1:8].isdigit():
  valid = False
elif not nric[-1].isalpha():
  valid = False
first = nric[0]
if first != 'S' and first != 'T' and first != 'G' and   first != 'F':
  valid = False

# check digit
if valid:
  sum = 0
  sum = sum + int(nric[1]) * 2
  sum = sum + int(nric[2]) * 7
  sum = sum + int(nric[3]) * 6
  sum = sum + int(nric[4]) * 5
  sum = sum + int(nric[5]) * 4
  sum = sum + int(nric[6]) * 3
  sum = sum + int(nric[7]) * 2
  if nric.startswith('T') or nric.startswith('G'):
    sum = sum + 4
  
  st_digits = "JZIHGFEDCBA"
  fg_digits = "XWUTRQPNMLK"
  sum = sum % 11
  
  if nric.startswith('S') or nric.startswith('T'):
    if st_digits[sum] != nric[-1]:
        valid = False
  if nric.startswith('F') or nric.startswith('G'):
    if st_digits[sum] != nric[-1]:
        valid = False

if valid:
  print("NRIC is valid.")
else:
  print("NRIC is invalid.")
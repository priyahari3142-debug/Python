x = int(input())
st = str(x)
rev = st[::-1]
if rev==st:
  print("Palindrome")
else:
  print("Not a Palindrome")

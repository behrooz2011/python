def is_palindrome(input_string):
  new_string = ""
  reverse_string = ""
  for x in input_string:
    new_string=new_string+x
  new_string=new_string.replace(" ","")
  new_string=new_string.lower()
  
  length = len(new_string)
  for y in range(length):
    reverse_string += new_string[length-y-1]
  if new_string == reverse_string:
    return True
  return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

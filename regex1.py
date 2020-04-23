# 

import re
# result = re.search(r"aza","plaza")
# print(result

def check_zip_code(text):
  result = re.search(r"(\s(\d{5})\D|\s(\d{5})-(\d{4})\D)", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-00012.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


print(re.findall(r"(\d{3})","ello 12345 and 123 and 456 and "))
print(re.findall(r"(\bare\b|\bis\b)", "I am you are he is is are"))#[ are is is are]
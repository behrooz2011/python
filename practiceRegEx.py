import re
def contains_acronym(x):
  res=re.search(r"[(][A-Z][a-zA-Z0-9]*[)]|[(][0-9][a-zA-Z0-9]*[)]", x)
  return res
print(contains_acronym(" Instant messaging (IM) is a set of communication technologies used for text-based communication"))


print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False

 
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

def func1(x):
  res=re.match(r"[A-Z]",x)
  return res
print(func1("Hello Everyone"))

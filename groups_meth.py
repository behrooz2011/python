# #groups()

import re
# result = re.search(r"^(\w*)\+\?\_  (\w*)$","Smith222+?_  Joe")# two spaces are added in the pattern
# result1 = re.search(r"^(\w*), (\w*)$","Mac, paul")
# result2=  re.search(r"^(\w*),(\w*)$","_Smith,Jgool")

# print(result)
# print(result1)
# print(result2)

# print("\n a line would come here \\n \n")

# print(result[0])
# print(result[1])
# print(result[2])
# print(result.groups())


# res = re.search(r"[0-4][0,1,9]\s","this is the first number 4222 and second 01 and 192 ok? ")
# res2 = re.findall(r"[0-4][0,1,2,9]*\s","this is the first number 4221 and second 01 and 119 ok? ")

# print(res)
# print(res2)
# print("\n using indexing method: \n")
# print(res[0])
# # print(res[1])
# # print(res[2])
# # print(res[3])
# # print(res2[4])


# print("\n using groups() method: \n")
# print(res.groups())
# print(res2.groups())

# print("\n string search: \n")
# newr= re.search(r"(\w*)  (\w*)","Hello everyone I would  like to  introduce  you")
# print(newr)
# print(newr[0])
# print(newr[1])
# print(newr[2])
# print(newr.groups())
# print(newr[3])
# print(newr[4])



# def rearrange_name(name):
#   result = re.search(r"^[a-zA-Z]* [a-zA-Z]*, [a-zA-Z]*", name)
#   # if result == None:
#   #   return name
#   # print("\n this a function: \n")
#   # print(result)
#   return "{} {}".format(result[2], result[1])

# name=rearrange_name("Kennedy, John F.")
# print(name)
# print(rearrange_name("Kennnnni, Joooo"))
# print(rearrange_name("Davis Boor, Jake"))

# x = re.search(r"[a-zA-Z]* [a-zA-Z]*, [a-zA-Z]*", "Davis Boor, Jake is a great guy")
# print(x[0])
# print(x.groups())


# aaa=("salam","doostan")
# print(aaa[1])

# plus = re.search(r"o+l+","hollp")
# plus1 = re.search(r"o+l+","hoooolp")
# plus2 = re.search(r"o+l+","holp")
# plus3 = re.search(r"o+l","hoolllllllp")

# print("\n here comes the plus regex: \n")
# print(plus)
# print(plus1)
# print(plus2)
# print(plus3)

res = re.search(r"^([\w \.-]*,) ([\w \.-])*$","Pat, David Basis ")
print(res)
print(res[0])
print(res.groups())
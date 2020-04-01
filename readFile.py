
# def main():
# 	f= open("gm.txt","r")
# 	if f.mode=="r":
# 		print(f.read())
# 	print(f.readline())
# 	print(2**15)

print(2**15)
# goo = open("guru99.txt", "r")

# print(goo.read())
# print(len(goo.read()))
# print(2**15)
with open("guru99.txt",encoding="utf8") as file:
	for line in file:
		print(line.strip())
		print(type(line))


#Roman to Integer
exp={
"IV":4,
"IX":9,
"XL":40,
"XC":90,
"CD":400,
"CM":900
}
norm={
"I":1,
"V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000
}


gg="hello"
print(gg[0]+gg[1])

print("Enter your roman number in Capital letters: ")
num=input()
arr=[]
if len(num) % 2 == 0:
    for i in range(0,len(num)):
        if 2*i <len(num)-1:
            y=num[len(num)-2-2*i]+num[len(num)-1-2*i]
            arr.append(y)
    print(arr)
else:
    for i in range(0,len(num)):
        if 2*i <len(num)-1:
            y=num[len(num)-2-2*i]+num[len(num)-1-2*i]
            arr.append(y)
    arr.append(num[0])
    print(arr)

solution= 0
for x in arr:
    if x in exp:
        solution += exp[x]
    else:
        if len(x) == 1:
            solution += norm[x]
        else:
            solution += norm[x[0]]+norm[x[1]]
print(solution)



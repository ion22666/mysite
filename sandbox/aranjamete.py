import string


s = [1,2,3,4,5,6,7,8]
i=0
while True:
    string = ""
    a = bin(i)[2:]
    if len(a)<len(s):
        a=((len(s)-len(a))*"0")+a
        
    for j in range(len(s)):
        if a[j]=="1":
            string+=str(s[j])
    if string=="":print("_")
    else:print(string)
    i+=1
    if a == (len(s)*"1"):
        break
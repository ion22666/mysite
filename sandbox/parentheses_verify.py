def generateParenthesis(n = 1,str="",openS=0,closeS=0):
    if openS == closeS == n:
        print(str)
        return
    if openS < n:
        str+="("
        generateParenthesis(n,str,openS+1,closeS)
        str=str[0:-1]
    if closeS < openS:
        str+=")"
        generateParenthesis(n,str,openS,closeS+1)
        str=str[0:-1]
generateParenthesis()
# cate inchise atatea si deshise
# 



'''class Paranteze:
    paranteze_deschise = ["(","[","{"]
    paranteze_inchise = [")","]","}"]
    def __init__(self,string):
        self.string = string
        print("parantezele: ",string," este ",self.is_valid())

    def is_valid(self):
        s = self.string
        for i in range(len(s)):
            if s[i] in  self.paranteze_deschise:
                return "valabil"
            else:
                return "nevalabil"'''






#p = Paranteze("()")
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            print(stack)
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
#stack = [ (     ]
print(py_solution().is_valid_parenthese("()()()()()()()()()()()())()()"))

from math import floor
import string

class Numbers:
    global roman_numerals,roman_numerals_combinations
    roman_numerals = {
        "M":1000,
        "CM":900,
        "D":500,
        "CD":400,
        "C":100,
        "XC":90,
        "L":50,
        "XL":40,
        "X":10,
        "IX":9,
        "V":5,
        "IV":4,
        "I":1
        }

    def __init__(self ,decimal_form=None , roman_form=None ):

        if type(decimal_form)==type("a"):
            roman_form = decimal_form
            decimal_form = None

        if not decimal_form and not roman_form:
            self = Numbers.creare_obiect()

        elif decimal_form and roman_form:
            self.decimal_form = decimal_form
            self.roman_form = roman_form
            self.print_number_when_created()

        elif roman_form:#din roman in decimal
            decimal_form = 0
            self.roman_form = roman_form
            i = 0
            for litera in roman_form:
                if i+1!=len(roman_form) and (litera+roman_form[i+1]) in roman_numerals.keys():
                        decimal_form+=-roman_numerals[litera]
                else:
                    decimal_form+=roman_numerals[litera]
                i+=1

            self.decimal_form = decimal_form
            self.print_number_when_created()
            return

        elif decimal_form:#din decimal in roman
            self.decimal_form = decimal_form
            roman_form = ""
            rest = decimal_form
            for litera,valoare in roman_numerals.items():
                catul = (floor(rest/valoare))
                roman_form += catul * litera
                rest = rest - (catul * valoare)
                if rest == 0:
                    break
            self.roman_form = roman_form
            self.print_number_when_created()

    def print_number_when_created(self):
        print("a fost creat un numaru: ",end="")
        s = ""
        for value in self.__dict__.values():
           s+=str(value)+" / "
        s= s[0:-2]
        print(s)

    def creare_obiect():
        print("Acum creati un obiect(lasa gol daca nu stii):")
        decimal_form = input("forma decimala: ")
        if decimal_form:
            decimal_form = int(decimal_form)
            return Numbers(decimal_form,None)
        roman_form = input("forma romana: ")
        if roman_form:
            return Numbers(None,roman_form)
        print("aia e , daca nu stii numerele")
        return

Numbers("VI")
print(globals())
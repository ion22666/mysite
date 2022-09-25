from ast import Num, Pass
from math import floor
import numbers
import re

class Numbers:
    global roman_numerals,roman_numerals_combinations
    roman_numerals = {
        "M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1
        }
    roman_numerals_combinations = {
        "CM":900,
        "CD":400,
        "XC":90,
        "XL":40,
        "IX":9,
        "IV":4

    }

    def __init__(self ,decimal_form=None , roman_form=None ):

        if not decimal_form and not roman_form:
            print("e nevoie de cel putin o forma pentru a crea un numar (numarul a fot sters)")
            del self

        elif decimal_form and roman_form:
            self.decimal_form = decimal_form
            self.roman_form = roman_form
            self.print_number_when_created()

        elif roman_form:#din roman in decimal
            decimal_form = 0
            self.roman_form = roman_form
            for litera,i in zip(roman_form,range(len(roman_form))):
                if i+1==len(roman_form) :
                    decimal_form += roman_numerals[litera]
                    break
                elif roman_numerals[roman_form[i+1]]>roman_numerals[litera]:
                    decimal_form+=-roman_numerals[litera]
                else:
                    decimal_form += roman_numerals[litera]
            self.decimal_form = decimal_form
            self.print_number_when_created()
            return


        elif decimal_form:#din decimal in roman
            self.decimal_form = decimal_form
            roman_form = ""
            rest = decimal_form
            x = dict(sorted((roman_numerals | roman_numerals_combinations).items(), key=lambda item: item[1],reverse=True))
            for litera,valoare in x.items():
                catul = (floor(rest/valoare))
                roman_form += catul * litera
                rest = rest - (catul * valoare)
                if rest == 0:
                    break
                
        self.roman_form = roman_form
        self.print_number_when_created()

    def print_number_when_created(self):
        print("a fost creat un numaru: ", self.decimal_form," / ",self.roman_form)


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
        
        

a1 = Numbers.creare_obiect()

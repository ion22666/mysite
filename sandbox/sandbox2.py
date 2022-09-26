class K:
    def __init__(self,attr1=None):
        if attr1:
            self.attr1 = attr1
            print(self,self.attr1)
            return
        else:
            self = K.creare_obiect()

    def creare_obiect():
        print("Acum creati un obiect(lasa gol daca nu stii):")
        attr1 = input("attr1: ")
        if attr1:
            return K(attr1)
        print("aia e , daca nu stii numerele")
        return

print(type("h"))
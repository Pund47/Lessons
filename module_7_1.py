from pprint import pprint


class Product():
    def __init__(self,name,weight,category):
        self.name      = name
        self.weight    = weight
        self.category  = category
    def __str__(self):
        return (f'{self.name} , {self.weight} ,{self.category}')


class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, "a")
        file.close()
    def get_products(self):
        file = open(self.__file_name,"r")
        pprint(file.read())
        file.close()

    def add(self,*args):
        for prod in  args:
            file = open(self.__file_name, "r")
            if str(prod) in file.read()  :  #and str(prod.weight) in file.read() and prod.category in file.read()
                print(f"Продукт {prod} уже есть в магазине")
            else:
                file.close()
                file = open(self.__file_name, "a")
                file.write(f" {prod} \n")
                file.close()
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
from pprint import pprint


class Product:
    name = ''
    weight = float
    category = ''

    def __init__(self, name, __weight, __category):
        self.name = name
        self.__weight = __weight
        self.__category = __category

    def __str__(self):
        return f'{self.name}, {self.__weight}, {self.__category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):
        f = 0
        file = open(self.__file_name, 'r')
        file.read()
        if file.tell() == 0:
            for j in products:
                file = open(self.__file_name, 'a')
                file.write(f'{j}\n')
                file.close()
        else:
            file.seek(0)
            for j in products:
                l = str(j)
                file.seek(0)
                for i in file:
                    k = i[0: len(i) - 1]
                    if l == k:
                        print(f'продукт {j} уже есть в магазине')
                        break
                    elif l != k:
                        f += 1
                        continue
                    elif f != 0:
                        file = open(self.__file_name, 'a')
                        file.write(f'{k}\n')
                        file.close()
                        f = 0
                        break

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

import os
os.system('cls' if os.name=="nt" else 'clear')
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP
# ---------------------------------------------
# OOP = Object Oriented Programming
# Classes -> BluePrint: Mimarların kullandığı mavi şablon kağıdıdır. Obje orada tanımlanmıştır.
# DRY: Don't Repeat Yourself
# ---------------------------------------------
# def print_type(data_list):
#     for data in data_list:
#         print(data, type(data))

# print_type([ 'Qadir', 123, 123.45, True, (1,2,3), [1,2,3], lambda x:x ])
# ---------------------------------------------
# Temel Kurallar:
# Python'da Class oluşturma:
# class ClassName: # PascalCase yapıda isimlendirilir.

#     variable_for_class = 'value'  # Atrribute/Property

#     # if (Conditions) ... # Wrong Using.

#     def example_function(paramatre, arguman):  # Method
         
#         variable_for_func = 'value'  # Parametre.

#         # if (Conditions)...
# ---------------------------------------------

# class Person:
#     name = 'Qadir'
#     surname = 'Adamson'

# print(Person)
# print(Person.name)
# print(Person.surname)

# Set Object from Class:
# personel = Person() # Instance = Classtan oluşturulmuş obje.

# print(personel)
# print(personel.name)
# print(personel.surname)

# print('----------------')

# personel.name = 'Rafe'
# personel.surname = 'Stefano'
# personel.age = 40

# print(personel.name)
# print(personel.surname)
# print(personel.age)

# print('----------------')

# print(Person.name)
# print(Person.surname)
# print(Person.age) # Instance'da yaptığımız değişkler class'ı ETKİLEMEZ.

# ---------------------------------------------

# Class'da yapılan değişiklikler Inctance'ı ETKİLER.
# class Person:
#     name = 'Qadir'
#     surname = 'Adamson'

# personel_1 = Person()

# print(personel_1.name)
# Person.name = 'Rafe'
# print(personel_1.name)

# ---------------------------------------------
# Bir instance'daki ekleme/güncelleme diğer instance'ı ETKİLEMEZ.
# class Person:
#     name = 'Qadir'
#     surname = 'Adamson'

# personel_1 = Person()
# personel_2 = Person()

# print(personel_1)
# print(personel_2)

# personel_1.name = 'Rafe'
# personel_2.name = 'Victor'

# print(personel_1.name)
# print(personel_2.name)

# personel_1.age = 40

# print(personel_1.age)
# print(personel_2.age)

# ---------------------------------------------

# class Person:
#     name = 'Qadir'
#     surname = 'Adamson'

# personel = Person # personel instance değil, class oldu.
# other_intance = personel() # Yeni class ile instance oluşturuldu.

class Person:
    name = 'Qadir'
    surname = 'Adamson'

    def full_name(self):
        print(f'{self.name} {self.surname}')
    

personel = Person()
personel.name = 'Rafe'
personel.surname = 'Stefano'

Person.full_name(Person)
# personel.full_name()
# print(Person.name)
# print(Person.surname)
# print(Person.full_name(Person))
    



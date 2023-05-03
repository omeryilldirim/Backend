import os
os.system('cls' if os.name=="nt" else 'clear')
# ---------------------------------------------
# ---------------------------------------------
# Python - OOP - 2
# ---------------------------------------------
# Encapcullation: Kapsülleme. Aynı amaç için kullanılan değişken ve methodları bir class içinde yazıyor olmsı
#    ve class içinde tanımlanan private attre erişelmiyor olması.
# Abstraction: Soyutlama. Kodların gizliliği ve birbirinde bağımsız çalışmaları.
# ---------------------------------------------
# Inheritance: Miras Alma. Bir classın tüm özelliklerinin başka bir classa aktarılmasına denir.
# Polymorphism: Miras alınan (inherit edilen) classın özellik/metodlarını yeniden yazılabilyor/değiştirebiliyor olmasına denir.

# ---------------------------------------------

class Person:

    company = 'Clarusway'

    def __init__(self, name, age, gender='Male'):
        self.name = name
        self.age = age
        self.gender = gender
        print('Personel OLuşturuldu.')

    def __str__(self):
        return f'{self.name} - {self.age}'

    def get_detail(self):
        return f'{self.name} - {self.age} - {self.gender} - {self.company}'

# person_1 = Person('Qadir', 40) # Bir classın atandığı değişkene instance denir.
# print(person_1)
# print(person_1.get_detail())

# Inheritance:
# JS -> class Employee extends Person
class Employee(Person):
# Person classının tüm özellikleri Employee classına aktarıldı.

    salary = 5000

person_1 = Employee('Busra', 29, 'Female')
class Car ():
    #constructor: escencia de una clase
    def __init__(self,brand,mode,color, engie_type):
        self.brand = brand
        self.mode = mode
        self.color = color
        self.engie_type = engie_type
        self.__maxprice = 900
        print ("se creo el objeto")

    #definicion de metodos (funcion)    
    def update_color (self, new_color):
        self.color = new_color

    def sell (self):
        print ("precio de venta:",self.__maxprice)

    #metodo setter

    def set_max_price (self, price):
        self.__maxprice = price

car = Car("kia","picanto","blanco","gasolina")
car2 = Car("Ford","Fiesta","Amarillo","gasolina")

##probando la funcion de la clase Car, update_color
car.update_color("negro")
print(car.color)

car . sell ()
#maner de usar un setter para cambia valores
car . set_max_price (1000)
car . sell ()


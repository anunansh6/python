# print(type(36)): output(<class 'int'>)

# class anil :
#     a=34
# print(type(anil()))    


# class car:
#     seater=7
#     wheels=4
# honda=car()
# sujuki=car()
# sujuki.seater=8
# print(honda.seater )
# print(honda.wheels )
# print(sujuki.seater )

# class bike:

#     wheels=2
#     seat=1
#     indigator=4

#     def start(self):
#         print("starting")
    
#     def light(self):
#         print("night")

# splender=bike()
# honda=bike()
# print(splender.light())

# dir function.....
# print(dir(bike))
# bike.wheels=4
# print(splender.wheels, honda.wheels)

# a=14
# b=15
# print(type(a))


# class car():
#     tyre=4
#     headlight=2
#     staring=1
#     def start(self):
#         print('start the car')
#     def stop(self):
#         print('stop the car')
# a=car()    
# print(a.headlight ,a.staring)
# a.start()
# a.stop()

# constracter method.....
# class car:
#     def __init__(self):
#          print("object created")
# a=car()

# class car:
#     def __init__(self):
#         self.tyre=4
#         self.headlight=2
#     def start(self):
#         print("start the car") 
#     def print_tyre(self):
#         print(self.tyre)   
# a=car()
# print(a.tyre)
# print(a.headlight)
# a.start()
# a.print_tyre()
# b=car()
# b.tyre=50
# b.print_tyre()

# class car :
#     def __init__(self,wheels=4,colour="red"):
#         self.colour=colour
#         self.wheels=wheels
# a=car(wheels=50,colour="white")    
# print(a.colour)    


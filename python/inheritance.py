# class person:

#     def __init__(self, name="atul",age=19,mobnumber=987655442):
#         self.name=name
#         self.age=age
#         self.mobnumber=mobnumber

#     def show_details(self):
#         print(self.name,self.age,self.mobnumber)

# a=person(name="atul")
# a.show_details()
        
# class student (person):
#     pass

# print(dir(student))
# b=student()
# print(dir(b))b
# b.show_details()

# mulltiple_inheritance....

# class subject:
#     def __init__(self,sub_name="math",sub_teacher="yash",):

#         self.sub_name=sub_name
#         self.sub_teacher=sub_teacher

#     def sub_details(self):
#         print(self.sub_name,self.sub_teacher)
# a=subject()
# a.sub_details()
# print(dir(a))

# class student (person,subject):
#     pass
# b=student()     
# print(dir(b))
# print(b.sub_name,b.name)

# multilevel inheritance...
# class subject(person):

#     def __init__(self,sub_name="math",sub_teacher="yash",):

#         self.sub_name=sub_name
#         self.sub_teacher=sub_teacher

#     def sub_details(self):
#         print(self.sub_name,self.sub_teacher)

# class student(subject):
#     pass
# c=student()
# print(dir(c))

# super_method......

# class vehical:

#     def __init__(self,colour='red',brand='sujuki'):
#         self.colour=colour
#         self.brand=brand

# class car (vehical):

#     def wheels(self):
#         self.wheel=4
#         super().__init__(colour="white")  
# a=car()
# print(dir(a))
# a.wheels()
# print(a.wheel)
# print(a.colour)

# class vehical :

#     def __init__(self,colour='white',brand='honda'):
#         self.colour=colour
#         self.brand=brand

# class car (vehical):
    
#     def __init__(self,colour='red',brand='honda'):
#         self.brand=brand
#         self.colour=colour
#         super().__init__(colour) 

# class  bike(vehical):


#     def __init__(self, colour='black', brand='honda'):
#         super().__init__(colour, brand)    

# a=vehical()
# print(a.colour)    
# b=car(colour='pink')    
# print(b.colour)

# encapsulation.....

# class parents :

#     def __init__(self,propertie="400 hekaed",farmhouse=3):
#         self._propertie=propertie
#         self.__farmhouse=farmhouse

# class boy(parents):

#     def __init__(self, propertie="400 hekaed", farmhouse=3):
#         super().__init__(propertie, farmhouse)

# class girl(parents):

#     def __init__(self, propertie="400 hekaed", farmhouse=3):
#         super().__init__(propertie, farmhouse)

# a=boy()
# print(dir(a))
# print(a._propertie)
# print(a.__farmhouse)
# print(a._parents__farmhouse)


         


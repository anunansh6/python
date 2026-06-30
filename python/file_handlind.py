a=open('ifelse.py',"r")
print(a.readline    ())
print(a.read())
print(a.readlines())
print(a.readable())

with open('ifelse.py') as a: 
    print(a.errors)    
    print(a.read()) 

a=open('exam.py')
print(a.read())

with open("desktop\python\error_handling.py","a") as a :
    # print(a.read())
    print(a.write("hjdbhbbhb"))


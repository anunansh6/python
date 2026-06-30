# a='1,2,3,4,5,6,7,8,9,0'
# # frozenset[a]
# # print(type(a[1]))
# a=a.split(",")
# print(a)
# for x in range(len(a)):
#     a[x]=int(a[x])
# print(type(a[0]))

# a=10
# for x in range(a):print(x);print(x)

# list comprehension...
# print([int(x) for x in a.split(",")])


# print([x for x in range(1,101,2) ])

# print([x for x in range(100) if x%2==0])

# a=[ 1,3,5,8,9,11,15,18]
# for x in a : print("sum") if x%2==0 else print("visham")

# b = frozenset( "s" if x%2==0  else "v" for x in a)

# print(b)

# a=int(input("enter num 1:"))
# if a%3==0  and (a%5==0):
#     print("divded by both")
# elif a%3==0:
#     print("divded by 3")
# elif a%5==0:
#     print("diveded by 5")   
# else:
#     print("no divided")   

# a='abcdefhjk' 

# b=[11,12,13,14,15,16,17]
# print(a)
# c=[]
# for x in range(len(a)): c.append({a[x],   b[x]});print(c)
    
# d={}
# for x in range(len(a)): d  [a[x]]=b[x]
# print(d)

# print({ a[x]:b[x]     for  x in range(len(a))})

# # print([[a[x],b[x]] for x in range(len(a))])
# l=len(b)
# if len(a)<len(b):l=len(a)

# print([[ a[x],b[x]]   for x in range (l)] )


# zip function....
# print(list(zip(a,b)))


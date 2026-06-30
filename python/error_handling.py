try:
    a=int(input('1st--->'))
    b=int(input('2nd--->'))
    
except ValueError,ZeroDivisionError:
    print('plz type only number')
    exit(0)
def divide(a,b):
    try:
        return a/b
    except:
        raise TypeError(f"you are trying to divide {a} with 0 which not possible")
    finally:
        print("program end")
print(divide(a,b))

    hjdbhbbhb
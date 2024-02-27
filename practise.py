a = int(input('a: '))
x = int(input('x: '))
z = int(input('z: '))

if (a < 0 and x < 0 and z < 0):
    y = float((1+z)*(x/((a-1)/(1+x))))
    print("result: ", y)
else:
    print("error")

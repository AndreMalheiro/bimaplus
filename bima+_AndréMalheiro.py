import math


n = int(input ("input number of polygon edges"))

#if n < 3:
#    print("Type again")
#    n = int(input ("input number of polygon edges"))


while n < 3: 
    n = int(input("Invalid number of polygon edges.Type again!"))

i = 0
x = []
y = []


print(f"{'Point':>3} {'x':>10} {'y':>10}")

while i < n:
    i = i + 1
    x.append(int(input(f"point {i}: ")))
    y.append(int(input(f"point {i}: ")))  
     



j = 0

Area = 0 
Sx = 0
Sy = 0
Ix = 0
Iy = 0 
Ixy = 0


while j < (n - 1):

    Area = 1 / 2 * ( x [j + 1] + x[j] ) * (y [j + 1 ] - y[j] ) + Area
    Sx = - 1 /6 * (x [j + 1] - x [j] ) * (y [j + 1] ** 2 + y[j] * y[j+1]+ y[j] ** 2) + Sx
    Sy = 1 / 6 * (y [j + 1] - y [j] ) * (x [j + 1] ** 2 + x[j] * x[j+1]+ x[j] ** 2) + Sy 
    Ix = - 1 / 12 * (x[j+1] - x[j]) * (y [j+1] ** 3 + y [j+1] ** 2 * y[j] + y[j+1] * y[j] ** 2 + y [j] ** 3 ) + Ix
    Iy = 1 /12 * (y [j+1] - y[j] ) * ( x [j+1] ** 3 + x [j+1] ** 2 * x [j] + x [j+1] * x [j] ** 2 + x [j] ** 3) + Iy
    Ixy = - 1 / 24 * (y[j+1] - y[j]) * (y [j+1] * (3 * x [j+1] ** 2 + 2 * x [j+1] * x [j] + x[j] ** 2 ) + y[j] * (3 * x [j] ** 2 + 2 * x [j+1] * x [j] + x [j+1] ** 2)) + Ixy
 

    j += 1

Xt = Sy/Area

Yt = Sx/Area

Ixt = Ix - Yt ** 2 * Area

Iyt = Iy - Xt ** 2 * Area

Ixyt = Ixy + Xt * Yt * Area

    
#print(f"{x,y}")

print("Geometry Characteristics")
print("-" * 25)

print("Area:", f"{Area:>8.2f}")
print("Sx:", f"{Sx:>10.2f}" )
print("Sy:", f"{Sy:>10.2f}")
print("Ix:", f"{Ix:>10.2f}")
print("Iy:", f"{Iy:>10.2f}")
print("Ixy:", f"{Ixy:>9.2f}")
print("Xt:", f"{Xt:>10.2f}")
print("Yt:", f"{Yt:>10.2f}")
print("Ixt:", f"{Ixt:>9.2f}")
print("Iyt:", f"{Iyt:>9.2f}")
print("Ixyt:", f"{Ixyt:>8.2f}")

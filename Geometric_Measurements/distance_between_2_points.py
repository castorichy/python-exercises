import math
X1, Y1 = input("Enter the values of X1 and Y1 respectively: ").split()
X2, Y2 = input("Enter the values of X2 and Y2 respectively: ").split()
X1 = int(X1)
X2 = int(X2)
Y1 = int(Y1)
Y2 = int(Y2)
Distance = math.sqrt(((X2-X1)*(X2-X1))+((Y2-Y1)*(Y2-Y1)))
print(Distance)

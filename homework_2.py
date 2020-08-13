#Exo 1
------------------------------------------------
a = float(input("Nhap a : "))
b = float(input("Nhap b : "))
c = float(input("Nhap c : "))

print("Equation : {}x^2 + {}x + c = 0".format(a,b,c))

delta = b**b-4*a*c
x1=""
x2=""
print("Value of delta : ", delta )

if a == 0:
  x1 =-b/c
elif delta <0:
  x1 = complex((-b),abs(delta)**0.5)/(2*a)
  x2 = complex((-b),-abs(delta)**0.5)/(2*a)
  
elif delta == 0:
  x1 = x2 = -b/(2*a)
else:
  x1 = (-b+delta**0.5)/(2*a)
  x2 = (-b-delta**0.5)/(2*a)

print("Nghiệm phương trình {} AND {}".format(x1,x2))

------------------------------------------------------
#Exo 2


n = int(input("Nhap n : "))
x = float(input("Nhap x : "))

print("Sum Calculation 2.1")
s1 = 0
for n in range (n+1):
  s1 = s1 + x**n
print("Sum s1= ", s1)

print("Sum Calculation 2.2")
s2 = 0
for n in range (n+1):
  s2 = s2 + ((-1)**n)*x**n
print("Sum s2= ", s2)

#------------------------------------------------------
#Exo3

n = int(input("Nhap n bé hơn 1000 : "))
sum_n = 0

if n >= 1000:
  n = int(input("Nhap n bé hơn 1000 : "))
if n < 100:
  sum_n=sum_n + n%(10)+ n//(10)
else:
  sum_n=sum_n + n%(10)
  n = n // 10
  sum_n=sum_n + n%(10) + n//(10)
  
print("Tổng các chữ số là {}".format(sum_n))











  
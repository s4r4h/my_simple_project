import math

print("Selamat Datang! Ini adalah program untuk mengetahui jenis akar persamaan kuadrat dan nilai akar-akarnya (jika merupakan akar nyata)")
a= int(input("Masukkan nilai a: "))
b= int(input("Masukkan nilai b: "))
c= int(input("Masukkan nilai c: "))
p= input("Masukkan variabelnya: ")
print("Maka persamaannya adalah :",a,p,"^2","+",b,p,"+",c,"= 0")

D = (b*b) - (4*a*c)
print("Nilai dikriminan dari persamaan tersebut adalah D =", D)
if D > 0 :
    print("Maka dari itu, diperoleh kedua akarnya nyata dan berbeda")
    X1 =(-b+(math.sqrt(D)))/(2*a)
    X2 =(-b-(math.sqrt(D)))/(2*a)
    print("Nilai akar-akarnya yaitu :",p,"=",X1,"dan",p,"=",X2)
elif D == 0 :
    print("Maka dari itu, diperoleh kedua akarnya nyata dan kembar")
    X =(-b+(math.sqrt(D)))/(2*a)
    print("Nilai akarnya yaitu :",p,"=",p,"=",X)
elif D < 0 :
    print("Maka dari itu, diperoleh kedua akarnya imajiner atau tidak punya akar nyata")


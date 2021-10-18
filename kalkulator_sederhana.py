def operasi():
    print("A. Penjumlahan")
    print("B. Pengurangan")
    print("C. Perkalian")
    print("D. Perkalian")

print("Selamat Datang di Program Kalkulator Sederhana")
print("Berikut operasi yang tersedia dalam program ini :")

operasi()
a = input("Silahkan pilih operasi yang ingin dilakukan (A/B/C/D): ")
x = int(input("Masukkan bilangan pertama yang akan dioperasikan : "))
y = int(input("Masukkan bilangan kedua yang akan dioperasikan : "))
if (a == "A") :
    p = x + y
    print(x,"+",y,"=",p)
elif (a == "B") :
    q = x-y
    print(x,"-",y,"=",q)
elif (a == "C") :
    r = x*y
    print(x,"*",y,"=",r)
elif (a == "D") :
    s = x/y
    print(x,":",y,"=",s)
    
def lanjut():
    b = input("Ingin melanjutkan operasi? (ya/tidak) : ")
    if b == "tidak" :
        print("Operasi selesai, terimakasih telah menggunakan program ini")
    else :
        print("1. Ingin melanjutkan operasi sebelumnya, atau")
        print("2. Ingin memulai operasi baru")
        c = input("silahkan pilih 1 atau 2 : ")
        print("Pilihan operasi selanjutnya :")
        operasi()
        d = input("Silahkan pilih operasi selanjutnya (A/B/C/D): ")
        if c == "1" :
            e = int(input("Hasil sebelumnya : "))
            f = int(input("Akan dioperasikan dengan biangan berapa? "))
        else :
            e = int(input("Masukkan bilangan pertama yang akan dioperasikan : "))
            f = int(input("Masukkan bilangan kedua yang akan dioperasikan : "))
        if (d == "A") :
            p = e + f
            print(e,"+",f,"=",p)
        elif (d == "B") :
            q = e - f
            print(e,"-",f,"=",q)
        elif (d == "C") :
            r = e*f
            print(e,"*",f,"=",r)
        elif (d == "D") :
            s = e/f
            print(e,":",f,"=",s)

        return lanjut()
lanjut()

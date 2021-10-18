def selectionSort(L):
    i=len(L)-1
    while i>0:
        max=0
        j=1
        while j <= i:
            maxt=L[max]
            if maxt < L[j]:
                max=j
            j+=1
        L[max],L[i]=L[i],L[max]
        i-=1
print("Selamat Datang! Ini adalah program untuk mengurutkan bilangan.")
print("Masukkan barisan bilangan yang ingin diurutkan, pisahkan dengan koma")
print("(contoh: 8,4,2,7)")
L=list(map(int, input().split(",")))
print("Sebelum diurutkan : ", L)
selectionSort(L)
print("Setelah diurutkan : ", L)

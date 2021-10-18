print("DERET FIBONACCI")

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

n=int(input("Bilangan Fibonacci ke berapa yang ingin dicari? "))
print("Bilangan fibonacci ke-",n,"adalah",fibonacci (n))



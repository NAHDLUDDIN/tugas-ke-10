def fibonacci(n):
    if n<0:
        return 0
    else:
        if n < 2:
            return n 
        else:
            return fibonacci(n-1) + fibonacci(n-2)
x=int(input("masukkan angka deret: "))

for i in range (x+1):
    print("bilangan fibonacci ke: ",(i)," adalah = ",fibonacci(i))
    



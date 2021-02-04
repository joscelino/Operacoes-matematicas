n = int(input())

if n<10:
    print(n)
else:
    while n >= 10:
        print(n % 10, end='')
        n = n//10
        if n < 10:
            print(n)
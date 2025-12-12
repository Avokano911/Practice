# The Fibonacci Number Algorithm

Prev = 0
Prev2 = 1

Num = 30

for i in range(Num):
    Fibonacci = Prev + Prev2
    #print(Fibonacci)
    Prev = Prev2
    Prev2 = Fibonacci

# Implementation using recursion

prev1 = 0
prev2 = 1
count = 2

def FibonacciR(prev1, prev2):
    global count
    if count <= 29:
        NFibo = prev1 + prev2
        print(NFibo)
        prev1 = prev2
        prev2 = NFibo
        count += 1
        FibonacciR(prev1, prev2)
    else:
        return

FibonacciR(prev1,prev2)

# Implementation Using Recursion

def f(n):
    if n <= 1:
        return n
    else:
        return f(n - 1) + f(n - 2)

print("This is the exact fibo of : 30 ", f(30))



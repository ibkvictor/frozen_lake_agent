def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)

print(mult(6, 7))

def fact(a):
    if a == 1:
        return 1;
    else:
        return a * fact(a-1)

print(fact(4))

def print_position(_from,to):
    print ("i am going " ,_from, "to", to)

def tower_of_hanoi(n,a,b,c):
    if n == 1:
        return print_position (a,b)
        
    else:
        return (tower_of_hanoi(n-1,a,c,b), tower_of_hanoi(1,a,b,c),tower_of_hanoi(n-1,c,b,a))

tower_of_hanoi(4,"a","b","c")

def fib(n):
    if n==0 or n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print (fib(8))
    
#  here i used a dictionary to store calculation and prevent repetition thus producing more efficient code
# del add
def fib(n ,d):
    if n in d:
        return d[n]
    else:
        return fib(n-1, d) + fib(n-2, d)


d = {1:1,2:2}
print(fib(6, d))

s = "mane"
print (s[0:4])

def palindrome(s):
    b = len(s)
    if b == 0 or b == 1:
        return True
    elif s[0] == s[b-1]:
        return palindrome(s[1:-1])
    else:
        return False

print (palindrome("rotor"))




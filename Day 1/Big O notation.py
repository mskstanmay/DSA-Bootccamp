
# O(n) complexity
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# O(n^2) complexity
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10)


# O(a+b) complexity
def print_items(a,b):
    for i in range(a):
        print(i)
    for i in range(b):
        print(i)
    

print_items(2,5)

# O(a*b) complexity
def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)

print_items(2,5)
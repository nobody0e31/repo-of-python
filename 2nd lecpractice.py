

def is_prime(n):
    if n < 2:
        return False
    
    i = 2
   
    
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

user_input = int(input("Enter the number: "))
result = is_prime(user_input)
print(result)
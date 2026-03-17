a = int(input("Enter start (a): "))
b = int(input("Enter end (b): "))

i = a  # Start from 'a' as requested 
while i <= b:
    if i % 2 == 0:
        print(i)
    i += 1  # Increment every time to avoid an infinite loop
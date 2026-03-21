fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = ["djwale" for fruit in fruits if "a" in fruit]

print(new_list) 
# Output: ['djwale', 'djwale', 'djwale']


############    #####           ###3##*****************








fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [fruit for fruit in fruits if "a" in fruit]

print(new_list) 
# Output: ['apple', 'banana', 'mango']






##                *******************.                       ***************




fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [1 for fruit in fruits if "a" in fruit]

print(new_list) 
# Output: [1, 1, 1]
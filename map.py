def square(x):
    return x * x
numbers = [1,2,3,4,5]
squares = map(square, numbers)
print(list(squares))

fruits = ["apple", "banana", "cherry"]
wordLengths = list(map(len, fruits))
print(wordLengths)

def ConvertToUpper(n):
    return n.upper()
names = ["alice", "bob", "carol", "dave", "eve"]
print(list(map(ConvertToUpper, names)))

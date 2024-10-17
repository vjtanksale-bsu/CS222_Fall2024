fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.remove("banana")
print(fruits)
print(len(fruits))
miscellaneous = {"alice", 50, True, "bob", 100}
print(miscellaneous)
print(len(miscellaneous))
for m in miscellaneous:
    print(m)
section1 = {100, 80, 90}
section2 = {70, 90}
print(section1.union(section2))
def main():
    midterm = {
        "Alice": 90, 
        "Bob" : 93, 
        "Carol" : 70, 
        "Dave" : 100, 
        "Eve" : 97
        }
    print(midterm["Alice"])
    print(midterm.values())
    for v in midterm.values():
        print(v)
    print(len(midterm))
    exams = {
        "Alice" : [100, 75, 80],
        "Bob" : [50, 50, 70]
    }
    print(exams["Bob"][2])
main()

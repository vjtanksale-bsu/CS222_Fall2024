def main():
    midterm = [90, 80, 100, 75, 82, 80]
    print(midterm[1])
    for m in midterm:
        print(m)
    print(len(midterm))
    print(max(midterm))
    midterm.append(93)
    midterm.insert(2, 70)
    print(midterm)
    midterm.remove(80)
    print(midterm)
main()
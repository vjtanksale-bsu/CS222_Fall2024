def main():
    try:
        studentList = open("students.txt", 'r')
        students = studentList.readlines()
        studentList.close()
        #print(students)
        fileOutput = open("output.txt", 'a')
        for s in students:
            #print(s)
            parts = s.split(',')
            #print(parts[0])
            if parts[2] == "Math":
                print(s)
            fileOutput.write(parts[1] + "'s GPA is " + parts[3] + "\n")
        fileOutput.close()
    except FileNotFoundError:
        print("File not found")
main()
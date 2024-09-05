def main():
    try:
        studentList = {}
        fileInput = open("studentsInfo.txt", 'r')
        students = fileInput.readlines()
        fileInput.close()
        for s in students:
            parts = s.split(',')
            studentList[parts[0]] = [parts[1], parts[2], parts[3], parts[4]]
        print(studentList)
    except FileNotFoundError:
        print("File not found")
main()
import operator


def readStudentsDetails():
    noOfStds = int(input("Enter the number of students  "))
    stdRecord = {}
    for student in range(0, noOfStds):
        name = input("Enter the name of the student: ")
        marks = input("Enter the marks of the student: ")
        print()
        stdRecord[name] = marks
    return stdRecord


def rankStudents(stdRecord):
    try:
        sortedstdRecord = sorted(
            stdRecord.items(), key=operator.itemgetter(1), reverse=True)
        print()
        print(sortedstdRecord)
        print()
        print("{} has secured first rank with {} marks".format(
            sortedstdRecord[0][0], sortedstdRecord[0][1]))
        print("{} has secured second rank with {} marks".format(
            sortedstdRecord[1][0], sortedstdRecord[1][1]))
        print("{} has secured third rank with {} marks".format(
            sortedstdRecord[2][0], sortedstdRecord[2][1]))
        print()
        return sortedstdRecord
    except IndexError:
        print("Enter a min of 1 student")
        quit()


def rewardSudents(sortedstdRecord, reward):
    print()
    print("{} has received a cash reward of ${}".format(
        sortedstdRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(
        sortedstdRecord[1][0], reward[1]))
    print("{} has received a cash reward of ${}".format(
        sortedstdRecord[2][0], reward[2]))
    print()


def appreciateStudents(sortedstdRecord):
    print()
    for record in sortedstdRecord:
        if int(record[1]) >= 950:
            print("Congrats on scoring {} marks,{}".format(
                record[1], record[0]))
        else:
            break


stdRecord = readStudentsDetails()
sortedstdRecord = rankStudents(stdRecord)
# print(rankStudents())
reward = (500, 300, 100)
# sortedstdRecord = sortedstdRecord
rewardSudents(sortedstdRecord, reward)
appreciateStudents(sortedstdRecord)

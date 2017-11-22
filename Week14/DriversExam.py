# Chapter 7 Programming Exercises 7 - Driver's License Exam
# Author: Steve Schroeder
# Week 14
#
STUDENT_FILE = "student_file.txt"
PASS_FAIL_THRESHOLD = 15


def main():
    try:
        student_answers = program_input()
        correct, grade, wrong, incorrect_answers, total = program_processing(student_answers)
        program_output(correct, grade, wrong, incorrect_answers, total)
    except IOError:
        print("There was a problem writing/reading to/from the file.")
    except IndexError:
        print("There was an issue with the index")
    except:
        print("There was an undefined error. Program ending")


def program_input():
    student_file = open(STUDENT_FILE, "w")
    for question in range(20):
        student_answer = input("Exam Question " + str(question + 1) + ": ")
        student_file.write(student_answer.upper() + "\n")
    student_file.close()
    student_answers = read_answers()
    return student_answers


def answer_data():
    answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
    return answers


def read_answers():
    answers = open(STUDENT_FILE, "r")
    student_answers = answers.readlines()
    answers.close()
    return student_answers


def program_processing(student_answers):
    correct = 0
    wrong = 0
    incorrect_answers = []
    answers = answer_data()
    total = len(answers)

    for student_answer in range(20):
        if student_answers[student_answer].rstrip() == answers[student_answer].upper():
            correct = correct + 1
        else:
            wrong = wrong + 1
            incorrect_answers.append(student_answer + 1)
    if correct / total >= PASS_FAIL_THRESHOLD / total:
        grade = "Pass"
    else:
        grade = "Fail"
    return correct, grade, wrong, incorrect_answers, total


def program_output(correct, grade, wrong, incorrect_answers, total):
    print("You got " + str(correct) + " answers correct out of " + str(total) + ".")
    print("You " + grade + "!")
    print("You got " + str(wrong) + " questions incorrect.")
    print("These were your incorrectly answered questions: " + str(incorrect_answers))


main()
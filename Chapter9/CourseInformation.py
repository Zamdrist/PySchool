# Chapter 9 Programming Exercises 1 - Course Information
# Author: Steve Schroeder
# Return the course room, instructor and time for a user selected course
#


def main():
    try:
        courses, course_room, course_instructor, course_time = course_information()
        selected_course = program_input(courses)
        course_details = program_processing(selected_course, course_room, course_instructor, course_time)
        program_output(course_details)
    except KeyError:
        print("There was a problem with the selection. Program ending")


def program_input(courses):
    course_list = ""
    for course in courses:
        course_list += course + ", "

    selected_course = input("Choose a course from the following list " + course_list.rstrip(", ") + ": ")

    if selected_course.upper() not in courses:
        print("That was not one of the courses to choose from.")
        exit()

    return selected_course.upper()


def course_information():
    courses = ("CS101", "CS102", "CS103", "NT110", "CM241")
    course_room = {"CS101": "3004", "CS102": "4501", "CS103": "6755", "NT110": "1244", "CM241": "1411"}
    course_instructor = {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich", "NT110": "Burke", "CM241": "Lee"}
    course_time = {"CS101": "8:00 a.m.", "CS102": "9:00 a.m.", "CS103": "10:00 a.m.", "NT110": "11:00 a.m.",
                   "CM241": "1:00 p.m."}
    return courses, course_room, course_instructor, course_time


def program_processing(selected_course, course_room, course_instructor, course_time):
    room = course_room[selected_course]
    instructor = course_instructor[selected_course]
    time = course_time[selected_course]
    course_details = "Course " + \
                     selected_course + \
                     " meets in room " + \
                     room + \
                     ", is taught by " + \
                     instructor + \
                     ", and begins at " + time
    return course_details


def program_output(course_details):
    print(course_details)


main()
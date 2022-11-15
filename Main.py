# Tester Class and Main Method
# Course: CS 4308

# Name: Andy Martinez Reyes
# Professor: Dr. Garrido
# Assignment #: Three

import Course

#Purpose of this program is to allow users to create, save, and edit Course obejcts that are saved into an array
#This is the Main method that will have all the interactions with the user


# methods for the menu Operations ###
#The Course number is used to select courses for the deletions and edits menu options
#method to delete specified course
def deletions(NcourseArray, limit, isFound): #Course Array does not have to be passed with a few changes
    #If there is no courses in array, user will be notified
    if(limit == 0 ):
        print("There is no Courses available to delete")
    else:
        print("Enter Course number to delete")
        print("select: ", end = " ")
        selectionD = input()

        for i in range(0,limit): 
            if(NcourseArray[i].get_CourseNumber() == selectionD):
                NcourseArray.pop(i)
                print("all done! That course has been removed!")
                isFound = 1
                break #breaks out of loop
        if(isFound == 0): #in case nothing was found or deleted
            print("no matching course number was found")
        
#method to add courses
def additions():
    print("Adding another course, PLease input the following information")
    ExtracourseName = input("Enter Course Name: ")
    ExtracourseNum = input("Enter Course Number: ")
    ExtracourseSection =  input("Enter Course Section: ")
    ExtraTermandYear =  input("Enter Course Term and year: ")
    ExtraNumofStudents =  input("Enter Number of students in this course: ")

    TempObject = Course.Course(ExtracourseName, ExtracourseNum, ExtracourseSection, ExtraTermandYear, ExtraNumofStudents)
    courseArray.append(TempObject)


#Method to edit specified course
def edits(limit, isFound):
    if(limit == 0 ):
        print("There is no Courses available. Please Add a course to edit")
    else:
        print("Enter Course number to edit")
        print("select: ", end = " ")
        selectionD = input()
        
        for i in range(0,limit): 
            if(courseArray[i].get_CourseNumber() == selectionD):
                print("Course has been found! What would you like to edit?")
                print("Course Edit Menu")
                print("'A') Name")
                print("'B') Number")
                print("'C') Section")
                print("'D') Term and year")
                print("'E') Number of students")
                print("'F') All values")
                print("'G') exit") #user can exit incase they change their mind
                print("") #for easier 

                editSelection = input()
                match editSelection:
                    case 'A':
                        print("Enter New Name")
                        NewcourseName = input(": ")
                        courseArray[i].set_CourseName(NewcourseName)
                        isFound = 1,
                    case 'B':
                        print("Enter New Number")
                        NewcourseNum = input(": ")
                        courseArray[i].set_CourseNumber(NewcourseNum)
                        isFound = 1,
                    case 'C':
                        print("Enter New Section")
                        NewcourseSection = input(": ")
                        courseArray[i].set_CourseSections(NewcourseSection)
                        isFound = 1,
                    case 'D':
                        print("Enter New Term and year")
                        NewTermandYear = input(": ")
                        courseArray[i].set_termAndYear(NewTermandYear)
                        isFound = 1,
                    
                    case 'E':
                        print("Enter New Number of students")
                        NewNumofStudents =  input(": ")
                        isFound = 1,
                        courseArray[i].set_numberOfStudents(NewNumofStudents),
                    case 'F':
                        print("Enter all new information")
                        NewcourseName = input("Enter Course Name: ")
                        NewcourseNum = input("Enter Course Number: ")
                        NewcourseSection =  input("Enter Course Section: ")
                        NewTermandYear =  input("Enter Course Term and year: ")
                        NewNumofStudents =  input("Enter Number of students in this course: ")
                        courseArray[i].inputAllCourse(NewcourseName,NewcourseNum ,NewcourseSection ,NewTermandYear,NewNumofStudents )
                        isFound = 1,
                    case 'G':
                        print("Thank you! Goodbye!")
                        isFound = 1
                break
        
        if(isFound == 0): #in case nothing was found 
            print("no matching course number was found")
###





#array that will hold course objects
courseArray = []

# This is an initial start to the program before the user can edit the courses.
print("Welcome! Please input the following information to get started")

# asks for input from the use
# layout can be changed
courseName = input("Enter Course Name: ")
courseNum = input("Enter Course Number: ")
courseSection =  input("Enter Course Section: ")
TermandYear =  input("Enter Course Term and year: ")
NumofStudents =  input("Enter Number of students in this course: ")

InitialCourse = Course.Course(courseName, courseNum, courseSection, TermandYear, NumofStudents)

courseArray.append(InitialCourse)
try:
    #menu for user selection
    MenuStatus = 1 #Used to get user input for menu selection 
    while MenuStatus != 4:
        print("Courses Menu")
        print("0) Display All Courses")
        print("1) Add Course")
        print("2) Remove Course")
        print("3) edit Course values")
        print("4) Exit")
        print("") #for easier 

        
        print("select: ", end = " ")
        MenuStatus = int(input())
        limit = len(courseArray)
        int(limit)      

    

    
        #switch statements for menu options
        match MenuStatus:
            case 0:
                #Check to see if there is no courses to display
                if(limit == 0 ):
                    print("There is no Courses available to display")
                else:
                    for i in range(0,limit): 
                        print("")
                        print("||") #used to divide courses for better readability
                        print("")
                        courseArray[i].displayAll()
                    print(" "),
            
            case 1:
                additions() ,

            case 2:
                deletions(courseArray, limit, 0),
            case 3:
                edits(limit, 0),
            case 4:
                print("Thank you! Goodbye!")


except:
    print("an error has occurred. Make sure to input the appropriate data types when doing any menu selections.")

            


    
    



#references 
#https://pythongeeks.org/methods-in-python/
#https://www.w3schools.com/python/gloss_python_array_remove.asp
#https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/
#https://www.youtube.com/watch?v=q4pnb5aDXXQ
#https://www.w3schools.com/python/python_try_except.asp



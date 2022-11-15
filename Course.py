


class Course:
    # Referenced https://www.geeksforgeeks.org/getter-and-setter-in-python/
    
  


    #allows to add entire information 
    def inputAllCourse(self, NCourseNames,NCourseNumbers,NCourseSections2, NTermYear ,ENumberOfStudents):
        self.set_CourseName(NCourseNames)
        self.set_CourseNumber(NCourseNumbers)
        self.set_CourseSections(NCourseSections2)
        self.set_termAndYear(NTermYear)
        self.set_numberOfStudents(ENumberOfStudents)


    #Constructor
    def __init__(self, CourseName,CourseNumber,CourseSections, termAndYear, numberOfStudents):
        self._CourseName = CourseName
        self._CourseNumber = CourseNumber
        self._CourseSections = CourseSections
        self._termAndYear = termAndYear
        self._numberOfStudents = numberOfStudents
    
    #Accessor and Mutator methods for each variable
    def get_CourseName(self):
        return self._CourseName
    def set_CourseName(self, NCourseName):
        self._CourseName = NCourseName

    
     
    def get_CourseNumber(self):
        return self._CourseNumber
    def set_CourseNumber(self, NCourseNumber):
        self._CourseNumber = NCourseNumber


    def get_CourseSections(self):
        return self._CourseSections
    def set_CourseSections(self, NCourseSections):
        self._CourseSections = NCourseSections

    def get_termAndYear(self):
        return self._termAndYear
    def set_termAndYear(self, NtermAndYear):
        self._termAndYear = NtermAndYear

    def get_numberOfStudents(self):
        return self._numberOfStudents
    def set_numberOfStudents(self, NnumberOfStudents):
        self._numberOfStudents = NnumberOfStudents
    #Displays all values in ordered thats easy to understand
    def displayAll(self):
        print("Course Number: " + self.get_CourseNumber() + ": ")
        print("Course Name: " + self.get_CourseName())
        print("Course Section: " + self.get_CourseSections())
        print("Course Term and Year: " + self.get_termAndYear())
        print("Number of Students: " + self.get_numberOfStudents())

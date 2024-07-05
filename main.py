import json
from Packages import emailcheck,markscheck,phonecheck
class Student:
    def __init__(self)->None:
        """Constructor of the class Student
        """
        self._s_name = " "
        self._s_roll_no = " "
        self._s_email = " "
        self._s_phone_no = 0000000000
        self._marks_maths = 0.0
        self._marks_science = 0.0
        self._marks_computer = 0.0
        self._marks_nepali = 0.0
        self._marks_english = 0.0
        self._s_address = " "
        self._s_percentage = 0.0
        self._s_rank = 0 
        self._s_status = " "
    def student_accept_Data(self)->None:
        """Takes student data from the user
        """
        while True:
            print("Enter the Student info:\n")
            self._s_name = input("Name: ")
            self._s_roll_no = input("Roll No: ")
            while True:
                self._s_email = input("Email: [Domain names:Gmail, Yahoo, Hotmail, Khwopa]: ")
                if emailcheck.email_check(self._s_email):
                    break
                else:
                    continue
            while True:
                self._s_phone_no = input("Phone no:")
                if phonecheck.check_phone(self._s_phone_no):
                    break
                else:
                    continue
            self._s_address = input("Student Address:")
            print("Enter student marks:")
            while True:
                self._marks_maths = float(input("Maths: "))
                if markscheck.marks_check(self._marks_maths):
                    break
                else:
                    continue
            while True:
                self._marks_science = float(input("Science: "))
                if markscheck.marks_check(self._marks_science):
                    break
                else:
                    continue
            while True:
                self._marks_computer = float(input("Computer: "))
                if markscheck.marks_check(self._marks_computer):
                    break
                else:
                    continue
            while True:
                self._marks_nepali = float(input("Nepali: "))
                if markscheck.marks_check(self._marks_nepali):
                    break
                else:
                    continue
            while True:
                self._marks_english = float(input("English: "))
                if markscheck.marks_check(self._marks_english):
                    break
                else:
                    continue
            self.pass_fail_determination()
            self.percentage()
            self.studet_write_Data()
            y = input("Do you want to enter more info?(Y/N)")
            z = y.upper()
            if z == "N":
                break
    def studet_write_Data(self)->None:
        """Writes the student data into the file : data_student.json
        """
        student = []
        student_data = {
            "Student Name" :self._s_name,
            "Student Roll No" : self._s_roll_no,
            "Student Email" : self._s_email,
            "Student Phone" : self._s_phone_no,
            "Student Address" : self._s_address,
            "Maths" : self._marks_maths,
            "Science" : self._marks_science,
            "Computer" : self._marks_computer,
            "Nepali" : self._marks_nepali,
            "English" : self._marks_english,
            "Status": self._s_status,
            "Percentage" :self._s_percentage,
        }
        with open("data_student.json","r") as file:
            student = json.load(file)
        student.append(student_data)
        with open("data_student.json","w") as file:
            json.dump(student,file,indent = 4)
    def pass_fail_determination(self)->None:
        """
        Checks if the marks is in each subject is passing marks or not
        """
        if self._marks_maths >= 32 and self._marks_science >= 32 and self._marks_computer >= 32 and self._marks_nepali >= 32 and self._marks_english >= 32:
            self._s_status = "PASS"
        else:
            self._s_status = "FAIL"
    def percentage(self)->None:
        """Calculates the percentage obtained by the student
        """
        percentage = 0.00
        percentage = (self._marks_maths + self._marks_science + self._marks_computer + self._marks_english + self._marks_nepali) / 5
        self._s_percentage = percentage
    def highest_and_lowest_scores(self)->None:
        """Reads marks of each student in each subject and displays highest and lowest in each subject
        """
        maths_max = 0.0
        science_max = 0.0
        computer_max = 0.0
        nepali_max = 0.0
        english_max = 0.0
        maths_min = 100.0
        science_min = 100.0
        computer_min = 100.0
        nepali_min = 100.0
        english_min = 100.0
        student_marks = []
        with open("data_student.json","r") as file:
            student_marks = json.load(file)
            for dictionary in student_marks:
                if dictionary["Maths"] > maths_max:
                    maths_max = dictionary["Maths"]
                if dictionary["Maths"] < maths_min:
                    maths_min = dictionary["Maths"]
                if dictionary["Science"] > science_max:
                    science_max = dictionary["Science"]
                if dictionary["Science"] < science_min:
                    science_min = dictionary["Science"]
                if dictionary["Computer"] > computer_max:
                    computer_max = dictionary["Computer"]
                if dictionary["Computer"] < computer_min:
                    computer_min = dictionary["Computer"]
                if dictionary["Nepali"] > nepali_max:
                    nepali_max = dictionary["Nepali"]
                if dictionary["Nepali"] < nepali_min:
                    nepali_min = dictionary["Nepali"]
                if dictionary["English"] > english_max:
                    english_max = dictionary["English"]
                if dictionary["English"] < english_min:
                    english_min = dictionary["English"]
            print("-----------------")
            print("Highest Marks:")
            print("-----------------")
            print("Maths:", maths_max)
            print("Science:",science_max)
            print("Computer:",computer_max)
            print("Nepali:",nepali_max)
            print("English:",english_max)
            print("-----------------")
            print("Lowest Marks:")
            print("-----------------")
            print("Maths:", maths_min)
            print("Science:",science_min)
            print("Computer:",computer_min)
            print("Nepali:",nepali_min)
            print("English:",english_min)
    def rank(self,student_roll:str)->None:
        """
        Displays the rank of the student 

        Args:
            student_roll (str): takes the roll no of the student
        """
        rank_order = []
        student_rank = []
        with open("data_student.json","r") as file:
            student_rank = json.load(file)
            for dictionary in student_rank:
                    rank_order.append(dictionary["Percentage"])
            sorted_list = sorted(rank_order, reverse=True)
        with open("data_student.json","r") as file:
            student_rank = json.load(file)
            for dictionary in student_rank:
                    if  dictionary["Student Roll No"]==student_roll:
                         percentage = (dictionary["Maths"] + dictionary["Science"] + dictionary["Computer"] + dictionary["Nepali"] + dictionary["English"]) / 5
                         for index,i in enumerate(sorted_list):
                                if percentage == i:
                                    self._s_rank = index + 1
        print("Rank : ",self._s_rank)
    def display_s_data(self,student_roll:str)->None:
        """
        Displays student data on the basis of entered Roll No

        Args:
            student_roll (str): Student roll_no entered from the user
        """
        print("Student data:")
        print("---------------")
        with open("data_student.json","r") as file:
            student = json.load(file)
            for dictionary in student:
                if  dictionary["Student Roll No"] == student_roll:
                    for x in dictionary.items():
                        key, value = x
                        print(f"{key} : {value}")

class Teacher(Student):
    def __init__(self)->None:
        """Constructor for the class Teacher
        """
        self._t_name = " "
        self._t_id = " "
        self._t_email = " "
        self._t_subject = " "
        self._t_phone = " "
        self._t_address = " "
        super().__init__()
    def teacher_accept_Data(self)->None:
        """Takes Teacher data from the user
        """
        while True:    
            print("Enter the Teacher info:\n")
            self._t_name = input("Name: ")
            self._t_id = input("ID: ")
            while True:
                self._t_email = input("Email:[Domain names:Gmail, Yahoo, Hotmail, Khwopa]:")
                if emailcheck.email_check(self._t_email):
                    break
                else:
                    continue
            while True:
                self._t_phone = input("Phone no:")
                if phonecheck.check_phone(self._t_phone):
                    break
                else:
                    continue
            self._t_subject = input("Subject: ")
            self._t_address = input("Address:")
            self.teacher_write_Data()
            y = input("Do you want to enter more data?(Y/N)")
            z = y.upper()
            if z == "N":
              break
    def teacher_authenticate(self)->None:
        """Checks if the user is registered Teacher or not by matching entered ID with Teacher ID 
        """
        teacher = []
        with open("data_teacher.json","r") as file:
            teacher = json.load(file)
            if len(teacher) != 0:
                teacher_id = input("Enter Teacher ID for Verification: ")
                for dictionary in teacher:
                    if dictionary["Teacher ID"] == teacher_id:
                        self.teacher_accept_Data()
            else:
                    self.teacher_accept_Data()
    def teacher_write_Data(self)->None:
        """Writes teacher data in data_teacher.json
        """
        teacher = []
        teacher_data = {
            "Teacher Name" :self._t_name,
            "Teacher ID" : self._t_id,
            "Teacher Subject" : self._t_subject,
            "Teacher Email" : self._t_email,
            "Teacher Phone" : self._t_phone,
            "Teacher Address" : self._t_address,
        }
        with open("data_teacher.json","r") as file:
            teacher = json.load(file)
        teacher.append(teacher_data)
        with open("data_teacher.json","w") as file:
            json.dump(teacher,file,indent = 4)
    def display_t_data(self)->None:
        """Displays data of teacher on the basis of Teacher ID
        """
        teacher_id = input("Enter the ID of the Teacher whose Data is to be displayed:")
        with open("data_teacher.json","r") as file:
            teacher = json.load(file)
            for dictionary in teacher:
                if dictionary["Teacher ID"] == teacher_id:
                    for x in dictionary.items():
                        key, value = x
                        if key == "Teacher Name" or key == "Teacher Email" or key == "Teacher Phone":
                            print(f"{key} : {value}")
    def access_to_student_input(self)->None:
        """A subroutine that provides access to enter student data after Teacher ID verification
        """
        teacher_id = input("Enter your Teacher ID for verification:")
        with open("data_teacher.json","r") as file:
            teacher = json.load(file)
            for dictionary in teacher:
                if dictionary["Teacher ID"] == teacher_id:
                    super().student_accept_Data()
    def access_to_student_display(self)->None:
        """A subroutine that provides access to Display Student Data on the basis of Entered Roll no
        """
        student_roll = input("Enter student Roll No: ")
        super().display_s_data(student_roll)
        super().rank(student_roll)
    def marks(self)->None:
        """A subroutine that provides access to highest and lowest scores
        """
        super().highest_and_lowest_scores()
        
# Main program starts here

t_obj = Teacher()
choice = int(input("Are you a Teahcer or Student?\nIf Teacher : Enter 1\nIf Student : Enter 2\n"))
if choice == 1:
    fir_choice = int(input("Teacher operations :\n1.Display Teacher Records\n2.Add New Teacher Records\n3.Display Student Records\n4.Add New Student Records\n")) 
    if fir_choice == 1 :
        t_obj.display_t_data()
    elif fir_choice == 2:
        t_obj.teacher_authenticate()
    elif fir_choice == 3 :
        t_obj.access_to_student_display()
    elif fir_choice == 4:
        t_obj.access_to_student_input()
elif choice == 2:
    sec_choice = int(input("Student Operations:\n1.View Records(Marks,Percentage and Rank)\n2.View highest and Lowest Marks in each subject\n"))
    if sec_choice == 1 :
        t_obj.access_to_student_display()
    elif sec_choice == 2:
        t_obj.marks()
    else:
        print("Invalid")
else:
    print("Invalid")


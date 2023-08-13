class Student:
    def __init__(self, name, student_id, age, gender):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.gender = gender
        
    def set_grade(self, grade):
        self.grade = grade
        
    def get_grade(self):
        print(self.grade)
        
    def display_student_info(self):
        try:
            print(
            f"""
                學生姓名 : {self.name} 
                學生學號 : {self.student_id} 
                學生年齡 : {self.age} 
                學生性別 : {self.gender} 
                學生成績 : {self.grade}"""
            )
        except AttributeError:
            self.grade = "無資料"
            print(
            f"""
                學生姓名 : {self.name} 
                學生學號 : {self.student_id} 
                學生年齡 : {self.age} 
                學生性別 : {self.gender} 
                學生成績 : {self.grade}"""
            )
class patients:
    def __init__(self, name, age, admission_date, history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.history = history
    
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Admission: {self.admission_date}, History: {self.history}")

# 示例调用
patient1 = patients("John Doe", 30, "2023-01-01", "No allergies")
patient1.print_details()
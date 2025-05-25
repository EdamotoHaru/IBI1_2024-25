class patients:
    def __init__(self, name, age, admission_date, history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.history = history
    
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Admission: {self.admission_date}, History: {self.history}")

# example usage
patient1 = patients("John Doe", 30, "2023-01-01", "No allergies")
patient2 = patients("Jane Smith", 25, "2023-02-01", "Allergic to penicillin")
patient3 = patients("Alice Johnson", 40, "2023-03-01", "Diabetic")
patient1.print_details()
patient2.print_details()
patient3.print_details()
# The above code defines a class named 'patients' that represents a patient with attributes such as name, age, admission date, and medical history.
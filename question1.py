from abc import ABC, abstractmethod

class Person(ABC):
  @abstractmethod
  def print_details():
    pass

class Doctor(Person):
  def __init__(self, name, age, specialization):
    self.name = name
    self.age = age
    self.specialization = specialization
  
  def print_details(self):
    print(f"Name: {self.name}, Age: {self.age}, Specialization: {self.specialization}")

class Patient(Person):
  def __init__(self, name, age, diagnosis):
    self.name = name
    self.age = age
    self.diagnosis = diagnosis
  
  def print_details(self):
    print(f"Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}")

class Nurse(Person):
  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department
  
  def print_details(self):
    print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")

if __name__ == '__main__':
  object_list = [
    Doctor("John Doe", 45, "Pulmonology"),
    Patient("Jane Smith", 28, "Bronchitis"),
    Nurse("Mary Jones", 38, "Pediatrics"),
  ]

  for obj in object_list:
    obj.print_details()
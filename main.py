#Class Introduction 
#Class : A class is a blueprint or template used to create objects. It defines what data (attributes) and what actions (methods) the objects will have.
#Objects : An object is an instance of a class — a real entity created using the class.
class students:
    class_yr = 2025 #its a class variable same for all objects instantied for this particular class.
    student_count = 0; #class variable.
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_count += 1;

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    
student1 = students("A",18,'A')
print(f"I am {student1.name} and my age is {student1.age} I got an {student1.grade} in {students.class_yr} , student count this year is {student1.student_count}.")
student2 = students("Z",21,'A')
print(f"I am {student2.name} and my age is {student2.age} I got an {student2.grade} in {students.class_yr} , student count this year is {student2.student_count}.")



# class vehicle:
#     def __init__(self,name,fuel_type,engine_type,cost):
#         self.name = name
#         self.fuel_type = fuel_type
#         self.engine_type = engine_type
#         self.cost = cost
#     def start(self):
#         print(f"{self.name} is starting.")
#     def stop(self):
#         print(f"{self.name} is stoping.")
# class petrolcar(vehicle):
#     pass

# c1 = petrolcar("Mycar","petrol","petroldrinkingengine",25000)
# print(c1.stop())

# NOTE FOR ABOVE CODE : If you do self.class_variable then each object has its own version (copy) of this class variable changes in this copy of a class varible wont affect the original class variable as its class dependent not object dependent but also remember you do class_variable += 1 in constructor as constructor runs when an object is instantied so you can use this to count total no. of objects made for that class.


        
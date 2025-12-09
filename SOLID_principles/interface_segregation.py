class Workable:
    def work(self):
        pass

class Manageable:
    def manage(self):
        pass

class Employee(Workable):
    def work(self):
        print("Employee working")

class Manager(Workable, Manageable):
    def work(self):
        print("Manager working")

    def manage(self):
        print("Manager managing")



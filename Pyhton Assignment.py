#Pyhton code
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

def search_by_age(employees, target_age):
    matching_employees = [emp for emp in employees if emp.age == target_age]
    return matching_employees

def search_by_name(employees, target_name):
    matching_employees = [emp for emp in employees if emp.name.lower() == target_name.lower()]
    return matching_employees

def search_by_salary(employees, operator, target_salary):
    operators = {
        ">": lambda x, y: x > y,
        "<": lambda x, y: x < y,
        ">=": lambda x, y: x >= y,
        "<=": lambda x, y: x <= y,
    }

    matching_employees = [emp for emp in employees if operators[operator](emp.salary, target_salary)]
    return matching_employees

def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Employee Table:")
    for emp in employees:
        print(emp)

    print("\nSearch Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (> < <= >=)")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        target_age = int(input("Enter the age to search for: "))
        result = search_by_age(employees, target_age)
    elif choice == 2:
        target_name = input("Enter the name to search for: ")
        result = search_by_name(employees, target_name)
    elif choice == 3:
        operator = input("Enter the operator (> < <= >=): ")
        target_salary = float(input("Enter the target salary: "))
        result = search_by_salary(employees, operator, target_salary)
    else:
        print("Invalid choice!")
        return

    if result:
        print("\nSearch Results:")
        for emp in result:
            print(emp)
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()

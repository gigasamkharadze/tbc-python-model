# Python Employee Model

## Description
This is a simple employee model that can be used to store employee information.
Each employee has the following attributes:
- Id
- Name
- SurName
- Age

Using this model, you can create, read, update and delete employees.
When querying the employee model, you can filter the results by any of the attributes
or by the combination of them.
You also can get a single employee by id, or get all employees without any filter.

## How to use

1. Clone the repository
2. Open the terminal and navigate to the repository folder

First, You need to run `db.py` to create the database and the table.
```bash
python db.py
```

Then, you can run `main.py` to interact with the employee model.
```bash
python main.py
```

If you want to change the Employee model, you can do it in `employee.py` file.


# Employee Model
```python
class Employee:
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age
```

# Employee Model Usage Examples
```python
# Create a new employee
employee = Employee('John', 'Doe', 25)
employee.save()

# Get all employees
employees = Employee.all()

# Get a single employee by id and update it
employee = Employee.get(1) 
employee.name = 'Jane'
employee.update()

# get all employees with age name, surname and age filters
all_employees = Employee.all(name='John', surname='Doe', age=25)

# delete an employee by id
employee = Employee.get(1)
employee.delete()
```

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


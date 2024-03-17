from employee import Employee
from db import conn


first_user = Employee.get(1)
if first_user is None:
    first_user = Employee("name", "surname", "age")
    first_user.save()

first_user.name = "Tornike"
first_user.age = 25
first_user.save()

all_employee = Employee.all(
    name="Tornike",
    surname="surname",
    age=26
)

conn.commit()
conn.close()

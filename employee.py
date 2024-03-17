from db import c, conn


class Employee(object):
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, pk):
        result = c.execute("""
            SELECT * FROM employee
            WHERE id = ? 
            """, (pk,)
                           )
        value = result.fetchone()
        if value:
            return Employee(value["name"], value["surname"], value["age"], value["id"])
        return None

    @classmethod
    def all(cls, **kwargs):
        query = "SELECT * FROM employee"

        if kwargs:
            conditions = " AND ".join(f"{key} = ?" for key in kwargs)
            query += " WHERE " + conditions
            values = tuple(kwargs.values())
        else:
            values = ()

        all_employee = c.execute(query, values)
        return [
            Employee(employee["name"], employee["surname"], employee["age"], employee["id"])
            for employee in all_employee
        ]

    def __repr__(self):
        return "<Employee {}>".format(self.name)

    def update(self):
        c.execute("""
            UPDATE employee
            SET name = ?, surname = ?, age = ?
            WHERE id = ? """,
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("""
            INSERT INTO employee (name, surname, age)
            VALUES (?, ?, ?)""", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    def save(self):
        if self.id is None:
            self.create()
        else:
            self.update()
        return self

    def delete(self):
        c.execute("""
            DELETE FROM employee
            WHERE id = ?""", (self.id,))

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

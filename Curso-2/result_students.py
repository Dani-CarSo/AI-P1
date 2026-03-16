#LAB Modulo 4- Sección 3
#Evaluating students' results
# Python essentials 2

from os import strerror

class StudentsDataException(Exception):
    """Base exception for all student-data errors."""
    pass


class WrongLine(StudentsDataException):
    """Raised when a line doesn't have exactly 3 valid fields."""
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


class FileEmpty(StudentsDataException):
    """Raised when the source file exists but contains no data."""
    def __init__(self):
        super().__init__(self)


data = {}   

file_name = input("Enter student's data filename: ")

try:
    f = open(file_name, "rt")
    lines = f.readlines()
    f.close()

  
    if len(lines) == 0:
        raise FileEmpty()

    for i, line in enumerate(lines):
        columns = line.split()

        
        if len(columns) != 3:
            raise WrongLine(i + 1, line)

        student = columns[0] + ' ' + columns[1]

        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)

        data[student] = data.get(student, 0.0) + points

    for student in sorted(data.keys()):
        print(f"{student:20s} {data[student]}")

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
except WrongLine as e:
    print(f"Wrong line #{e.line_number} in source file: {e.line_string}", end="")
except FileEmpty:
    print("Source file empty")
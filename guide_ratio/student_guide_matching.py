def match_students_teachers(students, teachers):
    class Person:
        def __init__(self, name, pref, count=None):
            self.name = name
            self.pref = pref
            self.count = count if count is not None else len(pref)

        def to_dict(self):
            return {'name': self.name, 'pref': self.pref, 'count': self.count}

    # teachers = [
    #     Person('Joseph', ['Student1','Priya','ghi'], 3),
    #     Person('Alice', ['jkl','mno','pqr'], 2),
    #     Person('Bob', ['stu','Shounak','yz'], 4),
    #     # add more teachers here
    # ]

    # students = [
    #     Person('Shounak', ['Joseph', 'Alice', 'Bob']),
    #     Person('Rahul', ['Alice', 'Bob', 'Joseph']),
    #     Person('Priya', ['Bob', 'Joseph', 'Alice']),
    #     Person('Student1', ['Joseph', 'Alice', 'Bob']),
    #     Person('Student2', ['Alice', 'Bob', 'Joseph']),
    #     Person('Student3', ['Bob', 'Joseph', 'Alice']),
    #     Person('Student4', ['Joseph', 'Alice', 'Bob']),
    #     Person('Student5', ['Alice', 'Bob', 'Joseph']),
    # ]

    # Convert teachers and students to dictionaries
 
    final_pairs = []

    # Stage 1: Matching
    unmatched_students = []
    for student in students:
        for teacher in teachers:
            if student['name'] in teacher['pref'] and teacher['name'] in student['pref']:
                if teacher['count'] > 0:
                    teacher['count'] -= 1
                    final_pairs.append(
                        {
                            'student': student['name'],
                            'teacher': teacher['name'],
                            'code': 'm'
                        }
                    )
                    
                    break
        else:
            unmatched_students.append(student)

    # Stage 2: Scheduling
    for student in unmatched_students:
        for teacher in teachers:
            if teacher['count'] > 0:
                teacher['count'] -= 1
                final_pairs.append(
                        {
                            'student': student['name'],
                            'teacher': teacher['name'],
                            'code': 's'
                        }
                    )
                break
        else:
            print("The ratio is not maintained. There are not enough teachers for the students.")
            break
    return final_pairs
    print(final_pairs)

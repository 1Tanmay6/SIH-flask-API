def match_students_teachers(students, teachers):
    class Person:
        def __init__(self, name, pref, count=None):
            self.name = name
            self.pref = pref
            self.count = count if count is not None else len(pref)

        def to_dict(self):
            return {'name': self.name, 'pref': self.pref, 'count': self.count}

    final_pairs = []

    # Stage 1: Matching
    unmatched_students = []
    for student in students:
        for teacher in teachers:
            if any(pref in teacher['pref'] for pref in student['pref']):
                if teacher['count'] > 0:
                    teacher['count'] -= 1
                    final_pairs.append(
                        {
                            'student': student['name'],
                            'teacher': teacher['name'],
                            'st_domain': student['pref'],
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
                            'st_domain': student['pref'],
                            'code': 's'
                        }
                    )
                break
        else:
            return {'error':"The ratio is not maintained. There are not enough teachers for the students."}
            break

    return final_pairs


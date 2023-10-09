class Person:
    def __init__(self, name, domains):
        self.name = name
        self.domains = domains

def match_students_mentors(students, mentors):
    matches = []
    for student in students:
        match_found = False
        for domain in student.domains:
            for mentor in mentors:
                if domain in mentor.domains:
                    match = {'st_name': student.name, 'mentor_name': mentor.name, 'st_domains': student.domains}
                    matches.append(match)
                    mentors.remove(mentor)
                    match_found = True
                    break
            if match_found:
                break
        if not match_found:
            match = {'st_name': student.name, 'mentor_name': 'NA', 'st_domains': student.domains}
            matches.append(match)
    return matches

def output_list_maker():
    db_st = [
        {
            'name': 'Student1',
            'domain': ['Domain1', 'Domain2', 'Domain3']
        },
        {
            'name': 'Student2',
            'domain': ['Domain4', 'Domain5', 'Domain6']
        },
        {
            'name': 'Student3',
            'domain': ['Domain7', 'Domain8', 'Domain9']
        },
        {
            'name': 'Student4',
            'domain': ['Domain1', 'Domain10', 'Domain11']
        },
        {
            'name': 'Student5',
            'domain': ['Domain2', 'Domain12', 'Domain13']
        },
        {
            'name': 'Student6',
            'domain': ['Domain3', 'Domain6', 'Domain14']
        },
        {
            'name': 'Student7',
            'domain': ['Domain4', 'Domain7', 'Domain15']
        },
        {
            'name': 'Student8',
            'domain': ['Domain5', 'Domain8', 'Domain1']
        },
        {
            'name': 'Student9',
            'domain': ['Domain6', 'Domain9', 'Domain2']
        },
        {
            'name': 'Student10',
            'domain': ['Domain7', 'Domain10', 'Domain3']
        },
        {
            'name': 'Student11',
            'domain': ['Domain8', 'Domain11', 'Domain4']
        },
        {
            'name': 'Student12',
            'domain': ['Domain9', 'Domain12', 'Domain5']
        },
        {
            'name': 'Student13',
            'domain': ['Domain10', 'Domain13', 'Domain6']
        },
        {
            'name': 'Student14',
            'domain': ['Domain11', 'Domain14', 'Domain7']
        },
        {
            'name': 'Student15',
            'domain': ['Domain12', 'Domain15', 'Domain8']
        },
        {
            'name': 'Student16',
            'domain': ['Domain13', 'Domain1', 'Domain9']
        },
        {
            'name': 'Student17',
            'domain': ['Domain14', 'Domain2', 'Domain10']
        },
        {
            'name': 'Student18',
            'domain': ['Domain15', 'Domain3', 'Domain11']
        },
        {
            'name': 'Student19',
            'domain': ['Domain1', 'Domain4', 'Domain12']
        },
        {
            'name': 'Student20',
            'domain': ['Domain2', 'Domain5', 'Domain13']
        },
        {
            'name': 'Student21',
            'domain': ['Domain3', 'Domain6', 'Domain14']
        },
        {
            'name': 'Student22',
            'domain': ['Domain4', 'Domain7', 'Domain15']
        },
        {
            'name': 'Student23',
            'domain': ['Domain5', 'Domain8', 'Domain1']
        },
        {
            'name': 'Student24',
            'domain': ['Domain6', 'Domain9', 'Domain2']
        },
        {
            'name': 'Student25',
            'domain': ['Domain7', 'Domain10', 'Domain3']
        },
        {
            'name': 'Student26',
            'domain': ['Domain8', 'Domain11', 'Domain4']
        },
        {
            'name': 'Student27',
            'domain': ['Domain9', 'Domain12', 'Domain5']
        },
        {
            'name': 'Student28',
            'domain': ['Domain10', 'Domain13', 'Domain6']
        },
        {
            'name': 'Student29',
            'domain': ['Domain11', 'Domain14', 'Domain7']
        },
        {
            'name': 'Student30',
            'domain': ['Domain12', 'Domain15', 'Domain8']
        },
        {
            'name': 'Student31',
            'domain': ['Domain13', 'Domain1', 'Domain9']
        },
        {
            'name': 'Student32',
            'domain': ['Domain14', 'Domain2', 'Domain10']
        },
        {
            'name': 'Student33',
            'domain': ['Domain15', 'Domain3', 'Domain11']
        },
        {
            'name': 'Student34',
            'domain': ['Domain1', 'Domain4', 'Domain12']
        },
        {
            'name': 'Student35',
            'domain': ['Domain2', 'Domain5', 'Domain13']
        },
        {
            'name': 'Student36',
            'domain': ['Domain3', 'Domain6', 'Domain14']
        },
        {
            'name': 'Student37',
            'domain': ['Domain4', 'Domain7', 'Domain15']
        },
        {
            'name': 'Student38',
            'domain': ['Domain5', 'Domain8', 'Domain1']
        },
        {
            'name': 'Student39',
            'domain': ['Domain6', 'Domain9', 'Domain2']
        },
        {
            'name': 'Student40',
            'domain': ['Domain7', 'Domain10', 'Domain3']
        },
        {
            'name': 'Student41',
            'domain': ['Domain8', 'Domain11', 'Domain4']
        },
        {
            'name': 'Student42',
            'domain': ['Domain9', 'Domain12', 'Domain5']
        },
        {
            'name': 'Student43',
            'domain': ['Domain10', 'Domain13', 'Domain6']
        },
        {
            'name': 'Student44',
            'domain': ['Domain11', 'Domain14', 'Domain7']
        },
        {
            'name': 'Student45',
            'domain': ['Domain12', 'Domain15', 'Domain8']
        },
        {
            'name': 'Student46',
            'domain': ['Domain13', 'Domain1', 'Domain9']
        },
        {
            'name': 'Student47',
            'domain': ['Domain14', 'Domain2', 'Domain10']
        },
        {
            'name': 'Student48',
            'domain': ['Domain15', 'Domain3', 'Domain11']
        },
        {
            'name': 'Student49',
            'domain': ['Domain1', 'Domain4', 'Domain12']
        },
        {
            'name': 'Student50',
            'domain': ['Domain2', 'Domain5', 'Domain13']
        },
        {
            'name': 'Student51',
            'domain': ['Domain3', 'Domain6', 'Domain14']
        },
        {
            'name': 'Student52',
            'domain': ['Domain4', 'Domain7', 'Domain15']
        },
        {
            'name': 'Student53',
            'domain': ['Domain5', 'Domain8', 'Domain1']
        },
        {
            'name': 'Student54',
            'domain': ['Domain6', 'Domain9', 'Domain2']
        },
        {
            'name': 'Student55',
            'domain': ['Domain7', 'Domain10', 'Domain3']
        }
    ]


    db_me = [
        {
            'name': 'Mentor1',
            'domain': ['Domain1', 'Domain7', 'Domain8']
        },
        {
            'name': 'Mentor2',
            'domain': ['Domain9', 'Domain15', 'Domain11']
        },
        {
            'name': 'Mentor3',
            'domain': ['Domain7', 'Domain12', 'Domain11']
        },
        {
            'name': 'Mentor4',
            'domain': ['Domain3', 'Domain10', 'Domain14']
        },
        {
            'name': 'Mentor5',
            'domain': ['Domain6', 'Domain13', 'Domain9']
        },
        {
            'name': 'Mentor6',
            'domain': ['Domain2', 'Domain8', 'Domain15']
        },
        {
            'name': 'Mentor7',
            'domain': ['Domain5', 'Domain12', 'Domain14']
        },
        {
            'name': 'Mentor8',
            'domain': ['Domain4', 'Domain11', 'Domain13']
        },
        {
            'name': 'Mentor9',
            'domain': ['Domain1', 'Domain7', 'Domain8']
        },
        {
            'name': 'Mentor10',
            'domain': ['Domain9', 'Domain15', 'Domain11']
        },
        {
            'name': 'Mentor11',
            'domain': ['Domain7', 'Domain12', 'Domain11']
        },
        {
            'name': 'Mentor12',
            'domain': ['Domain3', 'Domain10', 'Domain14']
        },
        {
            'name': 'Mentor13',
            'domain': ['Domain6', 'Domain13', 'Domain9']
        },
        {
            'name': 'Mentor14',
            'domain': ['Domain2', 'Domain8', 'Domain15']
        },
        {
            'name': 'Mentor15',
            'domain': ['Domain5', 'Domain12', 'Domain14']
        },
        {
            'name': 'Mentor16',
            'domain': ['Domain4', 'Domain11', 'Domain13']
        },
        {
            'name': 'Mentor17',
            'domain': ['Domain1', 'Domain7', 'Domain8']
        },
        {
            'name': 'Mentor18',
            'domain': ['Domain9', 'Domain15', 'Domain11']
        },
        {
            'name': 'Mentor19',
            'domain': ['Domain7', 'Domain12', 'Domain11']
        },
        {
            'name': 'Mentor20',
            'domain': ['Domain3', 'Domain10', 'Domain14']
        },
        {
            'name': 'Mentor21',
            'domain': ['Domain6', 'Domain13', 'Domain9']
        },
        {
            'name': 'Mentor22',
            'domain': ['Domain2', 'Domain8', 'Domain15']
        },
        {
            'name': 'Mentor23',
            'domain': ['Domain5', 'Domain12', 'Domain14']
        },
        {
            'name': 'Mentor24',
            'domain': ['Domain4', 'Domain11', 'Domain13']
        },
        {
            'name': 'Mentor25',
            'domain': ['Domain1', 'Domain7', 'Domain8']
        },
        {
            'name': 'Mentor26',
            'domain': ['Domain9', 'Domain15', 'Domain11']
        },
        {
            'name': 'Mentor27',
            'domain': ['Domain7', 'Domain12', 'Domain11']
        },
        {
            'name': 'Mentor28',
            'domain': ['Domain3', 'Domain10', 'Domain14']
        },
        {
            'name': 'Mentor29',
            'domain': ['Domain6', 'Domain13', 'Domain9']
        },
        {
            'name': 'Mentor30',
            'domain': ['Domain2', 'Domain8', 'Domain15']
        },
        {
            'name': 'Mentor31',
            'domain': ['Domain5', 'Domain12', 'Domain14']
        },
        {
            'name': 'Mentor32',
            'domain': ['Domain4', 'Domain11', 'Domain13']
        },
        {
            'name': 'Mentor33',
            'domain': ['Domain1', 'Domain7', 'Domain8']
        },
        {
            'name': 'Mentor34',
            'domain': ['Domain9', 'Domain15', 'Domain11']
        },
        {
            'name': 'Mentor35',
            'domain': ['Domain7', 'Domain12', 'Domain11']
        },
        {
            'name': 'Mentor36',
            'domain': ['Domain3', 'Domain10', 'Domain14']
        },
        {
            'name': 'Mentor37',
            'domain': ['Domain6', 'Domain13', 'Domain9']
        },
        {
            'name': 'Mentor38',
            'domain': ['Domain2', 'Domain8', 'Domain15']
        },
        {
            'name': 'Mentor39',
            'domain': ['Domain5', 'Domain12', 'Domain14']
        },
        {
            'name': 'Mentor40',
            'domain': ['Domain4', 'Domain11', 'Domain13']
        }
    ]


    students = [Person(st['name'], st['domain']) for st in db_st]

    mentors = [Person(me['name'], me['domain']) for me in db_me]

    matches = match_students_mentors(students, mentors)

    return matches
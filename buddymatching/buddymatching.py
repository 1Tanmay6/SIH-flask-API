import random

# Define the database file paths
STUDENTS_FILE = "buddymatching/content/Students.txt"
MENTORS_FILE = "buddymatching/content/buddy_mentors.txt"


def read_students():
    try:
        with open(STUDENTS_FILE, "r") as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        return []


def read_mentors():
    """Reads mentor information from the text file."""
    try:
        with open(MENTORS_FILE, "r") as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        return []


def write_students(students_data):
    """Writes updated student information to the text file."""
    with open(STUDENTS_FILE, "w") as file:
        file.writelines('\n'.join(students_data))


def allocate_buddy_mentor(student_name, student_domains, mentor_data):
    """Allocates a buddy mentor to a student based on the research domain."""
    matching_buddy_mentors = []

    for mentor in mentor_data:
        for domain in student_domains:
            if domain in mentor:
                matching_buddy_mentors.append(mentor)

    if not matching_buddy_mentors:
        return {"student_name": student_name, "mentor_allotted": "NA", "Domain": student_domains}

    # Randomly select a buddy mentor from the filtered list
    assigned_mentor = random.choice(matching_buddy_mentors)

    # Remove the assigned mentor from the list
    mentor_data.remove(assigned_mentor)

    return {"student_name": student_name, "mentor_allotted": assigned_mentor, "Domain": student_domains}

def output_list_maker():
    students_data = read_students()
    mentors_data = read_mentors()

    output_list = []  # Create an empty list to store the output

    for student_info in students_data:
        student_info = eval(student_info)  # Convert the string to a dictionary
        student_name = student_info["name"]
        student_domains = student_info["domain"]

        assigned_mentor = allocate_buddy_mentor(student_name, student_domains, mentors_data)

        output_list.append(assigned_mentor)

    return output_list



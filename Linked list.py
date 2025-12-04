class StudentNode:
    def __init__(self, name, admission_no, grades):
        self.name = name
        self.admission_no = admission_no
        self.grades = grades
        self.next = None

student_list = StudentNode("Otieno", "CIM/098/29", {"Python": 85, "Java": 90})
student_list.next = StudentNode("George", "CIM/001/29", {"Python": 78, "Java": 92})
student_list.next.next = StudentNode("Naomi", "CIM/008/29", {"Python": 87, "Java": 95})

linked_dict = {}

current = student_list
while current:
    if current.next:
        next_adm = current.next.admission_no
    else:
        next_adm = None
    
    linked_dict[current.admission_no] = {
        "name": current.name,
        "grades": current.grades,
        "next": next_adm
    }
    
    current = current.next

print("Student linked list as dictionary:")
for adm, data in linked_dict.items():
    print(f"Admission {adm}:")
    print(f"  Name: {data['name']}")
    print(f"  Grades: {data['grades']}")
    print(f"  Next student: {data['next']}")
    print()

class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(f"Roll: {temp.roll}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next


# Main program
students = StudentList()
students.add(1, "Siddhi", 85)
students.add(2, "Sneha", 90)
students.add(3, "Somesh", 80)

print("Student Records:")
students.display()

## 🐍 Linked List with Dictionary Nodes

# ---
# ### 1. Node Class Definition

class Node:
    """A Node in the linked list. Its data attribute holds a dictionary."""
    def __init__(self, student_data):
        # The data is the student dictionary (Name, Admission, Grades).
        self.data = student_data 
        # Pointer to the next node.
        self.next = None

# ---
# ### 2. LinkedList Class Definition

class LinkedList:
    """Manages the linked list operations, including insertion and display."""
    def __init__(self):
        # The starting point of the list.
        self.head = None

    def insert_at_beginning(self, student_data):
        """Adds a new node containing the student_data dictionary at the start of the list."""
        # 1. Create a new Node.
        new_node = Node(student_data)
        
        # 2. Set the new node's next pointer to the current head.
        new_node.next = self.head
        
        # 3. Update the head to point to the new node.
        self.head = new_node

    def display_list(self):
        """Prints the data (dictionaries) of all nodes in the list."""
        current_node = self.head
        if current_node is None:
            print("The student list is empty.")
            return

        print("\n**📚 Student Linked List Records 📚**")
        while current_node:
            print("-" * 30)
            # Iterate through the dictionary stored in the node's data
            for key, value in current_node.data.items():
                # Format the output for readability
                if key == "Grades" and isinstance(value, dict):
                    grades_str = ", ".join([f"{k}: {v}" for k, v in value.items()])
                    print(f"**{key}**: {{ {grades_str} }}")
                else:
                    print(f"**{key}**: {value}")
            current_node = current_node.next
        print("-" * 30)

# ---
# ### 3. Usage and Execution

# Create an instance of the LinkedList
student_list = LinkedList()

# Define the student data dictionaries
student1_data = {
    "Name": "Alice Johnson",
    "Admission": "S001",
    "Grades": {"Math": 'A', "CompSci": 'A-'}
}

student2_data = {
    "Name": "Bob Smith",
    "Admission": "S002",
    "Grades": {"Math": 'B+', "Physics": 'B'}
}

student3_data = {
    "Name": "Charlie Brown",
    "Admission": "S003",
    "Grades": {"Chem": 'A', "Bio": 'A+'}
}

# Insert the data into the linked list (inserts at the beginning, so Alice will be first)
student_list.insert_at_beginning(student3_data) # Becomes the 3rd node
student_list.insert_at_beginning(student2_data) # Becomes the 2nd node
student_list.insert_at_beginning(student1_data) # Becomes the 1st node (the head)

# Display the contents of the linked list
student_list.display_list()

                                            

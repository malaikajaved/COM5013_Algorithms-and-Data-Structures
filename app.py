from flask import Flask, render_template, request  # Import necessary modules from Flask

# Node class for managing linked list nodes
class Node:
    def __init__(self, value, next_node=None):
        """
        Initialize a Node with a value and an optional reference to the next node.
        """
        self.value = value  # Store the value of the node
        self.next_node = next_node  # Reference to the next no
        def get_value(self):
        return self.value  # Return the value of the node

    def get_next_node(self):
        return self.next_node  # Return the reference to the next node

    def set_next_node(self, next_node):
        self.next_node = next_node  # now set the reference to the next node

# this is a LinkedList class for handling contacts
class LinkedList:
    def __init__(self, value=None):
        """
        Initialize a LinkedList with an optional head node value.
        """
        self.head_node = Node(value) if value else None  # Create the head node of the linked list

    def get_head_node(self):
        return self.head_node  # Return the head node of the linked list

    def append(self, new_value):
        """
        Append a new value to the end of the linked list.
        """
        if not self.head_node:  # If the list is empty
            self.head_node = Node(new_value)  # Set the head node's value to the new value
            return
        current = self.head_node  # Start from the head node
        while current.get_next_node() is not None  # Traverse to the end of the list
            current = current.get_next_node()
        current.set_next_node(Node(new_value))  # Append the new value as a new node
    def search(self, key):
        """
        Search for a key in the linked list and return the associated value.
        """
        current_node = self.head_node
        while current_node:
            if current_node.get_value()[0] == key:  # Check if the key matches
                return current_node.get_value()[1]  # Return the associated value
            current_node = current_node.get_next_node()
        return None  # Return None if the key is not found
        
   def stringify_list(self):
        """
        Return a string representation of all contacts in the linked list.
        """
        if not self.head_node:
            return "Empty"
        string_list = ""
        current_node = self.head_node
        while current_node:
            string_list += str(current_node.get_value()) + " -> "
            current_node = current_node.get_next_node():
        return string_list.strip(" -> ")  # Remove the trailing arrow

        # HashMap class for managing contact storage
class HashMap:
    def __init__(self, array_size):
        """
        Initialize a HashMap with a fixed array size.
        """
        self.array_size = array_size  # Store the size of the hash map
        self.array = [None] * array_size  # Create an array of None values for the hash map

def hash_function(self, key):
        """
        Calculate a hash value using the sum of ASCII values of the characters in the key.
        """
        return sum(ord(char) for char in key) % self.array_size  # Return the hash index

def assign(self, key, value):
        """
        Assign a key-value pair to the hash map, handling collisions using a linked list.
        """
        index = self.hash_function(key)  # Get the index for the key using the hash function
        if self.array[index] is None:  # If there is no collision at this index
            self.array[index] = LinkedList((key, value))  # Create a new linked list for this key-value pair
        else:
            self.array[index].append((key, value))  # Append the key-value pair to the existing linked list
            
def retrieve(self, key):
        """
        Retrieve a value from the hash map using a key.
        """
        index = self.hash_function(key)  # Get the index for the key
        current_list = self.array[index]  # Get the linked list at that index
        if current_list:  # If the linked list exists
            return current_list.search(key)  # Search for the key in the linked list
        return None  # Return None if the linked list does not exist

def search_all(self, term):
        """
        Search for a term in all contacts stored in the hash map.
        """
        results = []
        for bucket in self.array:
            if bucket:  # If the linked list exists at this index
                current_node = bucket.get_head_node()  # Start from the head node
                while current_node:  # Traverse the linked list
                    contact = current_node.get_value()  # Get the contact data
                    if contact and (
                        term in contact[0]  # Check if the term matches the name
                        or term in contact[1]["phone_number"]  # Check if the term matches the phone number
                        or term in contact[1]["postal_address"]  # Check if the term matches the postal address
                    ):
                        results.append(contact)  # Add matching contact to results
                    current_node = current_node.get_next_node()  # Move to the next node
        return results  # Return the list of matching contacts

 def print_all(self):
        """
        Return a string representation of all contacts in the hash map.
        """
        all_contacts = []
        for bucket in self.array:
            if bucket:  # If the linked list exists at this index
                current_node = bucket.get_head_node()  # Start from the head node
                while current_node:  # Traverse the linked list
                    contact = current_node.get_value()  # Get the contact data
                    if contact:
                        # Format the contact for better readability
                        name = contact[0]
                        details = contact[1]
                        formatted_contact = f"Name: {name}, Phone: {details['phone_number']}, Address: {details['postal_address']}"
                        all_contacts.append(formatted_contact)
                    current_node = current_node.get_next_node()  # Move to the next node
        return "<br>".join(all_contacts) if all_contacts else "No contacts available."  # Return formatted contacts or a message if empty

# Flask app setup
app = Flask(__name__)
contacts = HashMap(10)  # Create the contacts list with 10 slots


# Preload some sample contacts
def preload_contacts():
    contacts.assign("Malaika", {"phone_number": "1234586124", "postal_address": "25 wendover Str"})
    contacts.assign("Amara", {"phone_number": "347581024", "postal_address": "456 desbourough Rd"})
    contacts.assign("Sam", {"phone_number": "3755278492", "postal_address": "71 brunel Ave"})
    contacts.assign("Moana", {"phone_number": "4738946528", "postal_address": "15 totter Rd"})
    print("Preloaded contacts:")
    print(contacts.print_all())


preload_contacts()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        address = request.form.get("address")
        if name and phone and address:
            contacts.assign(name, {"phone_number": phone, "postal_address": address})
            return render_template("results.html", message=f"Contact '{name}' added successfully!")
        else:
            return render_template("results.html", message="All fields are required!")
    return render_template("index.html")


@app.route("/search", methods=["GET"])
def search():
    term = request.args.get("term")
    if term:
        results = contacts.search_all(term)
        if results:
            result_message = "<br>".join([f"{res[0]}: {res[1]}" for res in results])
            return render_template("results.html", message=f"Results:<br>{result_message}")
        else:
            return render_template("results.html", message="No results found.")
    return render_template("results.html", message="Please provide a search term.")


@app.route("/view", methods=["GET"])
def view_all():
    """
    View all contacts stored in the hash map.
    """
    all_contacts = contacts.print_all()  # Fetch all contacts as a formatted string
    if all_contacts.strip():  # Check if there are any contacts
        # Wrap each contact in styled div elements
        formatted_contacts = "".join([
            f'<div class="contact-item">'
            f'<p>{contact}</p>'
            f'</div>'
            for contact in all_contacts.split("<br>")
        ])
        return render_template(
            "results.html",
            message=f"<h2>All Contacts:</h2>{formatted_contacts}"
        )
    return render_template("results.html", message="No contacts available.")




if __name__ == "__main__":
    app.run(debug=True)

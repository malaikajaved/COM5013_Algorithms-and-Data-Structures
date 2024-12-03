from flask Flask, render_template, request

class Node: #Node class for managing linked list nodes
    def__init__(self, value, next_node=None): 
      """
      initialise a Node with a value and an optional refernec to the node.
      """

      self.value = value  #we are going to store the contact info
      self.next_node = next_node  # points to the next node
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next_node(self, next_node):
        self.next_node = next_node





#linkedlist class is to handle collisions in hashmap
class Linkedlist:
   def__init__(self, value=None):
        """
        initialise a Likedlist with an optional head node value.
        """
      self.head_node = None(value)
# now retirve contact by name
def get_head_node (self):
    return self.head_node

def append(self, new_value):
    """
    append a new value to the end of the linked list
    """
current = self.head_node 
while current.get_next_node() is not none:
    current = current.get_next_node()
current.set_next_node(Node(new_value))

def search(self, key):
    """
    search for a key in the linked list and return the corresponding value
    """
current_node = self.head_node
while current_node:
    if current_node.get_value()[0] == key:
        return current_node.get_value()[1]
    current_node = current_node.get_next()
return None

def strigify_list(self):
    """
    create a readable string representation of the linked list.
    """
string list =""   #this string will be used to build the represantation of the linked list
current_node = self.get_head_node()
while current_node:   # it will loop through each node in the linked list
    if current_node.get_value():
        string_list += str(current_node.get value()) + " -> " # this creates a chain like represanation of the linked list
    current_node = current_node.get_next_node()
return string_list.strip(" -> ") # removes trailing from the end of the string 

# Hashmap class is used for managing contact storage 
class Hashmap:  
    def __init__(self, array_size):
        """
        initalise Hashmap with a fixed array size.
        """
        self.array_size = array_size
        self.array = [None] * array_size
    def hash_function(self, key):
        """
        calculating the hash value using sum of ASCII values of the characters in the key.
        """
        return sum(ord(char) for char in key)% self.array_size
        def assign(self, key, value):
            """
            Assign a key-value pair tothe hash map, handling colliions using alinked list.
            """
            index = self.hash_function(key)
            if self.array[index] is None:
                self.array[index] = LinkedList((key, value))
            else:
                self.array[index.append((key, value))
    def retrieve(self, key):
        """
        Retrieve a valuefrom the hash mapusing a key.
        """
        index = self.hash_function(key)
        current_list = self.array[index]
        if current_list:
            return current_list.search(key)
        return None

    def search_all(self, term):
        """
        search for a term in all fields (name, phone number, postal address).
        """
        results = []
        for bucket in self.array:
            if bucket:
                current_node = bucket.get_head_node()
                while current_node:
                    contact = current_node.get_value()
                    if (
                        term in contact[0] or
                        term in contact[1]["phone_number"] or
                        term in contact[1]["postal_address"]
                    ):
                        results.append(contact)
                        current_node = current_node.get_next_node()
                        return results
    def print_all(self):
        """
        Return a string represntation of all contacts in the hash map.
        """
        all_contacts = []
        for bucket in self.array:
            if bucket:
                all_contacts.append(bucket.stringify_list())
                return "\n".join(all_contacts)
                
# flask app setup
app = Flask(__name__)

# create the contacts list with 10 slots
contacts = HashMap(10)

#preload some sample contacts
def preload_contacts():
    """
    preload the hash map wuth sample contacts.
        """
    contacts.assign("Malaika", {"phone_number": "1234586124", "postal_address": "123 Rainbow St"})
    contacts.assign("Amara", {"phone_number": "347581024", "postal_address": "456 Sunshine Rd"})
    contacts.assign("Sam", {"phone_number": "3755278492", "postal_address": "789 Star Ln"})
    contacts.assign("Moana", {"phone_number": "4738946528", "postal_address": "101 Ocean Ave"})

preload_contacts()

@app.route("/", methods= ["GET", "POST"])
def index():
    """
    home page with forms for adding and searching contacts.
    if request.method == "POST":
     name = request.form["name"]
     phone = request.form["phone"]
     address = request.form["address]
     if name and phone and address:
     contacts.assign(name, {"phone_nimber": phone, "postal_address": address})
       return render_template("results.html, message=f"contact {name} added successfully!")
     else:
       return  render_template("result.html", message="All fields are required!")
       return render_template("index.html")

@app.route("/search", method=["GET"])
def search():
""" 
search for a contact by any field (name, phone or address).
"""
term = request.args.get("term")
if term:
  resuls = contacts.search_all(term)
  if results:
    result_message ="<br>".join([f"{res[0]}: {res[1]}" for res in resluts])
     return render_template("results.html", message=f"Results:<br>{result_message}")
    else:
      return render_template("resultshtml", message="please enter a search term.")

@app.route("/view")
def view():
"""
view allcontacts stored in the hash map.
"""
all_contacts = contacts.print_all()
return render_template("results.html", message=f"All contacts:<br>{all_contacts replace(' -> ', '<br>')}")

if__name__ == "__main__":
   app.run(debug=True)
   

    


     



        

    


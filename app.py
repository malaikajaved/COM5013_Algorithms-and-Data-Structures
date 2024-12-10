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
        self.next_node = next_node  # Set the reference to the next node


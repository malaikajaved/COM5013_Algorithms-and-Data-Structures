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

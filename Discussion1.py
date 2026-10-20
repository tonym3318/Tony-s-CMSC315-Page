"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class NetworkDevice:  # Parent Class
    """Using my experience working within a broadband network."""

    network_type =  "Broadband"

    def __init__(self, device_name, location):
        """Initialize the device name and location."""
        self.device_name = device_name
        self.location = location

    def display_info(self):
        """Display the network device's information."""
        print(f"Device: {self.device_name}, Location: {self.location}")

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class OpticalNode(NetworkDevice):   # Child class
    """Represent an Optical Node,this is the first part of a HFC (Hybrid Fiber/Coaxial Network"""
    device_type = "HFC Node"

    def __init__(self, device_name, location, gain_db, operational_status):
        """List the Optical Nodes information and operating status."""
        super().__init__(device_name, location)
        self.gain_db = gain_db
        self.operational_status = operational_status

    def adjust_gain(self, new_gain_db):
        """Adjust the output gain of the HFC Node"""
        self.gain_db = new_gain_db

    def display_info(self):
        """Show the Optical Node's information and operating settings."""
        print(f"Device: {self.device_name}, "
              f"Location: {self.location}, "
              f"Type: {self.device_type}, "
              f"Gain: {self.gain_db} dB, "
              f"Status: {self.operational_status}")

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    """Demonstrate class and instance namespaces using HFC Optical Nodes."""

    print("\n=== Namespace Demonstration ===")

    # Create 3 separate optical nodes
    node1 = OpticalNode("NC4000 GJ101", "Grand Junction", 49, "Online")
    node2 = OpticalNode("GS7000 GJ202", "Grand Junction", 49, "Online")
    node3 = OpticalNode("GAP GJ303", "Fruita", 0, "Offline")

    # Access the class variable through the class
    print("Class device type:", OpticalNode.device_type)

    # Access the class variable through an instance
    print("Node1 device type:", node1.device_type)

    # Add a firmware attribute to Node1 only
    node1.firmware_version = "1.2.0"

    # Display Each node's instance namespace
    print("\nNode1 namespace:", node1.__dict__)
    print("Node2 namespace:", node2.__dict__)
    print("Node3 namespace:", node3.__dict__)

    # Display the Optical Node class namespace
    print("\nOpticalNode class namespace:")
    print(OpticalNode.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    """Demonstrate shallow and deep copying of Optical Node data."""

    print("\n=== Copy Demonstration ===")

    # Create an optical node with nested mutable RF configuration data
    node = OpticalNode("GS7000 GJ202", "Grand Junction", 49, "Online")

    node.rf_config = {
        "output_levels": [42, 47],
        "frequencies": [303, 711]
    }

    # Create a shallow copy and a deep copy
    shallow_node = copy(node)
    deep_node = deepcopy(node)

    # Modify the original node's nested RF output level
    node.rf_config["output_levels"][0] = 55

    # A shallow copy shares nested mutable data with the original
    # A deep copy has independent nested data

    print("\nOriginal Node:", node.rf_config)
    print("Shallow Copy:", shallow_node.rf_config)
    print("Deep Copy:", deep_node.rf_config)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    """Test network device inheritance, namespaces, and copying."""

    print("=== Unit 1 OOP Assignment ===")

    # Create and test the parent NetworkDevice class
    print("\n=== Parent Network Device ===")
    network_device = NetworkDevice("CMTS GJ01", "Grand Junction")
    network_device.display_info()

    #Create and test the child OpticalNode class
    print("\n=== Child Optical Node ===")
    optical_node = OpticalNode("GS7000 GJ202", "Grand Junction", 49, "Online")
    optical_node.display_info()

    # Demonstrate the child class unique method
    print("\n=== Adjjust Optical Node Gain ===")
    optical_node.adjust_gain(52)
    optical_node.display_info()

    # Demonstrate class and instance namespaces
    demonstrate_namespaces()

    # Demonstrate shallow and deep copying
    demonstrate_copying()

if __name__ == "__main__":
    main()
Project Overview
This was developed for the CMSC3315 Unit 1 Discussion assignment. The application shows object-oriented programming (OOP) concepts using examples from broadband telecommunications and Hybrid Fiber/Coaxial (HFC) networks. I chose this because this is the industry I currently work in.
The program demonstrats inheritance, method overriding, class and instance namespaces, and shallow versus deep copying.
Class Design and Inheritance
A parent class named NetworkDevice was created to represent a device operating within a broadband network. The class included a shared class variable, network_type, and two instance variables, device_name and location.
A child class named OpticalNode was created through inheritance from NetworkDevice. This class added a device_type class variable and two additional instance variables, gain_db and operational_status.
The child class also included an adjust_gain() method and overrode the parent class's display_info() method to display additional optical node information.
Namespace Demonstration
Three optical node objects were created to demonstrate how Python managed class and instance namespaces.
The class variable device_type was accessed through both the OpticalNode class and an individual object. A firmware_version attribute was dynamically added to only one optical node.
The __dict__ attribute was used to display the individual instance namespaces and the class namespace. The results showed that each optical node maintained its own instance attributes while sharing class-level information.
Shallow and Deep Copying
An optical node object was created with nested RF configuration data, including output levels and frequencies.
The copy() function was used to create a shallow copy, while deepcopy() was used to create an independent deep copy.

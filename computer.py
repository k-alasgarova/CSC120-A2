"""
Filename: computer.py
Description: Defines the Computer class
Author: Kamilla 
"""

class Computer:
    """
    A Computer is one computer item in the resale shop. It stores computer's details and includes methods to update it.
    """

    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        """
        Creates a new Computer object and sets all the attributes.
        """
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    def update_price(self, new_price):
        """
        Updates computer's price to a new one.
        """
        self.price = new_price

    def update_os(self, new_os):
        """
        Updates computer's OS to a new one.
        """
        self.operating_system = new_os

    def refurbish(self, new_os=None):
        """
        Updates price based on the year it was made. If new_os is provided, also updates OS.
        """
        if int(self.year_made) < 2000:
            self.price = 0
        elif int(self.year_made) < 2012:
            self.price = 250
        elif int(self.year_made) < 2018:
            self.price = 550
        else:
            self.price = 1000
        
        if new_os is not None:
            self.operating_system = new_os
        
    def __str__(self):
        """
        Returns a formatted string representing computer when printing inventory.
        """
        return(
            f"{self.description} -- "
            f"Processor Type: {self.processor_type}"
            f"Hard Drive Capacity: {self.hard_drive_capacity}"
            f"Memory: {self.memory}"
            f"Operating System: {self.operating_system}"
            f"Year Made: {self.year_made}"
            f"Price: {self.price}"
        )



class Computer:

    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    def update_price(self, new_price):
        self.price = new_price

    def update_os(self, new_os):
        self.operating_system = new_os

    def refurbish(self, new_os=None):
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
        return(
            f"{self.description} -- "
            f"Processor Type: {self.processor_type}"
            f"Hard Drive Capacity: {self.hard_drive_capacity}"
            f"Memory: {self.memory}"
            f"Operating System: {self.operating_system}"
            f"Year Made: {self.year_made}"
            f"Price: {self.price}"
        )


    # What methods will you need?
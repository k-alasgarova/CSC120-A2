"""
Filename: oo_resale_shop.pyei
Description: Defines the ResaleShop class
Author: Kamilla
"""

class ResaleShop:
    """
    ResaleShop represents the store that can store inventory and buy, sell, refurbish, and print the inventory.
    """
    def __init__(self):
        """
        Creates a new shop with an empty inventory list.
        """
        self.inventory = []
    
    def buy(self, computer):
        """
        Adds a Computer object to the inventory.
        """
        self.inventory.append(computer)
    
    def sell(self, computer):
        """
        Removes the object from the Computer inventory if present, otherwise prints an error mesage.
        """
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Computer not found. Please select another item to sell.")
        
    def update_price(self, computer, new_price):
        """
        Updates the prices of a Computer in the inventory; if not found, prints an error message.
        """
        if computer in self.inventory:
            computer.update_price(new_price)
        else:
            print("Computer not found. Cannot update price.")
        
    def refurbish(self, computer, new_os=None):
        """
        Updates the price based on year and optional OS (refurbishes a Computer in the inventory); prints error if computer isn't found.
        """
        if computer in self.inventory:
            computer.refurbish(new_os)
        else:
            print("Computer not found. Please select another item to refurbish.")
    
    def print_inventory(self):
        """
        Prints all computers in the inventory or no inventory message if empty.
        """
        if self.inventory:
            for item in self.inventory:
                print(item)
            else:
                print("No inventory to display.")


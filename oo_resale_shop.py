class ResaleShop:


    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
    
    def buy(self, computer):
        self.inventory.append(computer)
    
    def sell(self, computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
        else:
            print("Computer not found. Please select another item to sell.")
        
    def update_price(self, computer, new_price):
        if computer in self.inventory:
            computer.update_price(new_price)
        else:
            print("Computer not found. Cannot update price.")
        
    def refurbish(self, computer, new_os=None):
        if computer in self.inventory:
            computer.refurbish(new_os)
        else:
            print("Computer not found. Please select another item to refurbish.")
    
    def print_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(item)
            else:
                print("No inventory to display.")


    # What methods will you need?
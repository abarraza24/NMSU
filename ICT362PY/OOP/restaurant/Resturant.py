class Resturant:
    """A simple class descriping the name of the resturant and cuisine type and a small message for opening hours
    """
    
    # Standard Constructor: accepts primitive data
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
        
    def describe_restaurant(self):
        print(f"{self.name} is a resturant that specializes in {self.cuisine_type}.")
        
    def open_resturant(self):
        print(f"The {self.name} is currently opened.")
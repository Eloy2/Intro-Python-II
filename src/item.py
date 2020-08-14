

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    '''
    def __str__(self): # NOT USED IN CODE JUST FOR REFERENCE
        return f"{self.name}: {self.description}"
    '''
    def on_take(self):
        print(f"\nYou have picked up {self.name}")
    
    def on_drop(self):
        print(f"\nYou have dropped {self.name}")


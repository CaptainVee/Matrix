class Budget:

    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
    
    def deposit(self, amount, item):
        if item == 'food':
            self.food = self.food + amount
        elif item == 'clothing':
            self.clothing = self.clothing + amount
        elif item == 'entertainment':
            self.entertainment = self.entertainment + amount
        else:
            print('invalid item selected')

    def withdraw(self, amount, item):
        if item == 'food':
            self.food = self.food - amount
        elif item == 'clothing':
            self.clothing = self.clothing - amount
        elif item == 'entertainment':
            self.entertainment = self.entertainment - amount
        else:
            print('invalid item selected') 

    def balance(self, item):
        
        if item == 'food':
            return self.food
        elif item == 'clothing':
            return self.clothing
        elif item == 'entertainment':
            return self.entertainment
        else:
            print('invalid item selected')
            
    def transferFrom(self, category, amount):        
        if category == 'food':
            self.food -= amount  
        elif category == 'clothing':
            self.clothing -= amount
        elif category == 'entertainment':
            self.entertainment -= amount
    
    def transferTo(self, category, amount):        
        if category == 'food':
            self.food += amount  
        elif category == 'clothing':
            self.clothing += amount
        elif category == 'entertainment':
            self.entertainment += amount    
        
    def transfer(self, amount, from_category, to_category):
        self.transferFrom(from_category, amount)
        self.transferTo(to_category, amount)
        
        

###Initialize a budget object
budget_1 = Budget(100, 100, 100)

### Withdraw from a budget
budget_1.withdraw(100, 'food')

### deposit to a budget
budget_1.deposit(100, 'food')

### Transfer from one budget to another
budget_1.transfer(50, 'entertainment', 'food')

### Check budget balance
budget_1.balance('food')

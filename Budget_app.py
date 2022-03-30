class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.ledger = list()
        self.alldescriptions = "" # maybe bad but used to shut that shit of reference up.

    def __repr__(self):
        while len(self.name) <= 30:
            self.name = "*" + self.name + "*"
        for x in range(len(self.ledger)):
            while len(self.ledger[x]["description"]) <= 23:
                self.ledger[x]["description"] = self.ledger[x]["description"] + " "
            while len(str(self.ledger[x]["amount"])) <= 7:
                self.ledger[x]["amount"] = " " + str(self.ledger[x]["amount"])
            # self.each_descriptions_and_amounts = self.ledger[x]["description"][:24] + self.ledger[x]["amount"][:7]
            self.alldescriptions = self.alldescriptions + (self.ledger[x]["description"][:24] + self.ledger[x]["amount"][:8] + "\n")
        return self.name + "\n" + self.alldescriptions + "Total: " + str(self.balance)
    def deposit(self, amount, description):
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.balance + amount
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True
    def withdraw(self, amount, description):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": - amount, "description": description})
            self.balance = self.balance - amount
            return True
        else:
            return False
    def transfer(self, amount, destination):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "transfer to " + destination.name)
            destination.deposit(amount, "transfer from " + self.name)
            return True
        return False
    def get_balance(self):
        return self.balance
a = Category("food")
b = Category("clothing")
c = Category("entertainment")
a.deposit(50,"Santa Claus arrived")
a.deposit(50,"Santa Claus arrived")
a.deposit(50,"Santa Claus arrivedsdsds  ")
a.withdraw(23, "fuck tyou")
a.transfer(30, b)
a.transfer(30, b)
print(a.ledger)
# a.transfer(1, c)
# print(a.get_balance())
# print(b.get_balance())
# print(c.get_balance())
# print(b.ledger)
print(a)
# def create_spend_chart(categories):

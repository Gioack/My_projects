class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.ledger = list()

    def __repr__(self):
        self.items = ""
        self.nameCopy = self.name
        while len(self.nameCopy) <= 30:
            self.nameCopy = "*" + self.nameCopy + "*"
        for x in range(len(self.ledger)):
            while len(self.ledger[x]["description"]) <= 23:
                self.ledger[x]["description"] = self.ledger[x]["description"] + " "
            while len(str(self.ledger[x]["amount"])) <= 7:
                self.ledger[x]["amount"] = " " + str(self.ledger[x]["amount"])
            self.items = self.items + (self.ledger[x]["description"][:24] + self.ledger[x]["amount"][:8] + "\n")
        return self.nameCopy + "\n" + self.items + "Total: " + str(self.balance)
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
# a.transfer(1, c)
# print(a.get_balance())
# print(b.get_balance())
# print(c.get_balance())
# print(b.ledger)
# print(a)
# print(b)
# print(c)
def create_spend_chart(Categories_list):
    Footer = ""
    count = 0
    for Category in Categories_list:
        if Footer == "":
            for Letter in Category.name:
                Footer = Footer + "    " + Letter + "\n"
        else:
            Footer = Footer.split("\n")
            for Letter in Category.name:
                if Category.name.index(Letter) > len(Footer):
                    while len(Letter) <= len(Footer[1]):
                        Letter = " " + Letter
                    Footer.append(Letter)
                else:
                    Footer[Category.name.index(Letter)] = Footer[Category.name.index(Letter)] + " " + Letter
            Footer = Footer.join("\n")
    print(Footer)
        # for Letter in Category:
create_spend_chart([a, b, c])

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
b = Category("dddddddddddd")
c = Category("ffffffffffff")
d = Category("wwwwwwwwwwwww")
e = Category("hhhhhhhhhhhhhhhhh")
a.deposit(50,"Santa Claus arrived")
a.deposit(50,"Santa Claus arrived")
a.deposit(50,"Santa Claus arrivedsdsdswwwwwwww")
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
    Dashes = "   "
    for Category in Categories_list:
        Index = 0
        # THIS CREATES THE FOOTER OF OUR FINAL STRING
        if Footer == "":
            for Letter in Category.name:
                Footer = Footer + "    " + Letter + "\n"
        else:
            Footer = Footer.rstrip().split("\n")
            for Letter in Category.name:
                if Index <= (len(Footer)-1):
                    Footer[Index] = Footer[Index] + "  " + Letter
                elif Index > len(Footer)-1:
                    while len(Letter) < len(Footer[0]):
                        Letter = " " + Letter
                    Footer.append(Letter)
                Index = Index + 1
            Footer = "\n".join(Footer)
    while len(Dashes) <= (len(Footer.split("\n")[0])+ 1):
         Dashes = Dashes + "-"
    Footer = Dashes + "\n" + Footer
    Graph_bar = ""
    # The following crates Graph_bar
    for x in range(1,10):
        Graph_bar = " " + str(x*10) + "|" + "\n" + Graph_bar
    Graph_bar = "100|" + "\n" + Graph_bar
    Graph_bar = Graph_bar.split("\n")
    for each_number in Graph_bar:
        if each_number[:3].strip() < difference:
             each_number = each_number + "  o"
    print(Graph_bar)

create_spend_chart([a, b, c, d, e])

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
            while len(str(float(self.ledger[x]["amount"]))) <= 7:
                self.ledger[x]["amount"] = " " + str(self.ledger[x]["amount"])
            self.items = self.items + (self.ledger[x]["description"][:24] + self.ledger[x]["amount"][:8] + "\n")
        return self.nameCopy + "\n" + self.items + "Total: " + str(self.balance)
    def deposit(self, amount, description= ""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.balance + amount
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        return True
    def withdraw(self, amount, description= ""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": - amount, "description": description})
            self.balance = self.balance - amount
            return True
        else:
            return False
    def transfer(self, amount, destination):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "transfer from " + self.name)
            return True
        return False
    def get_balance(self):
        return self.balance
    def Percentage_spent(self):
        Alldeposited = 0
        Allwithdrawed = 0
        ### DECIDE WHAT TO DO IF EMPTY
        for DicTransaction in self.ledger:
            if float(DicTransaction["amount"]) > 0:
                Alldeposited = Alldeposited + float(DicTransaction["amount"])
            elif float(DicTransaction["amount"]) <= 0:
                Allwithdrawed = abs(Allwithdrawed + float(DicTransaction["amount"]))
        Percentage = round((Allwithdrawed*100)/Alldeposited)
        return Percentage

a = Category("food")
b = Category("dddddddddddd")
c = Category("ffffffffffff")
d = Category("wwwwwwwwwwwww")
e = Category("hhhhhhhhhhhhhhhhh")
a.deposit(50,"Santa Claus arrived")
a.withdraw(50, "fuck tyou")
b.deposit(50,"Santa Claus arrived")
b.withdraw(10, "fuck tyou")
c.deposit(50,"Santa Claus arrived")
c.withdraw(40, "fuck tyou")
d.deposit(50,"Santa Claus arrived")
d.withdraw(10, "fuck tyou")

# a.transfer(1, c)

# print(b.get_balance())
# print(c.get_balance())
# print(a)
# print(b)
# print(c)
def create_spend_chart(Categories_list):
    Footer = ""
    Dashes = "    "
    for Category in Categories_list:
        Index = 0
        # THIS CREATES THE FOOTER OF OUR FINAL STRING
        if Footer == "":
            for Letter in Category.name:
                Footer = Footer + "     " + Letter + "\n"
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
    # Graph_bar = ""
    # The following crates Graph_bar COULD LIKE SO BETTER WITH LIST COMPREHENSION
    # for x in range(1,10):
    #     Graph_bar = " " + str(x*10) + "|" + "\n" + Graph_bar
    # Graph_bar = "100|" + "\n" + Graph_bar
    # Graph_bar = (Graph_bar.split("\n"))
    # Graph_bar.pop
    Graph_bar = [" " + str(x*10) + "|" if not x == 10 else "100|" for x in range(1,11)]
    # Graph_bar.append("100|")
    Graph_bar.reverse()
    print(Graph_bar)
    Isfirst = True
    for Category in Categories_list:
        for number in range(len(Graph_bar)):
            number_well_set = int(Graph_bar[number][:3].strip())
            if number_well_set <= Category.Percentage_spent(): #### CREATE DIFFERENCE
                if Isfirst == True:
                    Graph_bar[number] = Graph_bar[number] + " o"
                else:
                    Graph_bar[number] = Graph_bar[number] + "  o"
            else:
                if Isfirst == True:
                    Graph_bar[number] = Graph_bar[number] + "  "
                else:
                    Graph_bar[number] = Graph_bar[number] + "   "
        Isfirst = False
    Graph_bar = "\n".join(Graph_bar)
    Final_result = "Percentage spent by category\n" + Graph_bar +"\n"+ Footer
    return Final_result
print(create_spend_chart([a, b,c,d]))

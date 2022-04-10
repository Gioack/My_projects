## python Budget_app.py
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.Alldeposited = 0
        self.Allwithdrawn = 0
    def __repr__(self):
        self.items = ""
        self.nameCopy = self.name
        while len(self.nameCopy) <= 28:
            self.nameCopy = "*" + self.nameCopy + "*"
        for Index, Transaction in enumerate(self.ledger):
            final_row = ""
            for key,value in Transaction.items():
                if key == "description":
                    while len(value) <= 22:
                        value = value + " "
                    final_row = value[:23] + final_row
                elif key == "amount":
                    value = str("{:.2f}".format(value))
                    while len(str(value)) <= 6:
                        value = " " + str(value)
                    final_row = value[:7]
            self.items = self.items + final_row + "\n"
# If you don't want to create a copy of leger, you can destroy it and add the following code.
        # for Dictionary in self.ledger:
        #     Dictionary["description"] = Dictionary["description"].strip()
        #     if Dictionary["amount"][-3:] == ".00":
        #         Dictionary["amount"] = int(Dictionary["amount"][:-3].strip())
        #     else:
        #         Dictionary["amount"] = float(Dictionary["amount"].strip())
        balance = self.get_balance()
        return self.nameCopy + "\n" + self.items + "Total: " + "{:.2f}".format(balance)
    def deposit(self, amount, description= ""):
        self.ledger.append({"amount": amount, "description": description})
        self.Alldeposited = self.Alldeposited+ amount
    def check_funds(self, amount):
        if float(amount) > self.Alldeposited:
            return False
        return True
    def withdraw(self, amount, description= ""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            self.Allwithdrawn = self.Allwithdrawn + amount
            return True
        else:
            return False
    def transfer(self, amount, destination):
        if self.check_funds(amount) == True:
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        return False
    def get_balance(self):
        self.balance = self.Alldeposited - self.Allwithdrawn
        return self.balance
    def Percentage_spent(self):
        Percentage = round(((self.Allwithdrawn*100)/self.Alldeposited),-1)
        return Percentage
def create_spend_chart(Categories_list):
    Footer = ""
    Dashes = "    "
    for Category in Categories_list:
        # THIS CREATES THE FOOTER OF OUR FINAL STRING
        if Footer == "":
            for Letter in Category.name:
                Footer = Footer + "     " + Letter + "\n"
        else:
            Footer = Footer.rstrip().split("\n")
              #rstrip is here for eliminating the empty element that would be created
            for Index,Letter in enumerate(Category.name):
                if Index == 0:
                    Footer[Index] = Footer[Index] + "  " + Letter.strip()
                elif Index > 0:
                # the following covers 2 Scenarios:
                # scenario where the word is not the longest
                    if Index <= len(Footer)-1:
                        Footer[Index] = Footer[Index] + "  " + Letter
                        # the following covers the case when it's longer than the previous one but not the longest one
                        while len(Footer[Index]) < len(Footer[0]):
                            Footer[Index] = Footer[Index][:-1]+ " " + Footer[Index][-1]
                # scenario where the word is the longest word so far
                    else:
                        while len(Letter) < len(Footer[0]):
                            Letter = " " + Letter
                        Footer.append(Letter)
            Footer = "\n".join(Footer)
    while len(Dashes) <= (len(Footer.split("\n")[0])+ 1):
         Dashes = Dashes + "-"
    Footer = Dashes + "\n" + Footer
# this creates the Upper part of graphs
    Graph_bar = [" " + str(x*10) + "|" if not x == 10 else "100|" for x in range(1,11)]
    Graph_bar.reverse()
    Graph_bar.append("  0|")
    Isfirst = True
    for Category in Categories_list:
        for number,value in enumerate(Graph_bar):
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
# THINGS THAT CREATE CLASSES
a = Category("dsfdsfsdef")
b = Category("Food")
c = Category("Business")
d = Category("wwwwwww")
e = Category("hhhhh")
f = Category("sdsda")
g = Category("hhhhhhhh")
a.deposit(50,"Santa Claus arrived")
a.withdraw(12.5, "Thiefs arrived")
b.deposit(100,"Santa Claus arrived")
b.withdraw(70, "Thiefs arrived")
c.deposit(100,"Santa Claus arrived")
c.withdraw(20, "Thiefs arrived")
d.deposit(30,"Santa Claus arrived")
d.withdraw(10, "Thiefs arrived")
e.deposit(30,"Santa Claus arrived")
e.withdraw(10, "Thiefs arrived")
f.deposit(30,"Santa Claus arrived")
f.withdraw(29, "Thiefs arrived")
g.deposit(30,"Santa Claus arrived")
g.withdraw(10, "Thiefs arrived")
print(create_spend_chart([a, b, c, d, e, f, g]))
# Their_version = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
# print(Their_version)

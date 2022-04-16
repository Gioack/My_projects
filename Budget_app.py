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
            self.nameCopy = f"*{self.nameCopy}*"
        for Index, Transaction in enumerate(self.ledger):
            final_row = ""
            for key,value in Transaction.items():
                if key == "description":
                    while len(value) <= 22:
                        value += " "
                    final_row = f"{value[:23]}{final_row}"
                elif key == "amount":
                    value = str("{:.2f}".format(value))
                    while len(str(value)) <= 6:
                        value = f" {value}"
                    final_row = value[:7]
            self.items = f"{self.items}{final_row}\n"
# If you don't want to create a copy of leger, you can destroy it and add the following code.
        # for Dictionary in self.ledger:
        #     Dictionary["description"] = Dictionary["description"].strip()
        #     if Dictionary["amount"][-3:] == ".00":
        #         Dictionary["amount"] = int(Dictionary["amount"][:-3].strip())
        #     else:
        #         Dictionary["amount"] = float(Dictionary["amount"].strip())
        balance = "{:.2f}".format(self.get_balance())
        return f"{self.nameCopy}\n{self.items}Total: {balance}"
    def deposit(self, amount, description= ""):
        self.ledger.append({"amount": amount, "description": description})
        self.Alldeposited += amount
    def check_funds(self, amount):
        if float(amount) > self.Alldeposited:
            return False
        return True
    def withdraw(self, amount, description= ""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            self.Allwithdrawn += amount
            return True
        else:
            return False
    def transfer(self, amount, destination):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
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
                Footer = f"{Footer}     {Letter}\n"
        else:
            Footer = Footer.rstrip().split("\n")
              #rstrip is here for eliminating the empty element that would be created
            for Index,Letter in enumerate(Category.name):
                if Index == 0:
                    Footer[Index] = f"{Footer[Index]}  {Letter.strip()}"
                elif Index > 0:
                # the following covers 2 Scenarios:
                # scenario where the word is not the longest
                    if Index <= len(Footer)-1:
                        Footer[Index] +=  f"  {Letter}"
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
         Dashes += "-"
    Footer = f"{Dashes}\n{Footer}"
# this creates the Upper part of graphs
    Graph_bar = [(f'{" "*(3-len(str(x*10)))}{x*10}|') for x in reversed((range(11)))]
    Isfirst = True
    for Category in Categories_list:
        for number,value in enumerate(Graph_bar):
            number_well_set = int(Graph_bar[number][:3].strip())
            if number_well_set <= Category.Percentage_spent(): #### CREATE DIFFERENCE
                if Isfirst == True:
                    Graph_bar[number] += " o"
                else:
                    Graph_bar[number] += "  o"
            else:
                if Isfirst == True:
                    Graph_bar[number] += "  "
                else:
                    Graph_bar[number] += "   "
        Isfirst = False
    Graph_bar = "\n".join(Graph_bar)

    Final_result = f"Percentage spent by category\n{Graph_bar}\n{Footer}"
    return Final_result
# THINGS THAT CREATE CLASSES
Leonardo_da_Vinci = Category("Leo")
Michelangelo = Category("Micky")
Pablo_Picasso = Category("Pablo")
Vincent_van_Gogh = Category("van Gogh")
Leonardo_da_Vinci.deposit(50,"Sold Monna Lisa")
Leonardo_da_Vinci.withdraw(10, "I need to pay Fines because I was too lazy and I didn't respect my expiry dates")
Michelangelo.deposit(100,"Sold David")
Michelangelo.withdraw(70, "Bought a shower")
Pablo_Picasso.deposit(100,"Sold Les Demoiselles d'Avignon")
Pablo_Picasso.transfer(90, Vincent_van_Gogh)
Vincent_van_Gogh.deposit(0.01,"I sold a painting!")
Vincent_van_Gogh.withdraw(0.01, "It was a joke I didn't")
print(Michelangelo)
print(Vincent_van_Gogh)
print(create_spend_chart([Leonardo_da_Vinci, Michelangelo, Pablo_Picasso, Vincent_van_Gogh]))
# Their_version = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
# print(Their_version)

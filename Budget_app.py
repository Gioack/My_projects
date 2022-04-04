## python Budget_app.py
class Category:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.ledger = list()

    def __repr__(self):
        Copy_ledger = self.ledger[:]
        self.items = ""
        self.nameCopy = self.name
        # print(self.ledger)
        while len(self.nameCopy) <= 28:
            self.nameCopy = "*" + self.nameCopy + "*"
        for x in range(len(Copy_ledger)):
            while len(Copy_ledger[x]["description"]) <= 22:
                Copy_ledger[x]["description"] = Copy_ledger[x]["description"] + " "
            Copy_ledger[x]["amount"] = "{:.2f}".format(Copy_ledger[x]["amount"])
            while len(str(Copy_ledger[x]["amount"])) <= 6:
                Copy_ledger[x]["amount"] = " " + str(Copy_ledger[x]["amount"])
            self.items = self.items + (Copy_ledger[x]["description"][:23] + Copy_ledger[x]["amount"][:7] + "\n")
        for Dictionary in self.ledger:
            Dictionary["description"] = Dictionary["description"].strip()
            if Dictionary["amount"][-3:] == ".00":
                Dictionary["amount"] = int(Dictionary["amount"][:-3].strip())
            else:
                Dictionary["amount"] = float(Dictionary["amount"].strip())
        # print(self.ledger)
        return self.nameCopy + "\n" + self.items + "Total: " + "{:.2f}".format(self.balance)
    def deposit(self, amount, description= ""):
        try:
            int(amount)
        except:
            float(amount)
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.balance + float(amount)
    def check_funds(self, amount):
        if float(amount) > self.balance:
            return False
        return True
    def withdraw(self, amount, description= ""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance = self.balance - float(amount)
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
        Percentage = round(((Allwithdrawed*100)/Alldeposited),-1)
        return Percentage

a = Category("Business")
b = Category("Food")
c = Category("Entertainment")
d = Category("wwwwwww")
e = Category("hhhhhhhhhhhhhhhhh")
a.deposit(50,"Santa Claus arrived")
# a.withdraw(12.5, "fuck tyou")
b.deposit(100,"Santa Claus arrived")
b.withdraw(70, "fuck tyou")
c.deposit(100,"Santa Claus arrived")
c.withdraw(20, "fuck tyou")
d.deposit(30,"Santa Claus arrived")
d.withdraw(10, "fuck tyou")
# print(a.Percentage_spent())
# print(b)
# print(c.Percentage_spent())
# print(d.Percentage_spent())
def create_spend_chart(Categories_list):
    Footer = ""
    Dashes = "    "
    # List_of_Category_names = list()
    for Category in Categories_list:
        Index = 0
        # THIS CREATES THE FOOTER OF OUR FINAL STRING
        if Footer == "":
            for Letter in Category.name:
                Footer = Footer + "     " + Letter + "\n"
        else:
            Footer = Footer.rstrip().split("\n")
            for Letter in Category.name:
                # if Index <= (len(List_of_Category_names[-1])-1):
                #     Footer[Index] = Footer[Index] + "  " + Letter
                # elif Index > len(List_of_Category_names[-1])-1:
                #     while len(Letter) < len(Footer[0]):
                #         Letter = " " + Letter
                #     Footer.append(Letter)
                # Index = Index + 1
            # Footer = "\n".join(Footer)
                if Index == 0:
                    # print(Letter.replace(" ","sd"))
                    Footer[Index] = Footer[Index] + "  " + Letter.strip()
                    # print(Letter.replace(" ","sd"))
                elif Index > 0:
                # it's the longest word, it's not the longest but it's longer than the previous one
                    if Index <= len(Footer)-1:
                        Footer[Index] = Footer[Index] + "  " + Letter
                        while len(Footer[Index]) < len(Footer[0]):
                            Footer[Index] = Footer[Index][:-1]+ " " + Footer[Index][-1]
                    else:
                        while len(Letter) < len(Footer[0]):
                            Letter = " " + Letter
                        Footer.append(Letter)
                Index = Index + 1
            Footer = "\n".join(Footer)
        # List_of_Category_names.append(Category.name)

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
    Graph_bar.append("  0|")
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
    #   for item in Graph_bar:

    Graph_bar = "\n".join(Graph_bar)
    Final_result = "Percentage spent by category\n" + Graph_bar +"\n"+ Footer
    print(Final_result.split("\n"))
    return Final_result
# create_spend_chart([a, b,c,d])
Their_version = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
create_spend_chart([a, b,c])
print(Their_version.split("\n"))

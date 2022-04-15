# python Time_Calculator.py
from tkinter import *
root = Tk()
root.title("Time_Calculator")
root.configure(bg = "Black")
root.geometry("1366x768")
Result_Gui = Label(root)
def add_time(start, duration, day_started = ""):
    Days_of_Week=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    IsAM = False
    Days_after = 0
    # AM is Default
    if "PM" in start:
        start = start.replace("PM", "")
    else:
        start = start.replace("AM", "")
        IsAM = True
    start = [int(x) for x in start.split(":")]
    duration = [int(x) for x in duration.split(":")]
    ResultMinutes = (start[1] + duration[1]) % 60
    Hours_to_add_from_Minutes = (start[1] + duration[1] - ResultMinutes) / 60
    Hours_to_add = duration[0] + Hours_to_add_from_Minutes
    while Hours_to_add > 0:
        start[0] = start[0] + 1
        Hours_to_add = Hours_to_add - 1
        if (start[0] == 12) and (IsAM == True):
            IsAM = False
        elif (start[0] == 12) and (IsAM == False):
            IsAM = True
            Days_after = Days_after + 1
        if (start[0] > 12):
            start[0] = start[0] - 12
    if ResultMinutes < 10:
        ResultMinutes = f"0{ResultMinutes}"
    Result = f"{start[0]}:{ResultMinutes}"
    if IsAM == True:
        Result = f"{Result} AM"
    else:
        Result = f"{Result} PM"
    if day_started != "":
        Number_start_day = Days_of_Week.index(day_started[0].upper() + day_started[1:].lower())
        Day_it_ends = Days_after + Number_start_day
        while Day_it_ends > 6:
            Day_it_ends = Day_it_ends - 7
        Result = f"{Result}, {Days_of_Week[Day_it_ends]}"
    if Days_after == 1:
        Result = f"{Result} (next day)"
    if Days_after >= 2:
        Result = f"{Result} ({Days_after} days later)"
    global Result_Gui
    Result_Gui.destroy()
    Result_Gui = Label(root,text=Result, bg="Black",
                fg="White",font=("Bold",32),pady=80)
    Result_Gui.grid(row=6, column=1)
    return Result
Header = Label(root,padx=1,pady=10, bg="black")
Header.grid(row=0,column=1)
Instruction_left = Label(root, text="Write the starting time below:",font=("Bold",21))
Instruction_left.grid(row=1,column=0)
Starting_time = Entry(root, bg = "grey", fg="white", font=("Bold",23))
Starting_time.grid(row=2,column=0,padx=50)
thing_that_makes_all_more_separated = Label(root,padx=250,pady=100, bg="black")
thing_that_makes_all_more_separated.grid(row=6,column=1)
Instruction_right = Label(root, text="Write the hours to add below:",font=("Bold",21))
Instruction_right.grid(row=4,column=0)
Hours_to_add = Entry(root,bg = "grey", fg= "white",font=("Bold",23))
Hours_to_add.grid(row=5,column=0,padx=50)
Day_starting_Instuction = Label(root, text="Name of starting day:(optional)", font=("Bold",15))
Day_starting_Instuction.grid(row=7,column=0)
Day_starting = Entry(root,bg = "grey", fg= "white",font=("Bold",23))
Day_starting.grid(row=8,column=0,padx=50)
Calculate = Button(root, text="Calculate", padx=120, bg = "#36454F"
                    , fg= "white",pady=42,font=("Bold",33),
                    command=lambda: add_time(Starting_time.get(), Hours_to_add.get(),Day_starting.get()))
Calculate.grid(row=2,column=1)
root.mainloop()
# print(add_time("7:47 PM", "400:35"))

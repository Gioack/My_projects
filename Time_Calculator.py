def add_time(start, duration, day_started = ""): # 9:00 PM 3
    Days_of_Week=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    IsAM = ""
    Days_after = 0
    if "AM" in start:
        start = start.replace("AM", "")
        IsAM = True
    else:
        start = start.replace("PM", "")
        IsAM = False
    start = start.split(":")
    duration = duration.split(":")
    ResultMinutes = (int(start[1]) + int(duration[1])) % 60
    Hours_to_add_from_Minutes = ((int(start[1]) + int(duration[1])) - ResultMinutes) / 60
    Hours_to_add = int(duration[0]) + int(Hours_to_add_from_Minutes) #"11:55 PM", "24:08"
    start[0] = int(start[0])
    while Hours_to_add > 0:
        print(start[0])
        start[0] = start[0] + 1
        Hours_to_add = Hours_to_add - 1
        if (start[0] == 12) and (IsAM == True):
            IsAM = False
        elif (start[0] == 12) and (IsAM == False):
            IsAM = True
            Days_after = Days_after + 1
            print("Days_after" , Days_after)
        if (start[0] > 12):
            start[0] = start[0] - 12
    start[0] = str(start[0])
    if ResultMinutes < 10:
        ResultMinutes = "0" + str(ResultMinutes)
    Result =str(start[0]) + ":" + str(ResultMinutes)
    if IsAM == True:
        Result = Result + " AM"
    else:
        Result = Result + " PM"
    if day_started != "":
        Number_start_day = Days_of_Week.index(day_started[0].upper() + day_started[1:].lower())
        Day_it_ends = Days_after + Number_start_day
        while Day_it_ends > 6:
            Day_it_ends = Day_it_ends - 7
        Result = Result + ", " + Days_of_Week[Day_it_ends]
    if Days_after == 1:
        Result = Result + " (next day)"
    if Days_after >= 2:
        Result = Result + " (" + str(Days_after) + " days later)"

    return Result

print(add_time("11:59 PM", "24:05", "Wednesday"))

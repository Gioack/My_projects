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
    ResultHour = (int(start[0]) + int(duration[0]) + int(Hours_to_add_from_Minutes)) #"11:55 PM", "24:08"
    ResultHour_Copy = ResultHour
    if IsAM is True:
        while (ResultHour_Copy / 24) > 1:
            Days_after = Days_after + 1
            ResultHour_Copy = ResultHour_Copy - 24
    else:
        if ResultHour < 12:
            Days_after = 0
        elif (((ResultHour/24) / 12) > 1) or ((12 - int(start[0]) < 1)):
            ResultHour_Copy = ResultHour_Copy - (12 - int(start[0]))
            Days_after = 1
            IsAM = not IsAM
            while (ResultHour_Copy / 24) > 1:
                Days_after = Days_after + 1
                ResultHour_Copy = ResultHour_Copy - 24
        else:
            while (ResultHour_Copy / 24) > 1:
                Days_after = Days_after + 1
                ResultHour_Copy = ResultHour_Copy - 24
    while ResultHour > 12:
        ResultHour = ResultHour - 12
        IsAM = not IsAM
    if ResultMinutes < 10:
        ResultMinutes = "0" + str(ResultMinutes)
    Result =str(ResultHour) + ":" + str(ResultMinutes)
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


    # return new_time
print(add_time("11:10 PM", "48:10"))

calendar = []

calendar.append({
    "Day": "Monday",
    "Date": 1,
    "Activity": "Python Lab"
})

calendar.append({
    "Day": "Tuesday",
    "Date": 2,
    "Activity": "Data Structures"
})

calendar.append({
    "Day": "Wednesday",
    "Date": 3,
    "Activity": "DBMS"
})

calendar.append({
    "Day": "Thursday",
    "Date": 4,
    "Activity": "Statistics"
})

calendar.append({
    "Day": "Friday",
    "Date": 5,
    "Activity": "FDS Lab"
})

calendar.append({
    "Day": "Saturday",
    "Date": 6,
    "Activity": "Python Practice"
})

calendar.append({
    "Day": "Sunday",
    "Date": 7,
    "Activity": "Holiday"
})

print("Weekly Calendar")

for day in calendar:
    print("----------------------")
    print("Day:", day["Day"])
    print("Date:", day["Date"])
    print("Activity:", day["Activity"])

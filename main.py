from datetime import date, timedelta, datetime
def get_birthdays_per_week(users):
    if not users:
        return {}
    today = date.today()

    weekdays = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
    }
 
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday = birthday.replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        if not today <= birthday <= today + timedelta(days=7):
            continue

        if today <= birthday <= today + timedelta(days=7):
            day_week = birthday.weekday()
            if day_week == 5 or day_week == 6:
                weekdays["Monday"].append(name)
            elif day_week == 0:
                weekdays["Monday"].append(name)
            elif day_week == 1:
                weekdays["Tuesday"].append(name)
            elif day_week == 2:
                weekdays["Wednesday"].append(name)
            elif day_week == 3:
                weekdays["Thursday"].append(name)
            elif day_week == 4:
                weekdays["Friday"].append(name)
            else:
                return {}
        else:
            return {}
    users = {key: value for key, value in weekdays.items() if value}
    print(users)
    return users
  

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
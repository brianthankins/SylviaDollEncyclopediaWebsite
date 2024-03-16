from datetime import datetime, timedelta

def aboutmeage(month, day, year):
    # User Input (uncomment for user input)
    # birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    # birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

    # Predefined Date (uncomment for predefined date)
    birth_date = datetime(year=year, month=month, day=day)

    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    print(f"Your age is: {age}")
    return age

sylvia_age = aboutmeage(month=2, day=17, year=2017)
print(sylvia_age)
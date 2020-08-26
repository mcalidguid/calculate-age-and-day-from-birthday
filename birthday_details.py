from datetime import date
import datetime
import calendar


class BirthdayDetail:
    def find_day(self, birth_date):
        try:
            # Convert the user input to date() format
            born = datetime.datetime.strptime(birth_date, "%d%m%Y").date()
            day = born.weekday()
            name_of_day = calendar.day_name[day]
            print("You were born on", name_of_day)
        except ValueError:
            print("The entered date does not match the DDMMYYYY format.")

    def find_age(self, birth_date):
        try:
            # The number of days in a year
            days_in_year = 365.2425
            # Convert the user input to date() format
            born = datetime.datetime.strptime(birth_date, "%d%m%Y").date()
            # Subtract the date today to the date of birth then divide it to the exact number of days in a year
            age = int((date.today() - born).days / days_in_year)
            print("As of today, you are now", age, "years old.")
        except ValueError:
            print("Please try Again.")


day_dob = BirthdayDetail()
print("Enter your Birthday [DDMMYYY]: ")
user_input = input(">>>: ")
day_dob.find_day(user_input)
day_dob.find_age(user_input)

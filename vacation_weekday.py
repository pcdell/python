#1. Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a program that asks a
#     day number, and prints the day name (a string).
#2. You go on a wonderful holiday (perhaps to jail, if you don’t like happy exercises) leaving on day number 3
#     (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting
#     day number, and the length of your stay, and it will tell you the name of day of the week you will return on.

def weekday(day_number):

    if 0 <= int(day_number) <= 6:
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        day_name = days_of_week[int(day_number)]
        print("The day is", day_name)
    else:
        print("Invalid day number. Please enter a number between 0 and 6.")


def holiday(start, lenght):
    if 0 <= int(start) <= 6:
        day_week = (start + lenght) % 7
        weekday(day_week)
    else:
        print("Invalid day number to start. Please enter a number between 0 and 6.")


# Example usage:
start_day_input = int(input("Enter the starting day number (0-6): "))
holiday_length_input = int(input("Enter the length of your stay: "))

holiday(start_day_input, holiday_length_input)
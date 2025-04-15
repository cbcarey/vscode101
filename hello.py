from datetime import date



def say_hello(name):
    name = "Henry"
    print("Hello, " + name)

say_hello("VS Code")

def say_day_of_the_week(date):
    print("Today is " + date.strftime("%A"))

say_day_of_the_week(date.today())


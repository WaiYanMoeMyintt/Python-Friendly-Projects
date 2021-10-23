age  = input("Type your current age? ")
age_as_int = int(age)
years_remain = 90 - age_as_int
days_remain  = years_remain * 365
weeks_remain = years_remain * 52
months_remain  = years_remain * 12

message  = f"Your Have {days_remain} days, {months_remain}months, {years_remain} years left."
print(message)



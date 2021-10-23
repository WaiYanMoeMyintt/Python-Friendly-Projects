years = int(input("Enter a leap years: "))

if years % 4 == 0:
    print(f"This is a leap {years}  years")
    if years % 400 == 0:
        print(f"This is a leap {years} years")
    elif years % 4000 == 0:
         print(f"This is a leap {years} years")
elif years % 100:
      print(f"This is not a leap {years} years")
else:
      print(f"This is not a leap {years} years")

print("Welcome to the python pizza delivery")
pizza_size = input("What sizes do your want? S M OR L")
add_pepperoni = input("Do your want pepperoni Yes Or No")
extra_cheese = input("Do your want extra cheese Yes or NO")

bill = 0

if pizza_size == "S":
    bill+=15
elif pizza_size == "M":
    bill+=20
elif pizza_size =="L":
    bill+=25

else:
    bill+=0

if add_pepperoni == "Y":
    if pizza_size == "S":
        bill+=4
    else:
        bill+=3
if extra_cheese == "Y":
    bill+=1

print(f"Your Final bill is ${bill}")





print('''
                       $$$$$$$$$$$$$$$$$$$$$$$$$
                       $$$$$$$$$$$$$$$$$$$$$$$$$
                       $$$$$'`$$$$$$$$$$$$$'`$$$
                       $$$$$$  $$$$$$$$$$$  $$$$
                       $$$$$$$  '$/ `/ `$' .$$$$
                       $$$$$$$$. i  i  /! .$$$$$
                       $$$$$$$$$.--'--'   $$$$$$
                       $$^^$$$$$'        J$$$$$$
                       $$$   ~""   `.   .$$$$$$$
                       $$$$$e,      ;  .$$$$$$$$
                       $$$$$$$$$$$.'   $$$$$$$$$
                       $$$$$$$$$$$$.    $$$$$$$$
                       $$$$$$$$$$$$$     $by&TL$
                       -------------------------
                             I LOVE YOU
                       -------------------------
''')

print("Welcome to the Love Calculator")
partner_name1 = input("What is a your partner name \n")
partner_name2 = input("What is a your partner name \n ")

#solution below

combined_string = partner_name1 + partner_name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score  = int(str(love) + str(true))
if (love_score < 10) or (love_score > 90):
    print(f"your lover score is{love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love <=50):
    print(f"your score is{love_score}, your are alright together")
else:
    print(f"your score is {love_score}")



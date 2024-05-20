#If the bill was $150.00, split between 5 people, with 12% tip. 
print("welcome to the trip calculator")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
bill=float(input("what was the total bill"))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
tip=int(input("how much do you what to give a tip 10,12,15"))
#Write your code below this line 👇
spilt=int(input("how many people to spilt the bill"))
bill_with_tip=tip/100*bill+bill
print(bill_with_tip)
bill_per_person=bill_with_tip/spilt
print(bill_per_person)
final_amount=round(bill_per_person,2)
print(f"each person should pay {final_amount}")

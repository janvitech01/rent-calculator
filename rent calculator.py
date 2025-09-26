rent = int(input("Enter your hostel/ flat amount:"))
food = int(input("Enter your amount of food ordered:"))
elctricity_spend = int(input("enter the total of electricity spend="))
charege_per_unit =float(input("enter the charge per unit = "))
persons = int(input("enter the numbers of persons living in the flat/hostel = "))

Total_bill = rent + food + elctricity_spend
total_units = elctricity_spend / charege_per_unit
per_person_rent = rent / persons
per_person_food = food / persons
per_person_electricity = elctricity_spend / persons 
output = (food + rent + Total_bill) // persons


print("Total bill is:", Total_bill)
print("Total units consumed:", total_units) 
print("Each person has to pay:" , output)
print("Rent:", per_person_rent)
print("Food:", per_person_food)
print("Electricity:", per_person_electricity)

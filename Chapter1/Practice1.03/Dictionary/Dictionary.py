phoneNumber = {"Alfred" : "010-1234-5678", "Hedvik" : "011-5678-8765", "Ida" : "017-2468-3456"}
people = ["Alfred", "Hedvik", "Ida"]

print("1st printing : Phone Numbers!")
for i in people :
	print(f"{i} : {phoneNumber[i]}")

people.append("Dennis")
phoneNumber[people[-1]] = "019-9876-5432"

print("2nd printing : A new man\'s phone information!")
print(phoneNumber)

del phoneNumber["Hedvik"]

print("3rd printing : Updating Phone Numbers!")
print(phoneNumber)

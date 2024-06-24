clothPrice = {"Onepiece" : 2000, "Pants" : 2500, "Sweater" : 3000, "Shirt" : 2500, "Jeans" : 2000, "Skirt" : 2500}
cloth = ["Onepiece", "Pants", "Sweater", "Shirt", "Jeans", "Skirt"]
total_sum = 0

while True :
	shopping = input("Do you keep shopping? : ")

	if ((shopping == 'Y') or (shopping == 'y')) :
		print("You can buy these clothes below!")

		for i in range(0, 6) :
			print(f"{cloth[i]} : {clothPrice[cloth[i]]}")
		whatCloth = str(input("what cloth do you want? : "))
		total_sum += clothPrice[whatCloth]
		print(f"Til now, total price is {total_sum}.")
	elif ((shopping == 'N') or (shopping == 'n')) :
		break;
	else :
		print("Please enter appropriately.")

print(f"Your total price for your cloth is {total_sum}.")

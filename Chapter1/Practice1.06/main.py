from HanoiTower import *

print("According to a legend, there are 3 pillars in Hanoi, Vietnam.")
print("In most left pillar, there are some discs. And they have to be carried to most right pillar.")
print("How many times do people have to carry discs? You want to know that strongly, right?")
movingCount = int(input("Then enter a number that will be total moving count. You will know that! : "))
Hanoi_carry(movingCount, "LeftPillar", "Middle Pillar", "Right Pillar")
print(f"The total moving count is {MovingCount_get(movingCount)}.")

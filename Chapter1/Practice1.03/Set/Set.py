A = {3, 6, 9, 12, 15, 18, 21, 27, 30}

print("1st printing : First A.")
print(A)

A.add(24)

print("2nd printing : Second A adding a member.")
print(A)

B = {4, 8, 12, 16, 20, 24, 28, 32, 36, 40}

print("3rd printing : First B.")
print(B)

print("4th printing : The union set between A and B.")
print(A.union(B))

print("5th printing : The intersection between A and B.")
print(A.intersection(B))

A.discard(30)
A.discard(15)

print("6th printing : Third A without 15 multiples.")
print(A)

B.remove(20)
B.remove(40)

print("7th printing : Second B without 20 multiples.")
print(B)

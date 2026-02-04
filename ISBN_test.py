isbn = "0306401652"
total = 0
counter = 0
for i in isbn[: -1]:
    i = int(i)
#    print(i)
    total += int(i) * (10-counter)
    counter += 1

counter = 0
print(total)
while total % 11 != 0:
    total += 1
    counter += 1
print(total)
if isbn[-1] == "X":
    if counter == 10:
        print("Valid")
    else:
        print("Invalid")
else:
    if counter == int(isbn[-1]):
        print("Valid")
    else:
        print("Invalid")
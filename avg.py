score_sum = []
# asks for the score 3 times
# appends the input to the list
for i in range(1, 4):
    num = float(input(f"Enter score {i}: "))
    score_sum.append(num)
# sums all the elements of the list
avg = sum(score_sum) / 3

print(f"Their Average: {avg:.2f}")

if 95 <= avg <= 100:
    print("Excellent")
elif 86 <= avg < 95:
    print("Satisfactory")
elif 80 <= avg < 86:
    print("Fair")
elif 75 <= avg < 80:
    print("Poor")
elif 60 <= avg < 75:
    print("Failed")




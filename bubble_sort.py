num = [10, 2, 12, 14, 6, 8, 4]

print("="*100)
print (f"List: {num}")
print("="*100)
print()


for i in range(len(num)):
    swapped = False
    print("="*100)
    print(f"LOOP {i+1}")
    print("="*100)
    for j in range(len(num)-i-1):
        print(f"\tOld List: {num}")
        print(f"\tnum[j] = {num[j]}, num[j+1] = {num[j+1]}")
        print(f"\tComparing: {num[j]} and {num[j+1]}")
        if num[j] > num[j+1]:
            print(f"\t{num[j]} is greater than {num[j+1]}")
            print(f"\tSwapping: {num[j]} and {num[j+1]}")
            num[j], num[j+1] = num[j+1], num[j]
            print(f"\tNew List: {num}\n")
            swapped = True
        else:
            print(f"\t{num[j]} is not greater than {num[j+1]}")
            print(f"\tNew List: {num}\n")
    if not swapped:
        break

print(f"Sorted List: {num}")
print("="*100)

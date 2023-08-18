while True:
    fuel = {
        "DIESEL":55, # Diesel
        "UNLEADED":60, # Unleaded
        "PREMIUM":62  # Premium
        }
    
    gas_cost = 0

    print("\nCrumbz's Gas Station v1.0")
    for num, (key, value) in enumerate(fuel.items(), 1):
        print(f"{num} - {key}(P{value:.2f})")

    gas_type = input("\nEnter what to fill[DIESEL, UNLEADED, PREMIUM]: ").upper()

    while gas_type not in fuel.keys():
        print("Invalid input! Please only enter [DIESEL, UNLEADED, PREMIUM]")
        gas_type = input("\nEnter what to fill[DIESEL, UNLEADED, PREMIUM]: ").upper()

    gas_cost = fuel.get(gas_type.upper())

    fuel = int(input("Enter how much to fill: "))
    
    while fuel <= 0:
        print("Invalid input! Please enter a positive number!")
        fuel = int(input("Enter how much to fill: "))


    liter = fuel / gas_cost

    print(f"{fuel} fuel = {liter:.2f} liters")

    cash = int(input("Cash Tendered: "))
    
    while cash <= 0:
        print("Invalid input! Please enter a positive number!")
        cash = int(input("Cash Tendered: "))

    liter_cost = liter * gas_cost

    print(f"Your Change: P{(cash-liter_cost):.2f}")

    exit = input("Transact Again?[Y/N]: ").upper()

    while exit not in "YN":
        print("Invalid input! Please only enter [Y]/[N]!")
        exit = input("Transact Again?[Y/N]: ").upper()

    if exit == "N":
        print("Thank you for using our services!")
        break



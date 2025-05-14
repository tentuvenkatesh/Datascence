bill1 = float(input("enter total bill: "))
tip = int(input("How much percentage tip you want: "))
bill2 = bill1 * tip/100
total_bill = bill1+ bill2
num_per = int(input("how many persons want to share: "))
per_head = total_bill/num_per
print(f"each person has to pay {per_head}")
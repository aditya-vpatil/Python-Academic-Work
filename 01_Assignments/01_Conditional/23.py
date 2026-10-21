'''Calculate electricity bill based on units consumed'''


units = float(input("Enter units: "))
if units <= 1000:
    bill = units * 15 
print(f"Total bill:{bill}")

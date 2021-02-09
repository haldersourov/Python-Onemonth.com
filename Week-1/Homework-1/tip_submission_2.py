# One Month Python Week 1 Assignment

# Aternative way for submission 1
# Write a script that takes a dollar amount and recommennds a tip (15%, 18% and 20%)

total = float(input("What is you're bill sub-total? ").strip('$'))

tip_15 = total * 0.15
tip_18 = total * 0.18
tip_20 = total * 0.20

print("Tip Suggestions:")
print("----------------")
print(f"15% is ${tip_15:.2f}")
print(f"18% is ${tip_18:.2f}")
print(f"20% is ${tip_20:.2f}")
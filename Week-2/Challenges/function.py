# Create a function called uppercase_and_reverse that takes a little bit of text
# Uppercases it all, and then reverses it (flips all the letters around).

# >>> uppercase_and_reverse("Do not go gentle into that good night.")
# "THGIN DOOG TAHT OTNI ELTNEG OG TON OD"

def uppercase_and_reverse(text):
    return reverse(text.upper())
    
def reverse(text):
    return text [::-1]

print(uppercase_and_reverse("banana"))

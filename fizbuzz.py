# Fizz Buzz using a dictionary April, 9, 2020

n = 100  # Values to run through
vals = {"Fiz": 3, "Buzz": 5, "Bizz": 7, "Fuz": 8}  # Define multiples to be used

for i in range(1, n+1):
    out = ""
    for key in vals:
        if i % vals[key] == 0:
            out += key
    if not out:
        out = str(i)
    print(out)

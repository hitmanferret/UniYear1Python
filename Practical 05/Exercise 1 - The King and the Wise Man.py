square = 1
m = 1
total = 0

for i in range(64):
    rice = m * 30
    m = m * 2
    total += rice
    print("On square", (i + 1), "he will receive", rice, "mg of rice.")
print("Total amount of rice:", total, "mg")

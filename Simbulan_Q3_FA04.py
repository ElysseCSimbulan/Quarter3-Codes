names = ["Me", "Lia", "Jake"]
steps = [
    (4500, 5200, 4800, 5000, 5300),
    (4000, 4100, 3900, 4200, 4600),
    (6000, 5800, 5900, 6100, 6200)
]

total_steps = []
for person in steps:
    total_steps.append(sum(person))

highest = max(total_steps)
lowest = min(total_steps)

index = total_steps.index(highest)
highest_person = names[index]

for i in range(len(names)):
    print(f"{names[i]} total steps: {total_steps[i]}")

print(f"\nPerson with highest total steps: {highest_person}")
print(f"Difference between highest and lowest total: {highest - lowest}")
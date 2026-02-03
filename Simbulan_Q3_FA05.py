names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    (4500, 5200, 4800, 5000, 5300),
    (4000, 4100, 3900, 4200, 4600),
    (6000, 5800, 5900, 6100, 6200)
]

daily = []

for day in range(len(days)):
    total = 0
    for person in range(len(steps)):
        total += steps[person][day]
    daily.append(total)

for i in range(len(days)):
    print(f"{days[i]} total steps: {daily[i]}")

active = days[daily.index(max(daily))]
print(f"\nMost active day overall: {active}")
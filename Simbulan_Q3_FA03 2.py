prices = [
  [90, 30, 75],     // Gaisano Mall
  [110, 35, 55],    // SM City
  [100, 45, 60]     // Abreeza Mall
]

for i from 0 to 2:
    row_total = prices[i][0] + prices[i][1] + prices[i][2]
    row_average = row_total / 3
    print(prices[i])
    print("Total:", row_total, "Average:", row_average)
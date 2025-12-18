#Problem 1: Transaction Frequency Analyzer

transactions = [200, 500, 200, 100, 500, 200, 100, 500, 500]

# Count frequencies
freq = {}
for amount in transactions:
    freq[amount] = freq.get(amount, 0) + 1

# Sort by frequency descending, then value ascending
sorted_transactions = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

# Take top 2
top_2 = [item[0] for item in sorted_transactions[:2]]

print(top_2)







# Problem 2: Missing Value Percentage Calculator

data = [10, None, 20, 30, None, None, 40]

#Count total elements
total = len(data)

#  Count missing values
missing = 0
for value in data:
    if value is None:
        missing += 1

# Calculate percentage
percentage = (missing / total) * 100

# Round to 2 decimal places
percentage = round(percentage, 2)

print(percentage)

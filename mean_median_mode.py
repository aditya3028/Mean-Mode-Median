import csv
with open('Student_Marks.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    numbers = [float(row[0]) for row in reader]
print(numbers)

# Mean
mean = sum(numbers) / len(numbers)

# Median
numbers_sorted = sorted(numbers)
if len(numbers_sorted) % 2 == 0:
    median = (numbers_sorted[len(numbers_sorted)//2 - 1] + numbers_sorted[len(numbers_sorted)//2]) / 2
else:
    median = numbers_sorted[len(numbers_sorted)//2]

# Mode
mode = max(set(numbers), key=numbers.count)

# Print the results
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Mode: {mode:.2f}")

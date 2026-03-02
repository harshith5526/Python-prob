# Accept n numbers from the user

n = int(input("Enter the number of elements: "))

numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]

# Calculate Mean

mean = sum(numbers) / n

# Calculate Median

numbers.sort()

if n % 2 == 0:

median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

else:

median = numbers[n // 2]

# Calculate Mode

frequency = {num: numbers.count(num) for num in numbers}

max_count = max(frequency.values())

mode = [k for k, v in frequency.items() if v == max_count]

if len(mode) == n: # No mode if all numbers appear the same number of times

mode = "No mode" # Calculate Variance (Sample Variance, divide by (n-1))

mean_difference_squared_sum = sum((x - mean) ** 2 for x in numbers)

variance_sample = mean_difference_squared_sum / (n - 1) if n > 1 else 0 # Avoid division by 0

variance_population = mean_difference_squared_sum / n

# Calculate Standard Deviation

std_deviation_sample = variance_sample ** 0.5

std_deviation_population = variance_population ** 0.5
# Display results

print(f"Mean: {mean}")

print(f"Median: {median}")

print(f"Mode: {mode}")

print(f"Sample Variance: {variance_sample}")

print(f"Population Variance: {variance_population}")

print(f"Sample Standard Deviation: {std_deviation_sample}")

print(f"Population Standard Deviation: {std_deviation_population}")

# Name: Vijaya Mohan
# Roll Number: IITP_AIMLTN_2602502
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
max = 0

for i in temperatures:
    if i > max:
        max = i
print("The maximum temperature is:", max)
min = max
for i in temperatures:
    if i < min:
        min = i
print("The minimum temperature is:", min)


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
hot_days = 0
for i in temperatures:
    if i <= 30:
        continue
    hot_days +=1
print("Number of hot days (temperature > 30°C):", hot_days)
    

print("\n===== Task 3: Alert System =====")
# Write your code here
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_day = 0
for i, temp in enumerate(temperatures):
    if temp >= 40:
        break
    elif temp > 30:
      hot_day += 1
print("Number of hot days before alert:", hot_day)
print(f"Alert! Extreme temperature {temp} detected on Day {i}.")
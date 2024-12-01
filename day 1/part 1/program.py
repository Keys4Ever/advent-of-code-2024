def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    return total_distance

input_data = """
#Input data in readme.md of day 1
"""

lines = input_data.strip().split("\n")

right = []
left = []

for line in lines:
    values = line.split()
    if len(values) == 2:
        right.append(int(values[0]))
        left.append(int(values[1]))

total_distance = calculate_total_distance(left, right)
print("Total Distance:", total_distance)

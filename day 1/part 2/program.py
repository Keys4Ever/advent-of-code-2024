from collections import Counter

def calculate_similarity_score(left_list, right_list):
    right_count = Counter(right_list)
    
    similarity_score = sum(left * right_count[left] for left in left_list)
    
    return similarity_score

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

similarity_score = calculate_similarity_score(left, right)
print("Similarity Score:", similarity_score)

"""
solve problem without loop
"""
import re

a = "ab12cd345"
numbers = map(int, re.findall(r'\d+', a))  # Extract numbers from the string
result = sum(numbers)  # Sum the extracted numbers
print(result)
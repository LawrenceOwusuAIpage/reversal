from pathlib import Path
print(Path(__file__).resolve().parent.parent)

reverse = 0
number = 241
while number > 0:
    remainder = number % 10
    number = number//10
    reverse = reverse * 10 + remainder

print(reverse)
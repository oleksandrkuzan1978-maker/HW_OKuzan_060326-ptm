""" 03 Увеличение чисел

Напишите программу, которая
- заменяет все числа в строке на их эквивалент, умноженный на 10.

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
Пример вывода:
I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
"""
# ЗАДАНИЕ №3
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
print(text)
text1 = []
text = text.split()

for item in text:
    if item.isdigit() or (item.count(".") == 1 and item.replace(".", "").isdigit()):
        text1 += [str(float(item) * 10)]
    else:
        text1 += [item]

print("Результат:", " ".join(text1))

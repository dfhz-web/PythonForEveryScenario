message = ["apple123", "orange45", "banana789"]
sorted_message = sorted(message, key=lambda x: int(''.join(filter(str.isdigit, x))))
print(sorted_message)

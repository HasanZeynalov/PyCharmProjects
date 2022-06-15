import random

upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
lower = "qwertyuioplkjhgfdsazxcvbnm"
symbol = "?@#$%^&"
number = "1234567890"

string = upper + lower + symbol + number
length = 8

password = "".join(random.sample(string,length))

print(f"Your new password is {password}")

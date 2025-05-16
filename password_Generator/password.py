'''generate password which is tough to break for hackers
Python password Generate
'''

import random

lowwer_case = "qwertyuiopasdfghjklzxcvbnm"
upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
symbols = "@#$%&*/\?"

user_for = lowwer_case + upper_case + number + symbols
length_password = 8

password = "".join(random.sample(user_for,length_password))

print(f"Your password is: {password}")


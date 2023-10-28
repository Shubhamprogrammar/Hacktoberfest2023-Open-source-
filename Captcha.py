import random

up_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_case="abcdefghijklmnopqrstuvwxyz"
sym="@#$%?!~|?><*&"
num="123456789"

letters=up_case + low_case + sym + num
length=8
captcha =" ".join(random.sample(letters,length))
print(captcha)
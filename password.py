import random
lower = "abcdefghijklmnopqrstuvwxzy"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="1234567890"
symbol="[]{};*._"

all=lower + upper + number + symbol
length = 9
password= " ".join(random.sample(all,length))
print(" The password you Generated is :",password)
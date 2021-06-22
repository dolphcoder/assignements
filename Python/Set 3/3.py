import re

regex = re.compile(r"[789]\d{9}")
string = """hi! I'm ariana. I'm a singer. 
you can contact me on 9495667878 . 
My alternate phone no is 08086752310 . 
my landline number is 0481240562 . 
my address is 12th street, richmond road, Bangalore urban - 560098"""

match = regex.findall(string) 
print(match) 
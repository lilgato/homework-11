import re
findPhoneFile = open('FindPhonecc.txt','w')
phoneNumber = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phoneNumber.findall(findPhoneFile.read()))

email = re.compile(r'\w+@\w+.\w+')
print(email.findall(findPhoneFile.read()))

creditCard = re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}')
print(creditCard.findall(findPhoneFile.read()))

emailList = []
phoneList = []
CardList = []

findPhoneFile.close()

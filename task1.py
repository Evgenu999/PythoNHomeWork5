# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

list_text = ['ПРИНТЕР', 'НЕЗАБЫВАЕМАЯ', 'ЗИМБАБВЕ']
s = 'абв'

spisok = list(filter(lambda i: s not in i.lower(), list_text))
list1 = [i for i in list_text if s not in i.lower()]

print(spisok)
print(list1)

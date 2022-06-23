alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
y = 'y'
while y == 'y':
  text = input("enter text for encryption ", )
  text.upper
  offset = int(input("enter offset(key) ", ))
  endtext = ''
  action = input("Do you want to encrypt or decrypt?(en/de) ", )
  if action == 'en':
    for i in text:
      placeintext = alphabet.find(i)
      endplace = placeintext + offset
      endtext += alphabet[endplace % 27]
  elif action == 'de':
    for i in text:
      placeintext = alphabet.find(i)
      endplace = placeintext - offset
      endtext += alphabet[endplace % 27]
  else:
    print("enter en or de")
  print(endtext)
  y = input("Do you want to start new operation?(y/n) ")

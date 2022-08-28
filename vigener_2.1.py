alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
buffer = ''
key = ''

def encryption(buffer, key, alphabet):
  plain_text = buffer
  buffer = ''
  for i in range(len(plain_text)):
    buffer += alphabet[(alphabet.find(plain_text[i]) + alphabet.find(key[i % len(key)])) % 27]
  return buffer
  
def decryption(buffer, key, alphabet):
  cypher_text = buffer
  buffer = ''
  for i in range(len(cypher_text)):
    buffer += alphabet[(alphabet.find(cypher_text[i]) - alphabet.find(key[i % len(key)])) % 27]
  return buffer
  
y = 'y'
print("Please, use only upper index")
buffer = input("enter text for crypting: ", )
key = input("enter key for crypting: ", )
while y == 'y':
  action = input("Choose encryption or decription(e/d): ", )
  if action == 'e':
    buffer = encryption(buffer, key, alphabet)
  elif action == 'd':
    buffer = decryption(buffer, key, alphabet)
  else:
    print("invalid action, (e/d) wanted")
  print(buffer)
  y = input("would you start new operation?(y/n): ", )
  if y == 'y':
    buffer_clear = input("Do you want to enter new text and key?(y/n): ", )
    if buffer_clear == 'y':
      buffer = input("enter text for crypting: ", )
      key = input("enter key for crypting: ", )
print('Goodbye')    

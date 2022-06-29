alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
buffer = ''
key = ''

def encryption(buffer, key, alphabet):
  key_length = len(key)
  plain = buffer
  plain_length = len(plain)
  buffer = ''
  for i in range(plain_length):
    place_in_alphabet = alphabet.find(plain[i])
    place_in_alphabet_key = alphabet.find(key[i % key_length])
    buffer += alphabet[(place_in_alphabet + place_in_alphabet_key) % 27]
  return buffer
  
def decryption(buffer, key, alphabet):
  key_length = len(key)
  cypher = buffer
  cypher_length = len(cypher)
  buffer = ''
  for i in range(cypher_length):
    place_in_alphabet = alphabet.find(cypher[i])
    place_in_alphabet_key = alphabet.find(key[i % key_length])
    buffer += alphabet[(place_in_alphabet - place_in_alphabet_key) % 27]
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
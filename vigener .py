buffer = ''
key = ''
def encryption(buffer, key):
  key_length = len(key)
  key_int = [ord(i) for i in key]
  plain = buffer
  buffer = ''
  plain_int = [ord(i) for i in plain]
  for i in range(len(plain_int)):
    value = (plain_int[i] + key_int[i % key_length]) % 26
    buffer += chr(value + 65)
  return buffer
  
def decryption(buffer, key):
  key_length = len(key)
  key_int = [ord(i) for i in key]
  cipher = buffer
  buffer = ''
  cipher_int = [ord(i) for i in cipher]
  for i in range(len(cipher_int)):
    value = (cipher_int[i] - key_int[i % key_length]) % 26
    buffer += chr(value + 65)
  return buffer
  
y = 'y'
print("Please, use only upper index")
buffer = input("enter text for crypting: ", )
key = input("enter key for crypting: ", )
while y == 'y':
  action = input("Choose encryption or decription(e/d): ", )
  if action == 'e':
    buffer = encryption(buffer, key)
  elif action == 'd':
    buffer = decryption(buffer, key)
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
      
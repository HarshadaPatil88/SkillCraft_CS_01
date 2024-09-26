def caesar_cipher(text, shift):
  encrypted_text = ""
  for char in text:
      if char.isalpha():
          # Determine if the character is uppercase or lowercase
          base = ord('A') if char.isupper() else ord('a')
          # Shift the character and wrap around if needed
          shifted = (ord(char) - base + shift) % 26 + base
          encrypted_text += chr(shifted)
      else:
          # Non-alphabet characters remain unchanged
          encrypted_text += char
  return encrypted_text

def encrypt(message, shift):
  return caesar_cipher(message, shift)

def decrypt(encrypted_message, shift):
  # To decrypt, we shift in the opposite direction
  return caesar_cipher(encrypted_message, -shift)

def main():
  print("Caesar Cipher Encryption and Decryption")
  message = input("Enter your message: ")
  shift = int(input("Enter shift value (integer): "))

  encrypted_message = encrypt(message, shift)
  print(f"Encrypted message: {encrypted_message}")

  decrypted_message = decrypt(encrypted_message, shift)
  print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
  main()
#!/usr/bin/env python
# coding: utf-8

# In[1]:


def encrypt(message, key):
    # Create an empty string to store the encrypted message
    encrypted_message = ""
    
    # Iterate over each character in the message
    for letter in message:
        # Check if the character is a letter
        if letter.isalpha():
            # Check if the letter is uppercase
            if letter.isupper():
                # Encrypt the letter by adding the key value and converting back to a letter
                # ord() gets the Unicode code point of the letter
                # 65 is the Unicode code point for 'A', so we subtract it to get the letter's position in the alphabet
                # % 26 ensures that we wrap around to the beginning of the alphabet if we go past 'Z'
                # We add 65 back to convert the letter's position back to a Unicode code point for the encrypted letter
                encrypted_message += chr((ord(letter) + key - 65) % 26 + 65)
            else:
                # Encrypt the letter in the same way as above, but for lowercase letters
                encrypted_message += chr((ord(letter) + key - 97) % 26 + 97)
        else:
            # If the character is not a letter, just add it to the encrypted message as is
            encrypted_message += letter
    
    # Return the encrypted message
    return encrypted_message

def decrypt(message, key):
    # Create an empty string to store the decrypted message
    decrypted_message = ""
    
    # Iterate over each character in the message
    for letter in message:
        # Check if the character is a letter
        if letter.isalpha():
            # Check if the letter is uppercase
            if letter.isupper():
                # Decrypt the letter by subtracting the key value and converting back to a letter
                # ord() gets the Unicode code point of the letter
                # 65 is the Unicode code point for 'A', so we subtract it to get the letter's position in the alphabet
                # % 26 ensures that we wrap around to the end of the alphabet if we go past 'A'
                # We add 65 back to convert the letter's position back to a Unicode code point for the decrypted letter
                decrypted_message += chr((ord(letter) - key - 65) % 26 + 65)
            else:
                # Decrypt the letter in the same way as above, but for lowercase letters
                decrypted_message += chr((ord(letter) - key - 97) % 26 + 97)
        else:
            # If the character is not a letter, just add it to the decrypted message as is
            decrypted_message += letter
    
    # Return the decrypted message
    return decrypted_message


# In[2]:


message = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
key = 3

encrypted_message = encrypt(message, key)
print(encrypted_message)

decrypted_message = decrypt(encrypted_message, key)
print(decrypted_message)


# In[ ]:





def encrypt():
    alphabet = "abcdefghijklmnopqrstuvw"
    input_string = ""
    key = ""
    encrypted_string = ""

    #User Input: Text that should be encrypted
    input_string = input(">> Enter your phrase:")
    input_string = input_string.lower
    length_input_string = len(input_string)

    #User Input: Key that is used to encrypt the text
    key = input(">> Enter the key:")
    key = key.lower

    #Elongates the key to the length of the plaintext
    long_key = key
    length_long_key = len(long_key)
    while length_long_key < length_input_string: #Fix Error: TypeError: object of type 'builtin_function_or_method' has no len()
        long_key = long_key + key

    for letter in input_string:
        if letter in alphabet:

            #Finds position of letter inside of the plaintext
            pos = alphabet.find(letter)

            #Finds the position of the letter inside of the key
            key_char = long_key[key_pos]
            key_char_pos = alphabet.find(key_char)
            key_pos = key_pos + 1

            #Reduces the key to letters inside of the alphabet
            new_pos = pos + key_char_pos
            if new_pos > 26:
                new_pos = new_pos - 26
            
            #Adds the encrypted letter to the ciphertext
            new_char = alphabet[new_pos]
            encrypted_string = encrypted_string + new_char

        else:
            #Adds non letters to the ciphertext
            encrypted_string = encrypted_string + letter

    return(encrypted_string)

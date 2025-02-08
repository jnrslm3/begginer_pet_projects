import random

uppercaseLetter1 = chr(random.randint(65,90))
uppercaseLetter2 = chr(random.randint(65,90))

lowercaseLetter1 = chr(random.randint(97,122))
lowercaseLetter2 = chr(random.randint(97,122))

digit1 = str(random.randint(0, 9))
digit2 = str(random.randint(0, 9))

punctuation_choices = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"
punctuationSign1 = random.choice(punctuation_choices)
punctuationSign2 = random.choice(punctuation_choices)

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
print(password)


#https://www.101computing.net/wp/wp-content/uploads/ASCII-Table.pdf
import random
import math

class Password:
    def __init__(self, length, numbers):
        # password must be atleast 15 characters long
        self.length = self.get_valid_password_length(length)

        # numbers denote the user's choice whether to include numbers in the password
        # True or False
        self.numbers = numbers

    
    # getting the valid password length
    # 15 <= length_of_the_password <= 30
    def get_valid_password_length(self, length=None):
        if length is None:
            return 15
        
        if length < 15:
            return 15
        
        if length > 30:
            return 30
        
        return length
    

    # generating a random password
    def generate_password(self):
        password = ""

        for i in range(self.length):
            password += self.character_type_decision()
        
        return password
    

    # decision making
    # each character in the password can be either:
    #   - an uppercase or lowercase letter
    #   - a number from 0 to 9
    #   - a special character
    def character_type_decision(self):
        # password has both numbers and alphabets
        if self.numbers:
            choice = random.randint(0, 1)

            if choice:
                # choice is 1
                # generate a random number
                return self.random_number()
            
            return self.random_uppercase_or_lowercase()

        # password contains only an alphabet
        return self.random_uppercase_or_lowercase()


    # generating a random number from 0 to 9
    def random_number(self):
        return str(random.randint(0, 9))
    

    # generating a random special character from the list of special characters
    def random_special_character(self):
        special_characters = ["!", "@", "#", "$", "%", "&", "(", ")", "+", "{", "}", "?", "/", ":", "|"]

        return random.choice(special_characters)
    

    # generating a random alphabet
    def random_uppercase_or_lowercase(self):
        choice = random.randint(0, 1)

        if choice:
            return self.random_uppercase_letter()
        
        return self.random_lowercase_letter()
        
    
    # generating a random lowercase letter using ascii values
    def random_lowercase_letter(self):
        # 97 - ascii value of a
        # 122 - ascii value of b
        return chr(random.randint(97, 122))
    

    # generating a random uppercase letter using ascci values
    def random_uppercase_letter(self):
        # 65 - ascii value of A
        # 90 - ascii value of Z
        return chr(random.randint(65, 90))


if __name__ == "__main__":
    print(Password(15).generate_password())
import random
import math

class Password:
    def __init__(self, length):
        # password must be atleast 15 characters long
        self.length = self.get_valid_password_length(length)

    
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
            password += self.random_uppercase_or_lowercase()
        
        return password
    
    
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
    print(Password().generate_password())
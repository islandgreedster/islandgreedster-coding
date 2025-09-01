"""
Password Generator
------------------
Generates strong random passwords with letters, numbers, and symbols.
Created by islandgreedster 🚀
"""

import random
import string

class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate(self):
        return ''.join(random.choice(self.characters) for _ in range(self.length))

    def generate_multiple(self, count=5):
        return [self.generate() for _ in range(count)]


# Demo usage
if __name__ == "__main__":
    generator = PasswordGenerator(length=16)

    print("🔑 Your random password is:")
    print(generator.generate())

    print("\n📦 Here are 3 more passwords:")
    for pwd in generator.generate_multiple(3):
        print("-", pwd)

  

import random
import string

# Simple word list for memorable passwords
WORDS = [
    "apple", "happy", "cloud", "river", "sun", "ocean", "light", "star", "dream", "magic",
    "forest", "green", "swift", "brave", "lucky", "blue", "gold", "dragon", "nova", "zen"
]

def get_password_length():
    while True:
        try:
            length = int(input("Password length (min 6): "))
            if length >= 6:
                return length
            else:
                print("Please enter a number >= 6.")
        except ValueError:
            print("Please enter a valid number.")

def get_yes_no(prompt):
    while True:
        resp = input(f"{prompt} (y/n): ").lower()
        if resp in ['y', 'yes']:
            return True
        elif resp in ['n', 'no']:
            return False
        else:
            print("Please answer y or n.")

def generate_random_password(length, use_symbols):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_memorable_password(length, use_symbols):
    pw = ''
    while len(pw) < length:
        word = random.choice(WORDS)
        pw += word.capitalize() if random.random() < 0.5 else word
        if use_symbols and random.random() > 0.7:
            pw += random.choice('!@#$%&*?')
    # Trim to length
    return pw[:length]

def main():
    print("==== Customisable Password Generator ====")
    length = get_password_length()
    use_symbols = get_yes_no("Include special symbols?")
    memorable = get_yes_no("Should the password be memorable (uses random words)?")

    if memorable:
        password = generate_memorable_password(length, use_symbols)
    else:
        password = generate_random_password(length, use_symbols)

    print("\nYour generated password:")
    print("-" * (length + 4))
    print(f"  {password}")
    print("-" * (length + 4))

if __name__ == "__main__":
    main()

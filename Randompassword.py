import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    if not (use_upper or use_lower or use_digits or use_special):
        raise ValueError("At least one character set must be selected")

    special_chars = "@!#$%&*"
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += special_chars

    # Ensure at least one character from each selected set
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(special_chars))

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    return ''.join(password)

def main():
    print(Fore.CYAN + r"""
  ____   ____  
 |  _ \ / ___| 
 | |_) | |  _  
 |  __/ | |_| |
 |_|     \____|
    """ + Style.RESET_ALL)

    print("Author By: Gayathri Nalluri")
    print("GitHub: https://github.com/Gayathri2531\n")

    try:
        length = int(input("Enter password length (e.g. 08): "))
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters (@!#$%&*)? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\nGenerated Password: {Fore.GREEN}{password}{Style.RESET_ALL}")

    except ValueError as e:
        print(f"{Fore.RED}Error: {e}")

if __name__ == "__main__":
    main()


import secrets
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    groups = []

    if use_upper:
        groups.append(string.ascii_uppercase)

    if use_lower:
        groups.append(string.ascii_lowercase)

    if use_digits:
        groups.append(string.digits)

    if use_symbols:
        groups.append("!@#$%^&*()-_=+?")

    if not groups:
        raise ValueError("Select at least one character type.")

    if length < len(groups):
        raise ValueError(
            f"Password length must be at least {len(groups)} "
            "for the selected options."
        )

    for group in groups:
        characters += group

    # Ensure at least one character from each selected group
    password_chars = [secrets.choice(group) for group in groups]

    # Fill the remaining positions
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(characters))

    # Securely shuffle the characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=" * 45)
    print("       SECURE PASSWORD MAKER")
    print("=" * 45)

    try:
        length = int(input("Enter password length (4-128): "))

        if not 4 <= length <= 128:
            print("Please enter a length between 4 and 128.")
            return

        print("\nChoose character types (y/n):")
        use_upper = input("Include uppercase letters? ").strip().lower() == "y"
        use_lower = input("Include lowercase letters? ").strip().lower() == "y"
        use_digits = input("Include numbers? ").strip().lower() == "y"
        use_symbols = input("Include symbols? ").strip().lower() == "y"

        password = generate_password(
            length,
            use_upper,
            use_lower,
            use_digits,
            use_symbols
        )

        print("\n" + "-" * 45)
        print("Generated Password:", password)
        print("-" * 45)
        print("Keep your password private and secure.")

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()

def is_palindrome(string: str) -> bool:
    string = string.lower().replace(" ", "")
    return string == string[::-1]


def run():
    string = input("Check if it is palindrome: ")
    print(is_palindrome(string))


if __name__ == "__main__":
    run()
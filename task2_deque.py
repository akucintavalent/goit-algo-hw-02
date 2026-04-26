from collections import deque


def is_palindrome(string: str) -> bool:
    dq = deque()

    for letter in string:
        if not letter.isspace():
            dq.append(letter.lower())

    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False

    return True


def main() -> None:
    should_exit = False

    while not should_exit:
        try:
            string_to_verify = input("Enter a string to verify if it is a palindrome: ")
            string_is_palindrome = is_palindrome(string_to_verify)
            print(
                f"'{string_to_verify}' is {'' if string_is_palindrome else 'not '}a palindrome."
            )
        except KeyboardInterrupt:
            should_exit = True


if __name__ == "__main__":
    main()

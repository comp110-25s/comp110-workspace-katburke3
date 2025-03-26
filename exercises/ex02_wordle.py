__author__ = "730558066"


def contains_char(word: str, letter: str) -> bool:
    """determining if the letter is contained within the secret word"""
    assert len(letter) == 1, f"len({letter}) is not 1"
    index: int = 0
    while index < len(word):
        if word[index] == letter:
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """turning the guessed word into green, white, and yellow boxes"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result = result + GREEN_BOX
        elif (contains_char(word=secret, letter=guess[idx])) == True:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        idx += 1
    return result


def input_guess(expected_length: int) -> str:
    """is the word we guess the same length as the expected length?"""
    word_guess:str = input(f"Enter a {expected_length} character word:")
    while len(word_guess) != expected_length:
        word_guess = input(f"That wasn't {expected_length} chars! Try again:")
    return word_guess


def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    n_turn: int = 1
    while n_turn < 7:
        print(f"=== Turn {n_turn}/6 ===")
        turn_guess: str = input_guess(expected_length=len(secret_word))
        print(emojified(guess=turn_guess, secret=secret_word))
        if turn_guess == secret_word:
            return print(f"You won in {n_turn}/6 turns!")
        else:
            n_turn += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="codes")

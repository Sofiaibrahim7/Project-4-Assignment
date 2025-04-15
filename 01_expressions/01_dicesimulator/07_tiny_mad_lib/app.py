# Constant sentence beginning
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my"

def get_user_input(prompt: str) -> str:
    """Prompts the user and returns their input as a string."""
    return input(prompt)

def create_mad_lib(adjective: str, noun: str, verb: str) -> str:
    """Constructs and returns the final mad lib sentence."""
    return f"{SENTENCE_START} {adjective} {noun} {verb}!"

def main() -> None:
    # Getting user inputs
    adjective: str = get_user_input("Please type an adjective and press enter: ")
    noun: str = get_user_input("Please type a noun and press enter: ")
    verb: str = get_user_input("Please type a verb and press enter: ")

    # Creating and printing the final sentence
    final_sentence: str = create_mad_lib(adjective, noun, verb)
    print(final_sentence)

# Required line to run the main function
if __name__ == '__main__':
    main()

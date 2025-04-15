📝 Sentence Maker — Python Program
🧠 Problem Statement
Write a function make_sentence(word, part_of_speech) that takes a string word and an integer part_of_speech as parameters. Based on the value of part_of_speech, it will insert the word into a sentence template corresponding to the type of word (noun, verb, or adjective):

If part_of_speech is 0 (noun): "I am excited to add this ____ to my vast collection of them!"

If part_of_speech is 1 (verb): "It's so nice outside today it makes me want to ____!"

If part_of_speech is 2 (adjective): "Looking out my window, the sky is big and ____!"

The function should print the correct sentence with the word filled in the blank. The function should not return anything.

💻 Python Code
python
def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        # verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        # adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    print("Is this a noun, verb, or adjective?")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
🧪 Example Run:
pgsql
Please type a noun, verb, or adjective: groovy
Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 2
Looking out my window, the sky is big and groovy!
📌 Key Concepts
Conditional Statements: The program uses if and elif to choose the correct sentence template based on the part_of_speech input.

User Input: The program prompts the user to enter a word and a part of speech, then calls the make_sentence function to print the appropriate sentence.


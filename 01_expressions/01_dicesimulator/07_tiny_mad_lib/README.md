# 🎉 Mad Libs Game - Python Project

This is a simple **Mad Libs** word game built using Python.  
The game prompts the user for three types of words:
- An **adjective**
- A **noun**
- A **verb**

Then it combines those inputs into a fun and silly sentence!

---

## 📌 Problem Statement

Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

> Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into a sentence template to make an entertaining story.

### ✅ Sample Output

```plaintext
Please type an adjective and press enter: tiny  
Please type a noun and press enter: plant  
Please type a verb and press enter: fly  
Panaversity is fun. I learned to program and used Python to make my tiny plant fly!

📝 How the Code Works:
Function: main
The program first prompts the user to input an adjective, noun, and verb.

It then combines these inputs into a pre-defined sentence template.

Finally, the combined sentence is displayed to the user, creating a fun and unique story.

💻 How to Run the Code:
Install Python:

If you don't have Python installed, download and install it from Python.org.

Save the Code:

Copy the code into a file named mad_libs.py.

Navigate to the Directory:

Open a terminal (Command Prompt or PowerShell) and navigate to the directory where mad_libs.py is saved.

Run the Code:

In the terminal, run the command:

bash
Copy
Edit
python mad_libs.py
Expected Output:

After entering the adjective, noun, and verb, you should see an output like:

plaintext
Copy
Edit
Panaversity is fun. I learned to program and used Python to make my tiny plant fly!
🛠 Code Example:
python
Copy
Edit
# Sentence start template
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
💡 Key Concepts Used:
User Input: The program takes input from the user for three different word types.

String Manipulation: The words provided by the user are inserted into a sentence template.

Functions: Code is organized into functions for clarity and reusability.

📌 Additional Notes:
This project can be extended by allowing users to input multiple sets of words and creating multiple fun sentences.

You can modify the sentence template to create different stories by changing the SENTENCE_START.

The program can be further enhanced with input validation or error handling to ensure that the user enters valid words.













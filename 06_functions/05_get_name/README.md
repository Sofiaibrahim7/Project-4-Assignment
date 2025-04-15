👋 Greeting Program — Python Code
🧠 Problem Statement
Write a function get_name() that returns your name as a string. The program will then use this function to print a greeting.

🧪 Solution
Function:
get_name():

This function returns a string containing your name. For this example, it returns the name "Sophia".

main():

This function calls get_name() to get your name and prints a greeting with the name.

💻 Python Code
python

def get_name():
    return "Sophia"

# There is no need to edit code beyond this point

def main():
    name = get_name()  # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    main()
🧪 Example Run:
nginx

Howdy Sophia ! 🤠
📌 Key Concepts
String Return: The get_name() function simply returns a string.

String Concatenation: The print() function combines the returned string with the greeting.
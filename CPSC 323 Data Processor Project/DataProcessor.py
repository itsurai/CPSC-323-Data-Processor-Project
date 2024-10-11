import re
from tabulate import tabulate


#Main Function
def main():

    #Anything that you want to remove extra spaces from & tokenize goes in the string 'inputCode'
    inputCode = """
    # This is a sample code
    # It adds two numbers
    
    def add(a, b):
        # Add two numbers
        result = a +     b
        return result
    
    # Test the function
    print(add(5, 3))
    """

    #Show the output from specific functions.
    debugOutput = processUserInput(inputCode)
    print("Processed input\n\n", debugOutput)
    tokenizeResult = tokenizer(debugOutput)
    print("\nTokenized code\n", tokenizeResult)

    print("\nTabular Form:\n")
    printTable(tokenizeResult)

#Remove whitespace and comments
def processUserInput(inputCode):
    processedInput = []

    for line in inputCode.splitlines():
        #Identify excess empty space between characters and replace with a single space
        #Remove trailing/leading whitespace.
        line = re.sub(r'\s+', ' ', line).strip()

        #Match any lines beginning with a '#' and replace it with empty space
        line = re.sub(r'#.*', '', line)

        #We are skipping over any empty lines here
        if line:
            processedInput.append(line)

    #Rebuild the processed input.
    return "\n".join(processedInput)

#This function will tokenize the processed input
def tokenizer(processedInput):
    #We are establishing the categories. Can be expanded for more complex code.
    keywords = {'def', 'return', 'print'}
    operators = {'+', '-', '*', '/', '=', '=='}
    delimiters = {'(', ')', ':', ','}

    #The tokens dictionary has lists that will fill up as the processed code is tokenized.
    tokens = {
        'Keywords': [],
        'Identifiers': [],
        'Operators': [],
        'Delimiters': [],
        'Literals': []
    }

    #Regex splits the lines of code into the categories listed above.
    token_pattern = re.compile(r'\w+|\d+|[+\-*/=()]|[:,]')

    #Tokenizing happensh ere
    for line in processedInput.splitlines():
        for word in token_pattern.findall(line):
            if word in keywords:
                tokens['Keywords'].append(word)
            elif word in operators:
                tokens['Operators'].append(word)
            elif word in delimiters:
                tokens['Delimiters'].append(word)
            elif word.isdigit():
                tokens['Literals'].append(word)
            else:
                tokens['Identifiers'].append(word)  #Any leftovers must be identifiers! 
    
    return tokens


#Finally put the tokens into a table so its easier to read.
def printTable(tokens):
    #Convert the dictionary into rows where each row contains the category and the tokens joined by commas
    table_data = [[category, ', '.join(token_list)] for category, token_list in tokens.items()]
    
    #Print the table using tabulate
    print(tabulate(table_data, headers=["Category", "Tokens"], tablefmt="grid"))
    
if __name__ == "__main__":
    main()
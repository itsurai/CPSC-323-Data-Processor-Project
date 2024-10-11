import re

#Main Function
def main():
    print("Debug line 1")

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

    #Show the output from specific functions. Will remove later.
    debugOutput = processUserInput(inputCode)
    print(debugOutput)

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

    



    













if __name__ == "__main__":
    main()
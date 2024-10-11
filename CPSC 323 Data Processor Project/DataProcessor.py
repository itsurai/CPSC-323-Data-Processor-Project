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

    print(inputCode)
    print("End of main function")
    



if __name__ == "__main__":
    main()
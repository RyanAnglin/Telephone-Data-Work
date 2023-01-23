def main():

    filename = input("Enter name of input file: ")
    
    inputFile = open(filename, "r")#Opens the file of string
    
    words1 = inputFile.read() #Reads the string

    words2 = words1.split(";") #Splits the strings up by it's semicolon 

    print(words2) #Prints the array of split up numbers, 
    
    inputFile.close() #Closes the File 

main() 

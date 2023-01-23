'''Goal: Too take an array of numbers in AAAA-BB-CCC-DD format and change it to AAA-B-CC-DD format.
 
Step 2: Remove the first 0 in the AAAA group.
Step 3: Remove the dash and replace it with space. 
Step 4: Remove the second 0 from the BB group
Step 5: Remove the dash and replace it with space. 
Step 6: Remove the third 0 from CCC group.
Step 7: Remove the dash and replace it with space. 
Step 8: Keep the fourth DD.
Step 9: Output the number in AAA_B_CC_DD format.'''

def main():
#---------------------------------
    #Step 1: Grab a file with all the numbers in it.
    
    filename = input("Enter name of input file: ")
        # Ask for a file 
    
    inputFile = open(filename, "r")
        #Opens the file and contents are strings

#----------------------------------
    #Step 2: Read the file.
    
    words1 = inputFile.read()
        #Reads the string assigns them to a value.
    
#----------------------------------
    #Step 3: Split up string by their semicolons.
    
    SplitUpArray = words1.split()
        #Splits the strings up by it's semicolon 
   
    #print(SplitUpArray)
        #Prints the array of split up strings. Just a check to make sure they're split. 

#----------------------------------
    #Step 4: Open up an Output File.
    
    f = open("myfile.txt","w")
#-------------------------------------

    #Step 5: The Loop. Take a string in the array, change it. 
    i = 0 
    for i in range(len(SplitUpArray)):      

        NumInput = SplitUpArray[i]
            
        result_str = NumInput.replace('0','',1) #Remove first 0 in string
        #result_str = NumInput.replace('0','',2) #Remove second 0 in string 

        dex = 4 #The position of the character in the string we want to remove
        
        if len(result_str) > dex:

            result_str = result_str[0:dex] + result_str[dex+1:]
        
        index = 6 #The position of the character in the string we want to remove.

        if len(result_str) > index: #If the length of the string after 0s are remove is 
                                    #longer than the length of the characters position in which we want
                                    # to remove:
                                    
                result_str = result_str[0 : index] + result_str[index + 1 :] #or result_str
    
                    #Variable is changed to have characters from 0-6 to the end, and add on from 7 to
                    #the end of the string. 
                result_str = result_str.replace("-"," ")
                    #Replace dashes with spaces.  
                result_str = result_str + ","
                    #Take the string and add a semicolon at the end.

    #Step 6: Write the new string to the OutPut File     

        f.write(result_str)
        i = i+1
    #Step 7: Print the result as a check and close the input file. 
        print(result_str)
    
    inputFile.close() #Closes the File
    

main()

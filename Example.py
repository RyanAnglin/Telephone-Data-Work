'''Goal: Too take an array of numbers in AAAA-BB-CCC-DD format and change it to AAA-B-CC-DD format.
Step 1: Take a number and turn it into an integer. 
Step 2: Remove the first 0 in the AAAA group.
Step 3: Remove the dash and replace it with space. 
Step 4: Remove the second 0 from the BB group
Step 5: Remove the dash and replace it with space. 
Step 6: Remove the third 0 from CCC group.
Step 7: Remove the dash and replace it with space. 
Step 8: Keep the fourth DD.
Step 9: Output the number in AAA_B_CC_DD format.'''

def main():

    NumInput = input("Input a number: ")

    result_str = NumInput.replace('0','',1) #Remove first 0 in string
    result_str = NumInput.replace('0','',2) #Remove second 0 in string 

    index = 6
    
    if len(result_str) > index:
        result_str = result_str[0 : index : ] + result_str[index + 1 : : ]

    #index = 9
    
    #if len(result_str) > index:
        #result_str = result_str[0 : index : ] + result_str[index + 1 : : ]

    result_str = result_str.replace("-"," ")   
  
    print("Output Number:",result_str);


main()

"""
Name: Isa Graham Torres
Peers:
References: Class notes and Thonny Assistant
"""

"""
My Plan:
_____________________________________________________________________________________________________

get_letter()
    
    1. define letter as input("Give an single uppercase letter: ")
    2. set up an infinite while loop so that:
        a. if letter's length is greater than 1, it prints an error and restarts the loop with continue
        b. if letter is not A, B, or C, it prints an error and restarts the code with continue
        c. Else, It BREAKS out of the loop and returns letter
    
_____________________________________________________________________________________________________

get_digit()


    1. define digit as the input of("Give an single number character: ")
    2. set up an infinite while loop so that:
        a. if digit is not all digits, it prints an error and restarts the loop with continue
        b. if digit is not equal to 1, 2, or 3, it prints and error and restarts the loop with continue
        c. Else, it BREAKS out of the loop and returns digit
    
_____________________________________________________________________________________________________
check_pattern()
    
 
    1. print("Strings with the pattern:")
    2. set up a for loop so that:
        a. if a word in list contains letter before digit, print the word
        b. if a word in list contains digit before letter, don't print the word
        c. if a word in list contains letter before digit more than once, print the word once
_____________________________________________________________________________________________________
"""


def get_letter():
    
   
   # here I set up an infinite loop where letter is the input of "Give an single uppercase letter: "
    while True:
        letter = input("Give an single uppercase letter: ")
        
        # if the length of letter is greater than one, it prints "Error: it needs to be a single character." and re-runs the loop
        if len(letter) >1:
            print("Error: it needs to be a single character.")
            continue
        
            
        # else if letter is not "A", "B", or "C", it prints "Error: You provided the wrong character." and re-runs the loop
        elif letter not in ["A", "B", "C"]:
            print("Error: You provided the wrong character.")
            continue
             
        # if neither of the above conditions are true, than return letter and break out the loop       
        else:
            return letter
            break
        
        
            
def get_digit():
    
    
    # I sset up an infinite loop where digit is the input of "Give an single number character: "
    while True:
        digit = input("Give an single number character: ")
        
        # if digit is not a digit, print "Error: your input should be only digits." and re-run the loop
        if digit.isdigit() is False:
            print("Error: your input should be only digits.")
            continue
        
        # else if digit is not "1", "2", or "3", print "Error: a single digit needs to be in [1,3]." and re-run the loop
        elif digit not in ["1", "2", "3"]:
            print("Error: a single digit needs to be in [1,3].")
            continue
        
        # if neither of the above conditions are true, then return digit and break out the loop
        else:
            return digit
            break
            
            
    
        
        
        
        
            


def check_pattern(letter, digit, lst):
    
    
    # print the required text
    print("Strings with the pattern:")
    
    
    # for every word within the provided list, check if letter and digit are in the word
    for word in lst:
        if letter in word and digit in word:
            
            # if both letter and digit are in the word AND letter comes before digit, print the word
            if word.index(letter) < word.index(digit):
                print(word, end=" ")
                
            # if both letter and digit are NOT in the word OR letter comes after digit, break the loop
            else:
                break
    print()
            

#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    
    
    
    while True:
        
        # I set lst equal to st_list so I can call lst later
        lst = st_list
        
        # I run the get_letter() function and set letter equal to the result
        letter = get_letter()
        
        # I run the get_digit() function and set digit equal to the result
        digit = get_digit()
        
        # I run the check_pattern() function using the results of get_letter, get_digit, and the list of words
        check_pattern(letter, digit, lst)
        
        # I set up the y/n prompt 
        prompt = input("Try Again? (y/n): ")
        
        # if user enters "y", continue the loop
        if prompt == "y":
            continue
        
        # if user enters anything but "y", break out of the loop
        else:
            break
        



    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()
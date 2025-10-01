# FILE NAME - convert_C_to_F_02.py

# NAME: Makiko Michelle Yasumi
# DATE: October 1, 2025
# BRIEF DESCRIPTION:  This program allows users to choose to convert between Celsius and Fahrenheit in both directions.
# Then, the user can enter the temperature, and the program outputs the conversion.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    convert()

def convert():
    print("=" * 5 + " Temperature Converter " + "=" * 5)
    
    print("\n  1. Convert from Celsius to Fahrenheit")
    print("  2. Convert from Fahrenheit to Celsius")

    choice = int(input("\nPlease choose from the above menu: "))

    if choice == 1:
        celsius = int(input("Enter a temperature to convert: "))
        converted_f = celsius * 9/5 + 32
        print(f"\n{celsius:.1f} degrees Celsius is {converted_f:.1f} degrees Fahrenheit.")
    else:
        fahrenheit = int(input("Enter a temperature to convert: "))
        converted_c = (fahrenheit - 32) * 5/9
        print(f"\n{fahrenheit:.1f} degrees Fahrenheit is {converted_c:.1f} degrees Celsius.")

main()


########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: 32

32.0 degrees Fahrenheit is 0.0 degrees Celsius.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 1
Enter a temperature to convert: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.
'''


'''
===== Temperature Converter =====

  1. Convert from Celsius to Fahrenheit
  2. Convert from Fahrenheit to Celsius

Please choose from the above menu: 2
Enter a temperature to convert: -40

-40.0 degrees Fahrenheit is -40.0 degrees Celsius.
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is one lesson you learned in this lab?

How to spell "fahrenheit."


'''

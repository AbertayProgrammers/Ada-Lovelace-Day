import string

def shift_cipher(input_text, shift):
	# !INACTIVE! Create a string containing all printable non-whitespace characters
    # !INACTIVE! alphabet = ''.join([c for c in string.printable if c not in string.whitespace])
    
    # Create a string containing lowercase and uppercase ascii characters
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    # if the shift value is 0, test all possible shift values
    if shift == 0:
        print("!ENTERING REVERSE MODE!")
    	# test every shift from min to the max alphabet size
        for shift in range(-len(alphabet), 1):
        	# shift alphabet by given value (allows loop-arounds)
            shifted_alphabet = alphabet[shift:] + alphabet[:shift]
            # create translation table for alphabet to shifted alphabet 
            cipher = str.maketrans(alphabet, shifted_alphabet)
            # use transaltion table to print output
            print("Output:[%s], Key Used:[%s], Input:[%s]" % (input_text, -1*shift, input_text.translate(cipher)))
    else:	
        print("!ENTERING SHIFT MODE!")
        # shift alphabet by given value (allows loop-arounds)
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        # create translation table for alphabet to shifted alphabet 
        cipher = str.maketrans(alphabet, shifted_alphabet)
        # use transaltion table to print output
        print("Input:[%s],\n Key:[%s],\n Output:[%s]\n" % (input_text, shift, input_text.translate(cipher)))



if __name__ == "__main__":
    print("~!AR-Calders's Simple Shift Cipher Cracker!~")
    text = input("Ciphered Text: ")
    shift = int(input("Shift (0 to enter crack mode!)"))
    shift_cipher(text, shift)

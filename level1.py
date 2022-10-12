def solution(x):
        
	# message as an array of characters
	message = [y for y in x]

	for i in range(len(message)):

		if message[i].islower() == True:

			# subtracts current ascii value from 219
			# (ascii value of a + z) to get decoded character 
			new_character = chr(219 - ord(message[i]))
			message[i] = new_character

			decoded_message = ''.join(message)

		else:

			# failsafe for strings with no lowercase chars
			decoded_message = ''.join(message)

	return(decoded_message)

we can see that each character of enc is formed through 2 characters of the original flag. Each character is 16 bits long.
The first 8 bits (LSB side) are taken from the first character, the other 8 bits (MSB side) are taken from the second character
This means that we just need to take each character from the enc file and make two characters from by extracting the first 8
bits and the last 8 bits.


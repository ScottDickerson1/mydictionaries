#FileEncryption.py - Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:

#codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, etc . . .} Using this example, the letter A would be assigned the symbol %, 
# the letter a would be assigned the number 9, the letter B would be assigned the symbol @, and so forth. 
# The program should open this file -  info_security.txt  Download info_security.txt, read its contents, then use the dictionary to 
# write an encrypted version of the file’s contents to a second file (name it 'encrypted.txt'). 
# Each character in the second file should contain the code for the corresponding character in the first file.

infile = open('info_security.txt', 'r')
outfile = open('encrypted_Practice.txt', 'w')

code = {'a':'!', 'A': '@', 'b': '#', 'B':'$', 'c':'%', 'C':'^', 'd':'&', 'D':'*', 'e':'(', 'E':')', 'f':'-', 'F':'_', 'g':'=', 
'G':'+', 'h':'<', 'H':'>', 'i':',', 'I':'.', 'j':'?',
'J':'1', 'k':'2', 'K':'3', 'l':'4', 'L':'5', 'm':'6', 'M':'7', 'n':'8', 'N':'9', 'o':'0', 'O':'1!', 
'p':'2@', 'P':'3#', 'q':'4$', 'Q':'5%', 'r':'6^', 'R':'7&', 's':'8*', 'S':'9(', 't':'0)', 'T':'a1', 'u':'b@', 
'U':'c#', 'v':'d$', 'V':'e%', 'w':'f^', 'W':'g&', 'y':'h*', 'Y':'i(', 'x':'j)', 'X':'k1', 'z':'l2', 'Z':'m3'}

for words in infile:
    words = words.strip()

infile.close()

for ch in words:
    if ch in code:
        outfile.write(code[ch])
    else:
        outfile.write(ch)

outfile.close()
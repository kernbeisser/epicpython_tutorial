# imports as needed

def some_func():
    # Regular Expressions - the "re.match" and "re.search" methods
    # a = re.match(pattern, string, optional flags) # general match syntax; "a"
    # is called a match object if the pattern is found in the string, otherwise "a" will be None

mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP."

# importing the regular expressions module
import re

# checking if the characters "You" are indeed at the
# beginning of the string
a = re.match("You", mystr)

# result is 'You'; Python returns the match it found in the string according to
# the pattern we provided
a.group()

# re.I is a flag that ignores the case of the matched characters
a = re.match("you", mystr, re.I)

# general search syntax; searching for a pattern throughout the entire string;
# will return a match object if the pattern is found and None if it's not found
a = re.search(pattern, string, optional flags)

arp = "22.22.22.1      0         b4:a9:5a:ff:c8:45 VLAN# 222             L"

# result is '22.22.22.1'; 'r' means the pattern should be treated like a raw string; any pair of parentheses indicates the start and the end of a group; if a match is found for the pattern inside the parentheses, then the contents of that group can be extracted with the group() method applied to the match object; in regex syntax, a dot represents any character, except a new line character; the plus sign means that the previous expression, which in our case is just a dot, may repeat one or more times; the question mark matching as few characters as possible
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)

# returns all matches found in a given string, in the form of a tuple, where each match is an element of that tuple
a.groups()
('22.22.22.1', '0', 'b4:a9:5a:ff:c8:45 VLAN# 222', 'L')

# Regular Expressions - the "re.findall" and "re.sub" methods
# returns a list where each element is a pattern that was matched inside the target string
a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
# ['22.22.22.1']
# result of the above operation - a list with only one element, the IP address matched by the regex

b = re.sub(r"\d", "7", arp) # replaces all occurrences of the specified pattern in the
# target string with a string you enter as an argument

def main():
    some_func()

if __name__ == '__main__':
    main()

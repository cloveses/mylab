
# This file can be used to test the solution banner.py
# You do not need to submit this file.

from banner import make_banner

# Test case 1
result = make_banner('hello')
print(result)

# Uncomment line below to print blank line for nicer output
#print() 

# Test case 2
result = make_banner('QuickFox')
print(result)

# Uncomment line below to print blank line for nicer output
#print()

# Test case 3
result = make_banner('ZEBRA')
print(result)

# Test case 4, this case must give the following error:
# ValueError: All characters in text must be alphabetic.
result = make_banner('hello123')
print(result)

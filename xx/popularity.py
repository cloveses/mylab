
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work. 
#
#    Student no:    PUT YOUR STUDENT NUMBER HERE
#    Student name:  PUT YOUR NAME HERE
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  POPULARITY CLOUDS
#
#  Movie fans have strong opinions about their favourite actors.  In
#  this task you will develop a program that helps visualise some
#  of the opinions of movie fans derived from a survey of
#  Microsoft employees.  To do so you will make use of three
#  different computer languages, Python, SQLite and HTML.  You
#  will develop a Python function, show popularity, which accesses
#  data in an SQL database and uses this to generate HTML documents
#  which visually display an actor's popularity according to the
#  survey results.  See the instructions accompanying this file for
#  full details.
#
#--------------------------------------------------------------------#



#-----Acceptance Tests-----------------------------------------------#
#
#  This section contains unit tests that run your program.  You
#  may not change anything in this section.  NB: 'Passing' these
#  tests does NOT mean you have completed the assignment because
#  they do not check the HTML files produced by your program.
#
"""
------------------- Normal Cases with valid input --------------------

>>> show_popularity(['Female', 'Male', '30-40'], 20, 'Test01') # Test 1

>>> show_popularity(['20-30', '30-40', '40-50'], 50, 'Test02') # Test 2

>>> show_popularity(['20-40', '40-80', 'All'], 30, 'Test03') # Test 3

>>> show_popularity(['Female', 'Male', '30-40', '40-60', '60-100', 'All'], 30, 'Test04') # Test 4

>>> show_popularity(['All'], 20, 'Test05') # Test 5

>>> show_popularity(['30-40'], 50, 'Test06') # Test 6

>>> show_popularity(['30-50'], 0, 'Test07') # Test 7

------------------- Cases with invalid input ------------------------

>>> show_popularity(['20-30', '30-40', '3a-34' ], 30, 'Test08') # Test 8
Invalid customer group: 3a-34

>>> show_popularity(['teens', '20-20','30-40','40-50', '50-50', '60-d0'], 30, 'Test09') # Test 9
Invalid customer group: teens
Invalid customer group: 60-d0

>>> show_popularity(['old people', '30', '40-60', '-70', '70-100'], 30, 'Test10') # Test 10
Invalid customer group: old people
Invalid customer group: 30
Invalid customer group: -70

>>> show_popularity(['-', '30-50', '40-60', '50-20', '40 60'], 50, 'Test11') # Test 11
Invalid customer group: -
Invalid customer group: 40 60

>> show_popularity(['9-20'], 50, 'TestX')

""" 
#
#--------------------------------------------------------------------#



#-----Students' Solution---------------------------------------------#
#
#  Complete the task by filling in the template below.

# Get the sql functions
from sqlite3 import *


########################## PUT YOUR show_popularity FUNCTION HERE


#
#--------------------------------------------------------------------#



#-----Automatic Testing----------------------------------------------#
#
#  The following code will automatically run the unit tests
#  when this program is "run".  Do not change anything in this
#  section.  If you want to prevent the tests from running, comment
#  out the code below, but ensure that the code is uncommented when
#  you submit your program.
#
if __name__ == "__main__":
     from doctest import testmod
     testmod(verbose=True)   
#
#--------------------------------------------------------------------#

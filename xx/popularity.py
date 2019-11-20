
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
import random


########################## PUT YOUR show_popularity FUNCTION HERE
# select actor,count(*) from favorite_actors where customerID in (select customerID from customers where age=20) group by actor;
# select customerID, count(*) from customers where age=20;
def parse_query(types_lst):
     valid_groups = []
     valid = True
     for tp in types_lst:
          if '-' in tp:
               ages = tp.split('-')
               try:
                    if len(ages) != 2 or not ages[0].isdigit() or not ages[-1].isdigit():
                         raise ValueError('Invalid customer group: %s' % tp)
               except ValueError as e:
                    print(e)
                    valid = False
               else:
                    valid_groups.append(ages)
          else:
               try:
                    if tp not in ('Female', 'Male', 'All'):
                         raise ValueError('Invalid customer group: %s' % tp)
               except ValueError as e:
                    print(e)
                    valid = False
               else:
                    valid_groups.append(tp)
     if not valid:
          return
     return valid_groups

def query_data(valid_group):
     sql_first = 'select count(*) from customers '
     params = tuple()
     if isinstance(valid_group, list):
          if valid_group[0] == valid_group[1]:
               where_part = 'where age=?'
               params = (valid_group[0], )
          else:
               where_part = 'where age >= ? and age <= ?'
               params = tuple(valid_group)
     else:
          if valid_group in ('Female', 'Male'):
               where_part = 'where gender=?'
               params = (valid_group, )
          else:
               where_part = ''

     sql_first += where_part
     sql_second = '''select actor,count(*) as num from favorite_actors where customerID in 
     (select customerID from customers ''' + where_part + ' ) group by actor order by num DESC;'

     # print(sql_first, sql_second)
     return sql_first, sql_second, params

page_content = '''
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
<h2 align="center">Top {} Most Popular Actors</h2>
<h3 align="center">Customer Group:{}</h4>
<h3 align="center">Number of Customers:{}</h4>
<hr color='purple' />
<div align="center">
    {}
</div>
<hr color='purple' />
<div>{}{}</div>
</body>
</html>
'''     

def show_popularity(types_lst, actors_num, name):
     con = connect('movie_survey.db')
     cur = con.cursor()
     valid_groups = parse_query(types_lst)
     # print(valid_groups)
     if valid_groups:
          last_index = len(valid_groups) - 1
          # 生成所有文件名
          file_names = []
          for valid_group in valid_groups:
               fgp = valid_group if isinstance(valid_group, str) else '-'.join([str(i) for i in valid_group])
               file_names.append('_'.join((name, fgp + '.html')))
          # print(file_names)

          for index, valid_group in enumerate(valid_groups):
               sqls = query_data(valid_group)
               # print(sqls)
               cur.execute(sqls[0], sqls[-1])
               peoples = cur.fetchone()[0]
               cur.execute(sqls[1], sqls[-1])
               datas = []
               for data in cur.fetchall()[:actors_num]:
                    datas.append(data)
               # print(peoples, datas)
               popular_max = datas[0][-1]

               datas.sort(key=lambda x: x[0])
               # 人气榜演员名
               main_contents = ''
               for actor, populars in datas:
                    size = int(populars / popular_max * 400 + 100)
                    color = ''.join([hex(random.randint(0,255))[2:] for i in range(3)])
                    # print(color)
                    main_contents += '<span style="font-size:{}%;color:#{}">{}</span>'.format(size, color, actor)

               if index == 0:
                    pre_page = ''
               else:
                    pre_page = '<a href="%s" >%s</a>' % (file_names[index-1], 'Previous page')
               
               if index >= last_index:
                    next_page = ''
               else:
                    next_page = '<a href="%s" style="float:right">%s</a>' % (file_names[index+1], 'Next page')
               fgp = file_names[index][len(name)+1:len(file_names[index])-5]
               with open(file_names[index], 'w') as f:
                    f.write(page_content.format(actors_num, fgp, peoples, main_contents, pre_page, next_page))

               

     

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
     # from doctest import testmod
     # testmod(verbose=True)   
#
#--------------------------------------------------------------------#
     show_popularity(['Male', '30-30', '40-41','All'], 20, 'aaa')
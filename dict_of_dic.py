# Program 1 : Create a function which takes a string from below "cassandra database output" as an argument and returns a dictionary of dictionaries.
# All dictionaries should contain data for each row output from given input. It should be dynamic 
#(i.e. Irrespective number of rows or columns) 
# Key must be First column (i.e key) and Value as a dictionary
# Output sample -- {{'1.1' : {'activation_code': '1000005-1212', 'account_guid': 'null', 'external_id': '1', 'location': '10.0.9.16'}},
#                   {'1.4.' : {'activation_code': '500000551212', 'account_guid': 'null', 'external_id': '5', 'location': '10.0.9.16'}}.....}


# define dbResponse string as main data input 
dbResponse = '''
 key    | account_guid | activation_code | external_id | location
--------+--------------+-----------------+-------------+-----------
    1.1 |         null |    1000005-1212 |           1 | 10.0.9.16
    1.4 |         null |    500000551212 |           5 | 10.0.9.16
    1.6 |         null |    700000551212 |           7 | 10.0.9.16
    1.5 |         null |    400000551212 |           4 | 10.0.9.16
 1.1992 |         null |    157990235555 |   exr498680 | 10.0.9.16
    1.3 |         null |    200000551212 |           2 | 10.0.9.16
 1.2052 |         null |    423838550909 |   exr084213 | 10.0.9.16
 1.2152 |         null |    563626550909 |   exr350970 | 10.0.9.16
 1.1534 |         null |    835749550909 |   exr245191 | 10.0.9.16
  1.161 |         null |    547489550909 |   exr413464 | 10.0.9.16
 1.1955 |         null |    961459478950 |   exr874895 | 10.0.9.16
 1.1812 |         null |    535999550909 |   exr991462 | 10.0.9.16
 1.2153 |         null |    525874550909 |   exr446117 | 10.0.9.16
    1.2 |         null |    300000551212 |           3 | 10.0.9.16
  1.206 |         null |    997141550909 |   exr987098 | 10.0.9.16
  1.101 |         null |    870827550909 |   exr867333 | 10.0.9.16
  1.302 |         null |    938271123405 |   exr989961 | 10.0.9.16
 1.1795 |         null |    360276365614 |   exr498651 | 10.0.9.16
  1.855 |         null |    751409654321 |   exr130325 | 10.0.9.16
 1.1232 |         null |    397846550909 |   exr557906 | 10.0.9.16
    1.8 |         null |    800000551111 |           8 | 10.0.9.16
 1.2072 |         null |    551260550909 |   exr531801 | 10.0.9.16
    1.9 |         null |    900000551111 |           9 | 10.0.9.16
 1.2092 |         null |    379419235555 |   exr993899 | 10.0.9.16
 1.2154 |         null |    916479555555 |   exr465158 | 10.0.9.16
(25 rows)
'''

# storing title values of dbResponse string in list 
dbResponse_key=['key','account_guid','activation_code','external_id','location']

# defined empty dictionary for storing output values
answer_dict={}

# define string taking function for converting string into dictionary
def stringconvert(dbResponse):
  
  # spliting multiline string into single and storing value in val variable
  val=dbResponse.splitlines()
  
  for i in range(len(val)):
    
    # spliting val elements by '|' and storing them on tempval variable
    tempval=val[i].split('|')
    #print(tempval)

    # iterate tempval for getting key value and other elements of splitted string
    for j in range(len(tempval)):
      
      # flitering key value from tempval variable and storing in ans_key variable,also remove whitespace by strip function
      if(j==0):
        ans_key=tempval[j].strip()
        #print(ans_key)
      # storing other elements of tempval list 
      else:
        #print(exp)

        # storing other elements of tempval list into answer_dict dictionary
        answer_dict[ans_key]={dbResponse_key[2]:tempval[2].strip(),dbResponse_key[1]:tempval[1].strip(),dbResponse_key[3]:tempval[3].strip(),dbResponse_key[4]:tempval[4].strip()}

  #print(len(tempval))  
  
  # return answer_dict as return value of function
  return(answer_dict)

print(stringconvert(dbResponse))

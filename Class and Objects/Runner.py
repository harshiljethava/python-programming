from employee import Employee
emp_list=list()
crob=Employee()
prob=Employee()
upob=Employee()
while (True):
	
	print('''
	..............................
	>_ Please select the options :
	1) Create Employee
	2) Update Employee
	3) Print All Employee
	4) Exit the program
	..............................\n
		''')
	option=int(input())
	if(option==1):
		ce=crob.createEmployee()
		emp_list.append(ce)
	elif(option==2):
		print(">_ Enter Employee ID to update information")
		emp_id=int(input())
		ue=upob.updateEmployee(emp_id)
		for dic in emp_list:
			if(dic.keys() == ue.keys()):
				emp_list.remove(dic)
				emp_list.append(ue)
				print("\n>_UPDATED LIST :\n",emp_list) 		
	elif(option==3):
		prob.printEmployee(emp_list)
	elif(option==4):
		print("\nBye bye...")
		exit()
	else:
		print('''>_ Hmmm ! I am not able to understand your requirements !!!
Re-run the program with appropriate options !!! :)''')
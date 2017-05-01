import pprint
class Employee:
	def createEmployee(self):
		emp_dict=dict()
		emp_list=list()
		#print("create count : ",createcount)
		print(">_ Enter Employee ID:")
		emp_id=int(input())
		print(">_ Enter Employee Name:")
		emp_name=input()
		print(">_ Enter Employee Phone [eg : 9876543210]:")
		emp_phone=int(input())
		print(">_ Enter Employee Email:")
		emp_email=input()
		emp_dict[emp_id]={emp_name,emp_phone,emp_email}
		print(">_ Information of ",emp_name," has been stored !!!")
		return emp_dict

	def updateEmployee(self,emp_id):
		emp_dict=dict()
		emp_id=emp_id
		print("\n>_ UPDATING INFORMATION !!!\n")
		print(">_ Enter Employee Name:")
		emp_name=input()
		print(">_ Enter Employee Phone [eg : 9876543210]:")
		emp_phone=int(input())
		print(">_ Enter Employee Email:")
		emp_email=input()
		emp_dict[emp_id]={emp_name,emp_phone,emp_email}
		print(">_ Information of ",emp_name," has been updated !!!")
		return emp_dict 

	def printEmployee(self,emp_list):
		print(">_ All Employee Information ")
		for dic in emp_list:
			pprint.pprint(dic,width=2)
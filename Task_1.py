Employees=[[101,"Arun",25000,"HR"],[102,"Divya",30000,"IT"],[103,"Kiran",35000,"Finance"],[104,"Karthick",22000,"CS"],[105,"Teju",38000,"EEE"]]
print(Employees)
print(Employees[0][1]) #first employee name
print(Employees[1][2]) #second employee salary
print(Employees[4][3])#4th employee dept
Employees[4][2]=28000# update the salary of 5th employee
print(Employees[4])
Employees.append([106,"Anu",36000,"ECE"])
print(Employees)
Employees.pop(1)
print(Employees)
print(Employees.sort())
print(Employees)
print(Employees.reverse())
print(Employees)
print(sorted(Employees))
print(min(Employees))
print(max(Employees))
print(Employees.extend([107,"Arun",40000,"ECE"]))
print(Employees)
print(Employees.count([101,"Arun",25000,"HR"]))



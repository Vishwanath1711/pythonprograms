#eligiblity for the following companies based on the skill set and number of projects
'''infosys
zoho
evry india
TCS
'''
skills=str(input("enter the skills:"))
noofprojects=int(input("enter the number of projects you completed "))
if noofprojects>=4 and skills=="java" or skills=="c":
    print("you are eligible for infosys")
elif noofprojects>=6 and skills=="python":
    print("you are eligible for zoho")
elif noofprojects>=2 and skills=="c++":
    print("you are eligible for evry india")
elif noofprojects>=3 and skills=="javascript":
    print("you are eligible for TCS")
else:
    print("you are not eligible for any of these companies")
    

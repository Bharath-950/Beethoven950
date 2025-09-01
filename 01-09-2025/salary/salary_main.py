from salary_manager import creat_salary,read_all, read_by_salary
from salary_manager import salaries,update,delete_by_salary
def menu():
    message ='''
1 - Create salary
2 - Read All Salary
3 - Read By Salary
4 - Update
5 - Delete
6 - exit
'''
    choice = int(input(message))
    if choice == 1:
        salary = int(input('salary'))
        creat_salary(salary)
    elif choice ==2:
        result_salaries= read_all()
        print("Salaries")  
        for salary in result_salaries:
            print(salary)
    elif choice ==3:
        salary = int(input("seach Salary"))    
        index=read_by_salary(salary)
        if salary == -1:
            print('salary not found')  
        else:
            print(f'Salary is at index {index}')    
       
    elif choice ==4:
        old_salary = int(input("Salary to update"))
        new_salary = int(input('New salary'))
        update(salary,new_salary)
    elif choice ==5:
        salary =int(input("salary to delete"))  
        delete_by_salary(salary)  
    return choice   
def menus():
    print("Salary Management App")
    choice = menu()
    while choice!=6:
        choice = menu()
    print("Thank you for using app") 

menus()      
# creat_salary(1000) 
# creat_salary(2000)
# result=read_all()
# for salary in salaries:
#     print(salary)
# print(read_by_salary(1000))
# print(read_by_salary(4000))
# print(salaries[read_by_salary(8000)])


# update(8000,8500)
# print(read_all())

# delete_by_salary(1000)
# print(read_all())
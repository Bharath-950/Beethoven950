from product_manager import create_product,read_all
from product_manager import update , delete_by_id,read_by_id
from product import Product
def menu():
    message ='''
    The menu choices are
1 - Create product
2 - Read All products
3 - Read By Id
4 - Update
5 - Delete
6 - exit
your choice:'''

    choice = int(input(message))
    if choice == 1:
        name = input("name")
        description=input("description")
        category=input("category")
        tag=input("tag")
        stock=input("stock")
        price=input("price")
        id = -1
        product =Product(id,name,description,category,tag,stock,price)
        create_product(product)
        print("Product created sucessufully")
    elif choice ==2:
        products= read_all()
        print("product")  
        for product in products:
            print(product)
    elif choice ==3:
        id = int(input("ID"))    
        product=read_by_id(id)
        if product == None:
            print('product not found')  
        else:
            print(product)   
       
    elif choice ==4:
        id=int(input('ID'))
        old_product = read_by_id
        if old_product == None:
            print('product not fund')
        else:    
            print(old_product)
        name = input("name")
        description=input("description")
        category=input("category")
        tag=input("tag")
        stock=input("stock")
        price=input("price")
        new_product = Product(id,name,description,category,tag,stock,price)
        update(new_product)
        print("updated successfully")
    elif choice ==5:
        id =int(input("ID"))
        old_product = read_by_id(id) 
        if old_product == None:
            print("Product not fund")
        else:
             print(old_product)
             if input("Are you sure to delete(y/n)?") == "y":
                delete_by_id(id)  
                print("Product delete successfully ")
    return choice   
def menus():
    print("product Management App")
    choice = menu()
    while choice!=6:
        choice = menu()
    print("Thank you for using app") 

menus() 
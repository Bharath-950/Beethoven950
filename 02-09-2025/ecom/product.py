# id , description,category,tag,stock,price
class Product:
    def __init__(self,id ,name ,description,category,tag,stock,price):
        self.id=id
        self.name=name
        self.description=description
        self.category=category
        self.tag=tag
        self.stock=stock
        self.price=price
    def __str__(self):
        return f"[id={self.id},name={self.name},description={self.description},category={self.category},tag={self.tag},stock={self.stock},price={self.price}]"    

    def __repr__(self):
         return self.__str__()
# mobile_IQ = Product(1,"IQZ7","gaming","mobile",'samrt phone',10,18000) 
# Vivo = Product(id=1,name="Vivo",description="camera id good",category="mobile",tag='samrt phone',stock=100,price=21000) 

# print(mobile_IQ)   
# print(Vivo)
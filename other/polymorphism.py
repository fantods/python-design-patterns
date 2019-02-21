# allows for the same function to be used for different types

print(len("duck"))
# 4

print(len([1, 2, 3, 4]))
# 4


# can implement polymorphism with a function
class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 
   
    def language(self): 
        print("Hindi the primary language of India.") 
   
    def type(self): 
        print("India is a developing country.") 
   
class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 
   
    def language(self): 
        print("English is the primary language of USA.") 
   
    def type(self): 
        print("USA is a developed country.") 
  
def poly(obj): 
    obj.capital() 
    obj.language() 
    obj.type() 
   
obj_ind = India() 
obj_usa = USA() 
   
poly(obj_ind) 
# New Delhi is the capital of India.
# Hindi the primary language of India.
# India is a developing country.
poly(obj_usa) 
# Washington, D.C. is the capital of USA.
# English is the primary language of USA.
# USA is a developed country.
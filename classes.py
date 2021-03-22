# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:

  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
   
  #Brad = User(pass the pars)
  #print(Brad.age) //for accessing directly
    
    # Adding Encapsulation of variables... Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
    self._private = 1000 # Encapsulated variables are declares with '_' in the constructor.

  def greeting(self):                                         //any method inside the class will have self coz thats how we access and Brad.greeting is how we call it
      return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
      self.age += 1
 
 #function for encap variable
  def print_encap(self):
      print(self._private)

# Extend class
class Customer(User):       //In python we pass the class as a parameter for inheriting
  # Constructor
  def __init__(self, name, email, age):
      User.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
      self.name = name
      self.email = email
      self.age = age
      self.balance = 0

  def set_balance(self, balance):
      self.balance = balance

  def greeting(self):
      return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'   //overwriting the above fn

#  Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting()) //it can access the parents methods too

brad.has_birthday()
print(brad.greeting())

#Encapsulation -->
brad.print_encap()
brad._private = 800 #Changing for brad
brad.print_encap()

# Method inherited from parent
janet.print_encap() #Changing the variable for brad doesn't affect janets variable --> Encapsulation
janet._private = 600
janet.print_encap()

#Similary changing janet's doesn't affect brad's variable.
brad.print_encap()

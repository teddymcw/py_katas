 # -*- coding: utf-8 -*-


#need to know when to and when not to write classes here though, consult Jack what's his name

#so when you define a class you must know how to inspect it so that you can tell what it involves
#in its environment, just looking at object will let you know more about the basic environment that all python
#objects have then, won't it

#when an instance attribute is called, the attribute itself is called upon, then if nothing is known 
#we look up the classes method, this can be the __mro__ I suppose

#from DaBeaz's Essential Python Reference
class Account(object): 
    num_accounts = 0
    def __init__(self,name,balance): 
        self.name = name 
        self.balance = balance 
        Account.num_accounts += 1
    def __del__(self): 
        Account.num_accounts -= 1
    def deposit(self,amt):
        self.balance = self.balance + amt
    def withdraw(self,amt):
        self.balance = self.balance - amt
    def inquiry(self): 
        return self.balance


#onto subclassing
#When a derived class defines __init__(), the __init__() methods of base classes are not automatically invoked.
#Therefore, it’s up to a derived class to perform the proper initialization
#of the base classes by calling their __init__() methods
import random

class EvilAccount(Account):
    def __init__(self,name,balance,evilfactor):
        Account.__init__(self,name,balance) # Initialize Account
        self.evilfactor = evilfactor 
    def inquiry(self):
        if random.randint(0,4) == 1:
            return self.balance * self.evilfactor
        else:
            return self.balance

#even more subclassing while overwriting other methods, this is a fairly prime example of why 
#subclassing and probably just once should be done only when necessary
#quick note on multiple inheritance: think of method resolution when doing multiple inheritance 
#because this can easily get entangled, especially when there are two namespaces with same name that may
#cross paths at some point when being combined into one Class by multiple inheritance
#to debug the class.__mro__ is often used

#of course notice no __init__ here
class MoreEvilAccount(EvilAccount): 
    def deposit(self,amount):
        self.withdraw(5.00) # Subtract the "convenience" fee EvilAccount.deposit(self,amount) # Now, make deposit

#note on super 
#super(cls, instance) returns a special object that lets you perform attribute lookups on the base classes

class MoreEvilAccount(EvilAccount): #error is redefinition
    def deposit(self,amount):
        self.withdraw(5.00) # Subtract convenience fee super(MoreEvilAccount,self).deposit(amount) 
        super(MoreEvilAccount,self).deposit(amount) # Now, make deposit
        #also note that the syntax of the super function is different in python3




#Dynamic binding: (also sometimes referred to as polymorphism when used in the context of inheritance)
#is the capability to use an instance without regard for its type.
#this relates to mro in that you look in the instance class itself and then start going back up the chain

#Loose Coupling: For example, if you want to make a customized version of an existing object, 
#you can either inherit from it or you can simply create a completely new object that looks and acts 
#like it but is otherwise unrelated.
#This latter approach is often used to maintain a loose coupling of program components.
#EG: For example, code may be written to work with any kind of object whatsoever 
#   as long as it has a certain set of methods. 
#One of the most common examples is with various “file-like” objects defined in the standard library. 
#Although these objects work like files, they don’t inherit from the built-in file object.



#static methods: I still can't think of a time to really use them rather than just defining a class method 
class Foo(object): 
    @staticmethod #the decorator is needed, guess I should now fucking look at what this decorator needs
    def add(x,y):
        return x + y
instantiate = Foo()

x = Foo.add(3,4)   # x = 7
#print(x)
z = instantiate.add(5,6)
print(z)

import time
class Date(object):
    def __init__(self,year,month,day):
        self.year = year 
        self.month = month 
        self.day = day
    @staticmethod 
    def now():
        t = time.localtime()
        return Date(t.tm_year, t.tm_mon, t.tm_day) 
    @staticmethod
    def tomorrow():
        t = time.localtime(time.time()+86400) 
        return Date(t.tm_year, t.tm_mon, t.tm_day)

date = Date(2014, 8, 28)
#print(Date.now()) error here when trying to use the t.tm_day attribute, not sure how to resolve



#this gets even more confusing when deciphering class methods from instance methods 
#mostly a teminology confusion
#Class methods are methods that operate on the class itself as an object




#this is where I stopped on about pg. 125 of Dabeaz's Essential Python Reference 

#properties and descriptor's are mentioned in this chapter
#desciptors are syntactic sugar that let you look up

#the rest might be valuable to know if you're becoming an expert on the language but
#hardly useful at the moment


#a word on using the . operator, whenever you use the .  operator you are looking up a name, 
#there is a slight cost to this don't ya know. Not sure how to avoid this as the book suggests 
#or if there are other things that are less costly but its an interesting perspective I suppose
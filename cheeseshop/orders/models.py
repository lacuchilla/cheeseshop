from django.db import models

#Each "class" is a table in the DB.
#Each row in the table becomes an instance of the class.
#The "ids" are implied and you don't need to add them.

#Cheeseshops
class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    managerFirstName = models.CharField(max_length = 15)
    managerLastName = models.CharField(max_length = 15)
    email = models.EmailField()
    
    #This function is just to identify the shop
    def __str__(self):
        return self.name

#Cheeses
class Item(models.Model):
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    units = models.CharField(max_length=15)
    def __str__(self):
        return self.name

#Details for the whole Order
#Order matters. go figure.
class Order(models.Model):
    orderDate = models.DateField()
    fillDate = models.DateField()
    closedDate = models.DateField()
    totalCost = models.IntegerField()
    #paidFlag = look up how to do booleans
    
    def __str__(self):
        return self.name

#Ordered Cheeses
class OrderedItem(models.Model):
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order)
    quantity = models.IntegerField()



# Some examples of other types
#models.TextField()
#models.DateField()
#models.ManyToManyField([Class])
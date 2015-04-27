#cheese shop functions - will probably break these out into multiple files eventually

#Start with simple data access functions

def getShopList():
	return shopList

def getCheeseList():
	#Only one cheese, sorry
	return "Cheddar"

def getCheeseCost(cheese):
	return 10;

def getOrderStatus(shopId):
	#OPEN|FILLED|CLOSED
	return "FILLED"
	

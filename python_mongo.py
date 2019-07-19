from pymongo import MongoClient

client = MongoClient(host = "localhost", port = 27017)
my_db = client.PyMongo
item_collection = my_db.TesGoItems
staff_collection = my_db.TesGoStaff
logs_collection = my_db.Logs

#item func
def getOneItem(ColumnTitle, ItemToFind):

    getItem = {ColumnTitle : ItemToFind}

    searcher = item_collection.find_one(getItem)
    logs_collection.insert_one({"Action" : "getOneItem", "item searched" : ItemToFind})
    return searcher

def getManyItem(ColumnTitle, ItemToFind):

    getItem = {ColumnTitle : ItemToFind}
    searcher = item_collection.find(getItem)
    logs_collection.insert_one({"Action": "getManyItem", "item searched": ItemToFind})
    return searcher
def insertItem(name, price, stock):
    newItem = {"name": name, "price" : price, "stock" : stock}
    newID = item_collection.insert_one(newItem)
    logs_collection.insert_one({"Action": "insertItem", "item name": name, "item price" : price , "stock " : stock })
    print(str(name) + " added to database, with id: " + str(newID.inserted_id))

def updateStock(ItemToFind, NewStock):
    itemToUpdate = getOneItem("name",ItemToFind )
    newVal = { "$set" : { "stock" : NewStock}}
    logs_collection.insert_one({"Action": "updateStock", "item updated": ItemToFind, "new stock" : NewStock })
    item_collection.update_one(itemToUpdate, newVal)#

def updatePrice(ItemToFind, NewPrice):
    itemToUpdate = getOneItem("name",ItemToFind )
    newVal = { "$set" : { "price" : NewPrice}}
    logs_collection.insert_one({"Action": "updatePrice", "item updated": ItemToFind, "new price": NewPrice})
    item_collection.update_one(itemToUpdate, newVal)

def removeItem(ItemNameToRemove):
    itemToRemove = {"name" : ItemNameToRemove}
    logs_collection.insert_one({"Action": "removeItem", "item removed": ItemNameToRemove})
    item_collection.delete_one(itemToRemove)

def printAllItems():
    items_data = item_collection.find()
    for x in items_data:
        print(x)
#end of item func's
#----------------------------------------------------
#As a store manager, I want to add Staff to the system so that I can keep track of actions taken by which employee
    #add staff
#As a store manager, I want to delete staff from the system so that fired employees can no longer have access to the records
    #delete staff
#As a customer assistant, I want to update my own staff records, so that I can change my surname in case I get married.
    #update staff records
#As a store manager, I want to see all Staff in my store so that I can remember their names.
    #list all staff
#As a store manager, I want to update staff roles so that I can give promotions
    #NEED ROLES ATTRIBUTE
#As a store manager, I want to update staff salary so that I can give financial incentives.  
    #SALARY ATTRIBUTE !
    # ATTRIBUTES NAME, ROLE, SALARY,
def getOneStaff(staffToFind):

    getStaff = {"name" : staffToFind}
    searcher = staff_collection.find_one(getStaff)
    logs_collection.insert_one({"Action": "getOneStaff", "staff queried": staffToFind})
    return searcher

def getManyStaff(ColumnTitle, StaffToFind):

    getStaff = {ColumnTitle : StaffToFind}
    searcher = staff_collection.find(getStaff)
    logs_collection.insert_one({"Action": "getManyStaff", "column searched ": ColumnTitle , "data searched" : StaffToFind})
    return searcher

def insertStaff (name, role, salary):
    newStaff = {"name": name, "role" : role, "salary" : salary}
    newID = staff_collection.insert_one(newStaff)
    logs_collection.insert_one({"Action": "insertStaff", "name": name, "role": role, "salary" : salary})
    print(str(name) + " added to database, with id: " + str(newID.inserted_id))

def updateStaffSalary(staffName, newSalary):
    staffToUpdate = getOneStaff(staffName )
    newVal = { "$set" : { "salary" : newSalary}}
    logs_collection.insert_one({"Action": "updateStaffSalary", "name": staffName, "new salary": newSalary})
    staff_collection.update_one(staffToUpdate, newVal)

def updateStaffRole(staffName, newRole):
    staffToUpdate = getOneStaff(staffName )
    newVal = { "$set" : { "role" : newRole}}
    logs_collection.insert_one({"Action": "updateStaffRole", "name": staffName, "new role": newRole})
    staff_collection.update_one(staffToUpdate, newVal)

def removeStaff(staffNameToRemove):
    staffToRemove = {"name" : staffNameToRemove}
    logs_collection.insert_one({"Action": "removeStaff", "name": staffNameToRemove,})
    staff_collection.delete_one(itemToRemove)

def printAllStaff():
    staffData = staff_collection.find()
    for x in staffData:
        print(x)

searcher = logs_collection.find()
for x in searcher:
    print(x)

print("WELCOME TO TesGo SHOP MANAGMENT SYSTEM")
while True:
    userInput2 = int(input("Type 1 to enter item management \n 2 to enter staff management \n 3 to exit"))
    if userInput2 == 1:
        userInput = int(input("\n 1 to list all items, \n 2 to serch for specific item by its name \n 3 to add new item \n 4 to update item price \n 5 to update item stock \n 6 to remove item from database \n 7 to exit\n"))
        if userInput == 1: # list all items
            printAllItems()
        elif userInput == 2: # search for specific item
            itemName = input("Pease input name of item you search for: ")
            foundItem = getOneItem("name", itemName)
            print(foundItem)

        elif userInput == 3: # add new item
            newItemName = input("Please input item name: ")
            newItemPrice = input("Please input item price: ")
            newItemStock = input("Please input item stock: ")
            insertItem(newItemName, newItemPrice, newItemStock)
        elif userInput == 4: # update item price
            newPriceItem = input("Please enter name if item you want to change price: ")
            newPrice = input("Please enter new price: ")
            updatePrice(newPriceItem,newPrice)
        elif userInput == 5: # update item stock
            newStockItem = input("Please enter name if item you want to change stock: ")
            newStock = input("Please enter new stock: ")
            updateStock(newStockItem, newStock)
        elif userInput == 6: # remove item
            itemToRemove = input("Please enter name if item you want to remove: ")
            removeItem(itemToRemove)
        elif userInput == 7: # exit
            client.close()
            exit("Bye")

    elif userInput2 == 2:
        userInput = int(input("\n 1 to list all staff, \n 2 to serch for staff using name \n 3 to add new staff \n 4 to update staff salary \n 5 to update staff role \n 6 to remove staff from database \n 7 to exit\n"))
        if userInput == 1:  # list all staff
            printAllStaff()
        elif userInput == 2:  # search for specific staff
            staffName = input("Pease input name of staff you search for: ")
            foundStaff = getOneStaff(staffName)
            print(foundStaff)

        elif userInput == 3:  # add new staff
            staffName = input("Please input staff name: ")
            staffRole = input("Please input staff role: ")
            staffSalary = input("Please input staff salary: ")
            insertStaff(staffName, staffRole, staffSalary)

        elif userInput == 4:  # update  staff salary
            newStaffSalary = input("Please enter name of staff you want to edit his salary: ")
            newSalary = input("Please enter new salary: ")
            updateStaffSalary(newStaffSalary, newSalary)
        elif userInput == 5:  # update staff role
            newStaffRole = input("Please enter name of staff member to change his role: ")
            newRole = input("Please enter new role: ")
            updateStaffRole(newStaffRole, newRole)
        elif userInput == 6:  # remove staff
            staffToRemove = input("Please enter name of staff member to remove from database: ")
            removeItem(staffToRemove)
        elif userInput == 7:  # exit
            client.close()
            exit("Bye")
    elif userInput2 == 3:
        client.close()
        exit("Bye")



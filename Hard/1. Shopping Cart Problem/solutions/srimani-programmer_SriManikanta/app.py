from database import database
from datetime import datetime
import random

class Application:
    def __init__(self):
        self.shopName = "GadgetifyWithGSBlr"
        self.shopAddress = "311/5 Akshay nagar, Bangalore, Karnataka, India"
        self.shopPhoneNumber = "+91 9988776655"

    # Application Function that tries to Add the Shopping Cataegory into Database.
    def store(self):
        item = input('Enter your Shopping Item Catageory: ')
        try:
            database.addingShoppingCatageory(item)
            print("Succesfully Added the Item Categeory.")
        except Exception:
            print('Something went wrong while Category is adding.')
            exit(0)

    # Adding Item to the Store Databse from Application
    def addStoreItem(self):
        productId = 'PRD' + str(random.randint(195432, 199546))
        try:
            itemName = input('Enter your Item name: ')
            originalPrice = float(input('Enter Original Price of the product: '))
            discountPrice = float(input('Enter the discount price for the product if not available Enter Rs.0: '))
            weight = input('Enter the weight of the product: ')
            categoryId = input('Enter the Appropriate Category Id based on the product Catageory: ')
            database.addingShoppingItem(productId, itemName, originalPrice, discountPrice, weight, categoryId)
            print('Item Added Succesfully into the Store.')
        except Exception:
            print('Somwthing Went Wrong while item is adding into database')
            exit(0)

    # Application Try to view the Shopping Catageory
    def viewShoppingCategories(self):
        categories = database.getShoppingCategory()
        if(len(categories) > 0):
            print('\t\t Category Id \t\t Shopping Category')
            for data in categories:
                print('\t\t {} \t\t {}'.format(data[0], data[1]))
        else:
            print('No Shopping Categories Found.!')

    # Customer Order Creation
    def createOrder(self):
        name = input('Enter your name: ')
        phone = input('Enter Mobile number: ')
        paymentMethod = ['cash', 'card', 'online']

        method = None
        distance = None
        shippingAddress = None

        while True:
            try:
                method = int(input("Enter Customer payment Method\n 1.Cash\n 2.Card\n 3.Online\n Enter your choice between [1-3]: "))
                if(method < 1 or method > 3):
                    print("Please enter your choice between [1-3]: ")
                    continue
                else:
                    break
            except ValueError:
                print("Please Enter the Integer Value.")
                exit(0)

        deliveryOptions = ['home', 'take away']
        options = None

        while True:
            try:
                options = int(input('Enter your delivery Options\n 1. Home \n 2. Take Away\n Enter your Options between [1-2]: '))
                if(options < 1 or options > 2):
                    print("Please enter your choice between [1-2]: ")
                    continue
                else:
                    break
            except ValueError:
                print("Please Enter the Integer Value.")
                exit(0)

        if(deliveryOptions[options - 1] == 'home'):
            try:
                distance = float(input("Enter your home distance in kilometers from the Store: "))
                if(distance > 50):
                    print('Orders will not be processed more than 50 KMS')
                    return
                if(distance <= 0):
                    print("Please enter a valid distance.")
                    return
            except:
                print("Please Enter a Valid number for distance.")
                exit(0)
        
            shippingAddress = input('Enter your Shipping Address: ')
        elif(deliveryOptions[options - 1] == 'take away'):
            distance = "Not Applicable"
            shippingAddress = 'Not Applicable'
    
        items = database.getShoppingItems('NaN')
        for data in items:
            print('''{} {} : Rs.{} : Rs.{} : Weight:{} : Id: {}'''.format(data[0], data[1], data[2], data[3], data[4], data[5]))

        cartItems = []

        while True:
            item = input('Enter the product id which you want to buy: ')
            quantity = int(input('Enter the number of products/items you want to order: '))
            itemDict = {}
            productName = database.getProductDetails(item)
            itemDict[productName[1]] = quantity
            #print(itemDict)
            cartItems.append(itemDict)

            code = input('Do you want to order another product [y/n]: ')
            if(code.lower() == 'y'):
                del(itemDict)
                continue
            elif(code.lower() == 'n'):
                break
            else:
                print('Please enter a valid code.')
                continue
            
        # print(cartItems)
        orderID = database.customerOrderCreation(name, phone, paymentMethod[method - 1].capitalize(), cartItems, deliveryOptions[options -  1].capitalize(), distance, shippingAddress)
        # print(orderID)
        result = database.getOrderedData(orderID)
        cName = result[0][2]
        cReceiptId = result[0][7]
        cPhoneNumber = result[0][3]
        cShippingAddress = result[0][8]
        cDistance = result[0][6]
        itemNames = list()
        itemQuantity = list()
        
        for item in range(0,len(result)):
            itemNames.append(result[item][1])
            itemQuantity.append(result[item][9])
        
        amount = database.generateBilling(itemNames, itemQuantity)

        finalAmount = amount[0]
        shippingCharges = 0
        if(distance > 5 and distance <= 20):
            shippingCharges = 30
            finalAmount += 30
        elif(distance > 20 and distance <= 50):
            shippingCharges = 60
            finalAmount += 60

        billingTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        orderStatus = "inProgress"
        
        database.finalOrder(cReceiptId, orderID, cName, cPhoneNumber, cShippingAddress, cDistance, finalAmount, amount[1], amount[2], orderStatus, billingTime, paymentMethod[method - 1], deliveryOptions[options - 1], shippingCharges)

        print('#################### ORDER BILLING #########################')

        print('Shop Name: {}'.format(self.shopName))
        print('Shop Address: {}'.format(self.shopAddress))
        print('Shop Contack number: {}'.format(self.shopPhoneNumber))

        print('Order Id: {}'.format(orderID))
        print('Customer Name: {}'.format(cName))
        print('Customer Phone Number: {}'.format(cPhoneNumber))
        
        for i in range(0, len(itemNames)):
            priceResults = database.cursor.execute('''SELECT item_price, discount_price FROM shopping_items WHERE item_name=?''', (itemNames[i], )).fetchone()
            print('Item Name : {} Item Quantity: {} Item Price : {} Discount Price: {}'.format(itemNames[i], itemQuantity[i], priceResults[0], priceResults[1]))

        print('Total Amount to be paid: {}'.format(finalAmount))
        print('Total tax Amount: {}'.format(amount[1]))
        print('Your Savings: {}'.format(amount[2]))
        if(distance > 0):
            print('Total Shipping Charges: {}'.format(shippingCharges))
            print('Shipping Address: {}'.format(cShippingAddress))
            print('Distance: {}'.format(cDistance))

        print('Payment Method Used: {}'.format(paymentMethod[method - 1]))
        print('Your Billing Time: {}'.format(billingTime))
        print('Order Status: {}'.format(orderStatus))

    '''finalOrders
        (receipt_id, order_id, customer_name, phone, customer_address, distance, totalAmount, 
        totaltax, totalSavings, order_status, billingTime, payment_method, delivery_option, shipping_charges)
    '''

    def getCustomerOrderStatus(self, orderId):

        print('#################### ORDER BILLING #########################')

        print('Shop Name: {}'.format(self.shopName))
        print('Shop Address: {}'.format(self.shopAddress))
        print('Shop Contack number: {}'.format(self.shopPhoneNumber))

        result = database.cursor.execute(''' SELECT order_id, customer_name, phone, customer_address, distance,
        totalAmount, totaltax, totalSavings, order_status, billingTime, payment_method, delivery_option, 
        shipping_charges
        FROM finalOrders WHERE order_id=?
        ''', (orderId, )).fetchone()

        print('Order Id: {}'.format(result[0]))
        print('Customer Name: {}'.format(result[1]))
        print('Customer Phone Number: {}'.format(result[2]))
        
        orders = database.cursor.execute('SELECT order_item, order_quantity FROM customer_order WHERE order_id=?',(orderId,)).fetchall()
        if(len(orders) > 0):
            for i in range(0, len(orders)):
                prices = database.cursor.execute('SELECT item_price, discount_price FROM shopping_items WHERE item_name=?', (orders[i][0],)).fetchone()
                print('Item Name : {} Item Quantity: {} Item Price : {} Discount Price: {}'.format(orders[i][0], orders[i][1], prices[0], prices[1]))

        print('Total Amount to be paid: {}'.format(result[5]))
        print('Total tax Amount: {}'.format(result[6]))
        print('Your Savings: {}'.format(result[7]))
        if(result[4].isdigit()):
            print('Total Shipping Charges: {}'.format(result[-1]))
            print('Shipping Address: {}'.format(result[3]))
            print('Distance: {}'.format(result[4]))

        print('Payment Method Used: {}'.format(result[-2]))
        print('Your Billing Time: {}'.format(result[-4]))
        print('Order Status: {}'.format(result[-5]))
    
    # Gives the Customer Ordered Products.
    def getCustomerOrderedproducts(self):

        id = input('Enter your Order Id:')
        result = database.getOrderedData(id)
        print('Customer Name: {}'.format(result[0][2]))
        print('Customer Receipt Id: {}'.format(result[0][7]))
        print('Customer Phone Number: {}'.format(result[0][3]))
        print('Customer Shipping Address: {}'.format(result[0][8]))
        print('Customer House Distance from Office: {}'.format(result[0][6]))
        print('################## CUSTOMER ORDERED PRODUCTS ########################')
        for data in range(0, len(result)):
            print('Product Name: {} \nProduct Ordered Quantity: {}'.format(result[data][1], result[data][9]))

    def viewShoppingItems(self, id):
        items = None
        if id == 0:
            items = database.getShoppingItems('NaN')
        elif id == 1:
            items = database.getShoppingItems("item_name")
        elif id == 2:
            items = database.getShoppingItems("item_price")
        elif id == 3:
            items = database.getShoppingItems('discount_price')
        elif id == 4:
            items = database.getShoppingItems('item_weight')
        elif id == 5:
            items = database.getShoppingItems('category_id')
        
        print('Item Name\t\t\t Item Price\t Docount Price\t Item Weight\t Item Catageory_ID')
        for data in items:
            # print(data)
            print('''{} : Rs.{} : Rs.{} : Weight:{} : Id: {}'''.format(data[1], data[2], data[3], data[4], data[5]))

    def changeOrderStatus(self, id, status):
        result = database.changeStatus(id, status)
        if(len(result) > 0):
            print('Order Id: {}'.format(result[0][0]))
            print('Order Staus: {}'.format(result[0][1]))
            print('Billing Time: {}'.format(result[0][2]))
            print('Total Amount: {}'.format(result[0][3]))
        methods = database.cursor.execute('SELECT payment_mode, delivery_mode FROM orders WHERE order_id=?', (id, )).fetchall()
        if(len(methods) > 0):
            print('Mode of Delivery: {}'.format(methods[0][1]))
            print('Payment Method: {}'.format(methods[0][0]))

    def getOrdersList(self, id):
        data = None
        if(id == 0):
            data = database.listOrders('NaN')
        elif(id == 1):
            data = database.listOrders('order_id') 
        elif(id == 2):
            data = database.listOrders('order_status') 
        elif(id == 3):
            data = database.listOrders('billingTime') 
        elif(id == 4):
            data = database.listOrders('totalAmount') 
        elif(id == 5):
            data = database.listOrders('delivery_option') 
        if(len(data) > 0):
            print('Order Id \t Order Status \t Billing Date and Time \t Total Amount \t Delivery Option \t Payment Methos')
            for i in range(0, len(data)):
                print('{} : {} : {} : {} : {} : {} '.format(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5]))
        else:
            print('No Order data is available.')
            exi(0)
app = Application()

useMode = None

try:
    useMode = int(input('Enter the Category to use to Application \n 1. Vendor Mode \n 2. Customer Mode\n'))
    if(useMode < 1 or useMode > 2):
        print('Please enter the valid mode within range [1-2]')

except ValueError:
    print("Please Enter the Integer Value.")
    exit(0)

if useMode == 1:
    print('################################ WELCOME TO VENDOR MODE ################################')
    print('''
        Enter the Task Number to perform the following task\n
        1. Adding Shopping Catageory
        2. Adding shopping item
        3. View Customer Orders
        4. View Shopping Categories
        5. View Shopping Items
        6. Change Order Status\n
    ''')
    try:
        taskCode = int(input('Enter the task Code within range [1-6]: '))
        # Adding Shopping Catageory
        if(taskCode == 1):
            app.store()
        # Adding Shopping Item
        elif(taskCode == 2):
            
            while True:
                code = input('Are you willing to add Item to the Store[y/n]: ')
                if(code.lower() == 'y'):
                    app.addStoreItem()
                elif(code.lower() == 'n'):
                    exit(0)
                else:
                    print('Please enter a valid code.')

        elif(taskCode == 3):
            sortCode = input('Do you want to Sort the Customer Orders? [y/n]: ')
            if(sortCode.lower() == 'y'):
                try:
                    type = int(input('''Available Sorts and Filters are:
                                        1. Sort and Filetr by Order Id
                                        2. Sort and Filetr by Order Status
                                        3. Sort and Filetr by Billing Date
                                        4. Sort and Filetr by Total Amount
                                        5. Sort and Filetr by Delivery Option
                                        Enter your Filter by Id within [1-5]: '''))
                    if(type < 1 or type > 5):
                        print('Please enter the valid Filter Number.')
                        exit(0)
                    else:
                        app.getOrdersList(type)
                except Exception:
                    print("Please Enter the Integer Value.")
                    exit(0)
            elif(sortCode.lower() == 'n'):
                app.getOrdersList(0)
            else:
                print('Enter the valid Option')
                exit(0)
        # Viewing the Shopping Categories
        elif(taskCode == 4):
            app.viewShoppingCategories()
        # Viewing the Shopping Items
        elif(taskCode == 5):
            sortCode = input('Do you want to Sort the Products? [y/n]: ')
            if(sortCode.lower() == 'y'):
                try:
                    type = int(input('''Available Sorts and Filters are:
                                        1. Sort and Filetr by Item Name
                                        2. Sort and Filetr by Item Price
                                        3. Sort and Filetr by Item Discount Price
                                        4. Sort and Filetr by Item Weight
                                        5. Sort and Filetr by Item Category Id
                                        Enter your Filter by Id within [1-5]: '''))
                    if(type < 1 or type > 5):
                        print('Please enter the valid Filter Number.')
                        exit(0)
                    else:
                        app.viewShoppingItems(type)
                except Exception:
                    print("Please Enter the Integer Value.")
                    exit(0)
            elif(sortCode.lower() == 'n'):
                app.viewShoppingItems(0)
            else:
                print('Enter the valid Option')
                exit(0)
        # Chainging the Order Status
        elif(taskCode == 6):
            id = input('Enter your Order Id: ')
            orderStatus = ['in progress', 'completed', 'canceled']
            status = None

            while True:
                try:
                    status = int(input('Available Status for the Order\n 1. In Progress\n 2. completed\n 3. Canceled\n Enter your status:'))
                    if(status < 1 or status > 3):
                        print('please enter value within range [1-3]: ')
                        continue
                    else:
                        break
                except ValueError:
                    print('Please enter a proper value')
                    exit(0)
            
            app.changeOrderStatus(id, orderStatus[status-1])
    except ValueError:
        print("Please Enter the Integer Value.")
        exit(0)

elif useMode == 2:
    print('################################ WELCOME TO Customer MODE ################################')
    print('''
        Enter the Task Number to perform the following task\n
        1. Order a Product
        2. Order Status
    ''')
    try:
        taskCode = int(input('Enter the task code within range [1-2]:'))
        if(taskCode == 1):
            app.createOrder()
        elif(taskCode == 2):
            id = input('Enter your Order Id: ')
            app.getCustomerOrderStatus(id)
    except ValueError:
        print("Please Enter the Integer Value within range [1-2]")
        exit(0)


database.cursor.close()
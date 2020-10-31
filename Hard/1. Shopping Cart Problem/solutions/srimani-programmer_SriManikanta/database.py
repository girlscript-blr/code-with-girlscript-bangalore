__author__ = "Sri Manikanta."

import sqlite3
import random

class ShoppingDatabase:

    def __init__(self):
        self.connection = sqlite3.connect('shoppingCart.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")

    # Creating the Admin for Adding Shopping Category
    def addingShoppingCatageory(self,category):
        id = category[0:5].upper() + str(random.randint(3987545, 4567843))
        self.cursor.execute("CREATE TABLE IF NOT EXISTS shopping_catageory(category_id TEXT NOT NULL, category_name TEXT NOT NULL)")
        self.cursor.execute("INSERT INTO shopping_catageory(category_id, category_name) VALUES (?, ?)", (id, category))
        self.connection.commit()

    def getCategoryResults(self):
        results = self.cursor.execute('SELECT * FROM shopping_catageory').fetchall()
        for category in results:
            print(category)

    def addingShoppingItem(self, productId, itemName, itemPrice, itemDiscountPrice, itemWeight, itemCategoryId):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS shopping_items(product_id TEXT NOT NULL, item_name text NOT NULL, item_price REAL NOT NULL, discount_price REAL NOT NULL, item_weight TEXT NOT NULL, category_id TEXT NOT NULL)")
        self.cursor.execute("INSERT INTO shopping_items(product_id, item_name, item_price, discount_price, item_weight, category_id) VALUES (?, ?, ?, ?, ?, ?)", (productId, itemName, itemPrice, itemDiscountPrice, itemWeight, itemCategoryId))
        self.connection.commit()

    def getShoppingItems(self, sortOrder):
        if sortOrder == 'NaN':
            result = self.cursor.execute('SELECT * FROM shopping_items').fetchall()
            return result
        elif sortOrder == "item_name":
            result = self.cursor.execute("SELECT * FROM shopping_items ORDER BY item_name").fetchall()
            return result
        elif sortOrder == 'item_price':
            result = self.cursor.execute("SELECT * FROM shopping_items ORDER BY item_price").fetchall()
            return result
        elif sortOrder == 'discount_price':
            result = self.cursor.execute("SELECT * FROM shopping_items ORDER BY discount_price").fetchall()
            return result
        elif sortOrder == "item_weight":
            result = self.cursor.execute("SELECT * FROM shopping_items ORDER BY item_weight").fetchall()
            return result
        elif sortOrder == "category_id":
            result = self.cursor.execute("SELECT * FROM shopping_items ORDER BY category_id").fetchall()
            return result

    def getShoppingCategory(self):
        result = self.cursor.execute("SELECT * FROM shopping_catageory ORDER BY category_name").fetchall()
        return result

    def getOrderDetails(self):
        result = self.cursor.execute('SELECT * FROM customer_order').fetchall()
        if(len(result) > 0):
            for data in result:
                print(data)
    
    def getCustomerOrderDetails(self):
        result = self.cursor.execute('SELECT * FROM orders').fetchall()
        return result

    def getProductDetails(self, id):
        result = self.cursor.execute('SELECT * FROM shopping_items WHERE product_id=?',(id,)).fetchone()
        return result

    def getOrders(self, id):
        result = self.cursor.execute('SELECT * FROM customer_order WHERE order_id=?', (id,)).fetchall()
        return result

    def generateBilling(self, orderedItems, orderedQuantity):

        totalAmount = 0.0
        totalTax = 0.0
        tatalSavings = 0.0

        for i in range(0, len(orderedItems)):
            result = self.cursor.execute('''SELECT item_price, discount_price FROM shopping_items WHERE item_name=?''', (orderedItems[i],)).fetchall()
            # print(result)
            if(result[0][1] > 0):
                # print("Ordered Quantity: {}".format(orderedQuantity[i]))
                totalAmount = totalAmount + (result[0][1] * orderedQuantity[i])
                tatalSavings += ((result[0][0] - result[0][1]) * orderedQuantity[i])
                # print(totalAmount)
            else:
                totalAmount += result[0][0]
            
        totalTax = ((totalAmount * 0.06))
        totalAmount = totalAmount + totalTax

        return [totalAmount, totalTax, tatalSavings]

    def getOrderedData(self, order_id):
        result = self.cursor.execute('''SELECT 
            customer_order.order_id, 
            customer_order.order_item, 
            orders.customer_name,
            orders.customer_phone_number,
            orders.payment_mode,
            orders.delivery_mode,
            orders.distance,
            orders.receipt_id,
            orders.shipping_address,
            customer_order.order_quantity
            FROM orders INNER JOIN customer_order ON orders.order_id = customer_order.order_id WHERE orders.order_id=?
        ''',(order_id,)).fetchall()
        return result

    def finalOrder(self, receiptId, order_id, name, phone, address, distance, totalAmount, totalTax, totalSavings, orderStatus, billingTime, paymentMethod, deliveryMethod, shippingCharges):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS finalOrders(receipt_id TEXT NOT NULL PRIMARY KEY, order_id TEXT NOT NULL, customer_name TEXT NOT NULL, phone TEXT NOT NULL, customer_address TEXT NOT NULL, distance TEXT NOT NULL, totalAmount REAL NOT NULL, totaltax REAL NOT NULL,totalSavings REAL NOT NULL, order_status TEXT NOT NULL, billingTime TEXT NOT NULL, payment_method TEXT NOT NULL, delivery_option TEXT NOT NULL, shipping_charges INT NOT NULL)')
        self.cursor.execute('''INSERT INTO finalOrders
        (receipt_id, order_id, customer_name, phone, customer_address, distance, totalAmount, totaltax, totalSavings, order_status, billingTime, payment_method, delivery_option, shipping_charges)
        VALUES
        (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (receiptId, order_id, name, phone, address, distance, totalAmount, totalTax, totalSavings, orderStatus,billingTime, paymentMethod, deliveryMethod, shippingCharges))
        self.connection.commit()

    def customerOrderCreation(self, customerName, customerPhoneNumber, paymentMode, cartItems, deliveryMode, distance, shippingAddress):
        itemsList = list()
        itemsQuantity = list()

        for item in cartItems:
            itemsList.append(list(item.keys()))
            itemsQuantity.append(list(item.values()))
        
        # print(itemsList)
        # print(itemsQuantity)

        orderId = "ORD" + str(random.randint(9843434, 9902349))
        receiptId = 'RECP' + str(random.randint(73243453, 79493343))
        
        self.cursor.execute('CREATE TABLE IF NOT EXISTS receipts(receipt_id TEXT NOT NULL PRIMARY KEY, customer_name TEXT NOT NULL)')

        self.cursor.execute('CREATE TABLE IF NOT EXISTS customer_order(order_id TEXT NOT NULL, order_item TEXT, order_quantity INT, receipt_id TEXT NOT NULL, FOREIGN KEY(receipt_id) REFERENCES receipts(receipt_id))')
        
        self.cursor.execute('INSERT INTO receipts(receipt_id, customer_name) VALUES (?, ?)', (receiptId, customerName))

        customerData = []
        
        for i in range(0, len(itemsList)):
            data = []
            data.append(orderId)
            data.append(itemsList[i][0])
            data.append(itemsQuantity[i][0])
            data.append(receiptId)
            customerData.append(tuple(data))
            del(data)

        print(customerData)
        # (orderId, itemsList[i][0], itemsQuantity[i][0])

        self.cursor.executemany('INSERT INTO customer_order(order_id, order_item, order_quantity, receipt_id) VALUES (?, ?, ?, ?)', customerData)
        self.connection.commit()
        del(customerData)
        print('Sucess.!')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS orders(customer_name TEXT NOT NULL, customer_phone_number TEXT NOT NULL, payment_mode TEXT NOT NULL, delivery_mode TEXT NOT NULL, distance INTEGER NOT NULL, shipping_address TEXT NOT NULL, order_id TEXT NOT NULL, receipt_id TEXT NOT NULL, FOREIGN KEY(receipt_id) REFERENCES receipts(receipt_id))')
        self.cursor.execute('INSERT INTO orders(customer_name, customer_phone_number, payment_mode, delivery_mode, distance, shipping_address, order_id, receipt_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (customerName, customerPhoneNumber, paymentMode, deliveryMode, distance, shippingAddress, orderId, receiptId))
        self.connection.commit()
        print("Success.!")

        return orderId

    def customerOrderStatus(self, orderId, orderStatus):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS order_status(order_id TEXT NOT NULL, order_status TEXT NOT NULL)')
        self.cursor.execute('INSERT INTO order_status(order_id, order_status) VALUES (?, ?)', (orderId, orderStatus))
        self.connection.commit()

    def getOrderStatus(self):
        result = self.cursor.execute('SELECT * FROM order_status').fetchall()
        return result

    def changeStatus(self, id, status):
        self.cursor.execute('''UPDATE finalOrders
        SET order_status=?
        WHERE order_id=?''', (status, id))
        self.connection.commit()
        
        result = self.cursor.execute('''SELECT order_id, order_status, billingTime, totalAmount FROM finalOrders
        WHERE order_id=?''', (id, )).fetchall()
        return result
    '''
    INSERT INTO finalOrders
        (receipt_id, order_id, customer_name, phone, customer_address, distance, totalAmount,
         totaltax, totalSavings, order_status, billingTime, payment_method, delivery_option)
    '''
    def listOrders(self, sortOrder):
        result = None
        if(sortOrder == 'NaN'):
            result = database.cursor.execute('SELECT order_id, order_status, billingTime, totalAmount, delivery_option, payment_method  FROM finalOrders').fetchall()
        elif(sortOrder == 'order_id'):
            result = database.cursor.execute('SELECT order_id, order_status, billingTime, totalAmount, delivery_option, payment_method  FROM finalOrders ORDER BY order_id').fetchall()
        elif(sortOrder == 'order_status'):
            result = database.cursor.execute('SELECT order_id, order_status, billingTime, totalAmount, delivery_option, payment_method  FROM finalOrders ORDER BY order_status').fetchall()
        elif(sortOrder == 'billingTime'):
            result = database.cursor.execute('SELECT order_id, order_status, billingTime, totalAmount, delivery_option, payment_method  FROM finalOrders ORDER BY billingTime').fetchall()
        elif(sortOrder == 'totalAmount'):
            result = database.cursor.execute('SELECT order_id, order_status, billingTime, totalAmount, delivery_option, payment_method  FROM finalOrders ORDER BY totalAmount').fetchall()
        elif(sortOrder == 'delivery_option'):
            result = database.cursor.execute('SELECT order_id, order_status, billingTime, totalAmount, delivery_option, payment_method  FROM finalOrders ORDER BY delivery_option').fetchall()

        return result

database =  ShoppingDatabase()
# database.customerOrderStatus('ORD9858812', "Completed")
# database.getOrderStatus()
# database.getOrderDetails()
# database.getCustomerOrderDetails()
# database.addingShoppingCatageory("Electronics")
# database.getCategoryResults()
# database.addingShoppingItem('ORD197732','Apple Macbook Pro', 191000, 189000, '2.0KG', 'ELECT4002239')
# database.getShoppingItems('item_weight')
# cartItems = [{"One Plus 8 Pro": 3}]
# database.customerOrderCreation("ABC", "9912575995", "Card", cartItems, "Home", 25, "Hyderabad")
# database.getShoppingCategory()
# database.cursor.execute('DROP TABLE finalOrders')
# database.connection.commit()
# database.cursor.close()

# print(database.cursor.execute('SELECT * FROM finalOrders').fetchall())


# Usage Simulations

<!-- Screenshots here -->
<details>
    <summary>Vendor Side</summary>
    <ul>
    <li>
    <details>
      <summary>Vendor Site Workflow</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063306-832cdb80-cb87-11ea-97f3-c5cb4c5f744e.gif" alt="Peek 2020-07-21 18-26">
    </details>
    </li>
    <li>
    <details>
      <summary>Category Modification</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063297-81fbae80-cb87-11ea-9934-caebfde1d554.gif" alt="Peek 2020-07-21 18-28">
    </details>
    </li>
    <li>
    <details>
      <summary>Item Modification</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063289-8031eb00-cb87-11ea-843e-76be5823c366.gif" alt="Peek 2020-07-21 18-30">
    </details>
    </li>
    <li>
    <details>
      <summary>Order Status Change</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063223-6b555780-cb87-11ea-8df9-7c501416c883.gif" alt="Peek 2020-07-21 18-55">
    </details>
    </li>
    <li>
    <details>
      <summary>Order Listing and Filtering</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063222-6a242a80-cb87-11ea-84e4-11ab897221d4.gif" alt="Peek 2020-07-21 18-56">
    </details>
    </li>
    <ul>
</details>

<details>
    <summary>Customer Side</summary>
    <ul>
    <li>
    <details>
      <summary>Site Workflow</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063260-75775600-cb87-11ea-8a22-7aeb33e543dc.gif" alt="Peek 2020-07-21 18-35">
    </details>
    </li>
    <li>
    <details>
      <summary>Item Quantity Update Validation</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063286-7e682780-cb87-11ea-8475-82d7c6c7b1df.gif" alt="Peek 2020-07-21 18-34">
    </details>
    </li>
    <li>
    <details>
      <summary>Checkout Validation</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063251-7314fc00-cb87-11ea-992e-f3510dea4c23.gif" alt="Peek 2020-07-21 18-45">
    </details>
    </li>
    <li>
    <details>
      <summary>Sample Bill Screenshot</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88069487-23d2c980-cb8f-11ea-98cd-80f4e56f4a49.png" alt="Screenshot 2020-07-21 20-17">
    </details>
    </li>
    <li>
    <details>
      <summary>Bill Generation and Regeneration</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063230-6c868480-cb87-11ea-9977-87e3609a8496.gif" alt="Peek 2020-07-21 18-49">
    </details>
    </li>
    <li>
    <details>
      <summary>Order Status Checking</summary>
      <img src="https://user-images.githubusercontent.com/39518771/88063207-67293a00-cb87-11ea-94c7-e03e2e8beab9.gif" alt="Peek 2020-07-21 18-57">
    </details>
    </li>
    </ul>

</details>

# Local testing

1. Make sure you're in the correct directory:

```
/code-with-girlscript-bangalore/Hard/1. Shopping Cart Problem/solutions/chttrjeankr_Ankur_Chattopadhyay/
```

2. Run `pip install -r requirements.txt` to install Django

3. Prepare Django app by

```
python manage.py makemigrations
python manage.py migrate
```

4. Create Vendor Admin by

```
python manage.py createsuperuser
```

and enter `username`, `email` and `password` for Vendor

5. Run Django app by

```
python manage.py runserver
```

6. Go to `127.0.0.1:8000` to use the shopping app as customer

7. Go to `127.0.0.1:8000/admin` to use the shopping app as vendor

# Approach

- Django Admin is used as a Vendor interface
- Customer's website has 3 main options:
  - Browsing categories
  - Checkout with Order
  - Check order status
- `Item` and `Category` details by Vendor are stored in `sqlite3` DB which may be modified without much changes in logic of application.
- `Order` details are partially stored in the `sqlite3` DB and the details of the items purchased in the order are stored as JSON in `/shoppingcart/order_invoices/` directory with `order_<id>.json` filename.

  > Foreign keys are not used as change in Item details by the vendor post purchase, would lead to change in already processed order details and also in already generated bills, which would be highly inconvenient.

  > Cart data is stateless, until the order is finalized.

- `order_directory`, `shop_details` and `delivery_cost` are stored separately that can be changed whenever needed as per the vendor's discretion.

# Usage Simulations

<!-- Screenshots here -->

<details>
  <summary>Site Workflow</summary>
  <img src="https://user-images.githubusercontent.com/39518771/87249195-35bfb880-c47b-11ea-93ee-c75d82a285ec.gif" alt="Peek 2020-07-12 19-54">
</details>

<details>
  <summary>Item Quantity Validation</summary>
  <img src="https://user-images.githubusercontent.com/39518771/87249194-35272200-c47b-11ea-8e1c-881a2cd54622.gif" alt="Peek 2020-07-12 19-57">
</details>

<details>
  <summary>Clear Cart feature</summary>
  <img src="https://user-images.githubusercontent.com/39518771/87249193-33f5f500-c47b-11ea-8880-19708dc79dab.gif" alt="Peek 2020-07-12 19-58">
</details>

<details>
  <summary>Shipping Distance Validation</summary>
  <img src="https://user-images.githubusercontent.com/39518771/87249192-32c4c800-c47b-11ea-9c01-49f9cea695de.gif" alt="Peek 2020-07-12 20-00">
</details>

<details>
  <summary>Sample Bill Screenshot</summary>
  <img src="https://user-images.githubusercontent.com/39518771/87249460-d793d500-c47c-11ea-86de-2e7e3a69cf20.png" alt="Screenshot 2020-07-12 20-18">
</details>

<details>
  <summary>Bill Regeneration</summary>
  <img src="https://user-images.githubusercontent.com/39518771/87249191-30626e00-c47b-11ea-9a9e-99cadc140632.gif" alt="Peek 2020-07-12 20-02">
</details>

# Local testing

1. Make sure you're in the correct directory:

```
/code-with-girlscript-bangalore/Medium/1. Shopping Cart Problem/solutions/chttrjeankr_Ankur_Chattopadhyay/
```

2. Run `pip install -r requirements.txt` to install Flask

3. Run flask app by

```
export FLASK_APP=app.py
flask run
```

4. Go to `127.0.0.1:5000` to use the shopping app

# Approach

- `shopping_list`, `shop_details` and `delivery_cost` are stored separately that can be changed whenever needed
- User needs to go to shopping list to add items into cart
- Checkout page consists of a form where users can enter information
- Once the user submits the form, the function `app.get_bill()` calculates total bill
- Bill is generated at the backend after necessary validations and calculation of tax, discounts and delivery charges (if any)
- Generated bill can be printed by user
- Bill is rendered in an HTML template which separates concerns in different `<div>` tags

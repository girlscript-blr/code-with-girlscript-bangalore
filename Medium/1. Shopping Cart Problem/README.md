# Shopping Cart Problem - Medium

> Date : 1st July 2020

## Prerequisites
- Basic input output of strings and numbers.
- Basic conditional statements.
- One of `Class`/`Object`/`Dictionary`/`Map` to store shopping items. (Depends on the language you are using)
- Creating, displaying & manipulating arrays.
- Basic calculation.
- Getting the current date & time and displaying it in human readable form.

## Problem Statement

In this section, `GadgetifyWithGSBlr` allows the customer to enter details as per the input specified. An additional parameter(distance) is added in this section that has to be taken into account for calculating the delivery charges. The app has to generate a bill accordingly containing all the details provided by the user and the total amount.

- There should be a static list of shopping items along with their name, original price, discount price (if any), and weight in grams. (Total items >= 5, Discount items >=2)

  Example:

  ```
  Name: Basshead earphones, Original Price: Rs. 1200, Discount price: Rs. 899, Weight: 150g
  Name: Bluetooth computer mouse, Original Price: Rs. 600, Discount price: Rs. 499, Weight: 120g
  ```

- When the application runs, the user must be asked the following.
  - Name
  - Phone no
  - Payment method `(cash/card/online)`
  - Select multiple shopping item and it’s quantity.
    `For Example, the user can select 3 basshead earphones & 2 bluetooth computer mouse`
  - Takeaway / Home delivery
  - Distance from shop to the delivery address in KM. (if Home delivery is selected)
  - Shipping address (if Home delivery is selected)
- The shop doesn’t provide home delivery to addresses more than 50KM away. If the user selects more than 50KM, an appropriate message should be displayed.
- While listing the shopping items, the application should display the original price, discount price, and the amount saved by the user if he/she buys that product.
- The app should generate a bill for the selected item, including a 6% tax on the total amount.
- The total amount should include a shipping charge if Home delivery is selected. The shipping charge is to be calculated as:
  | Distance | Price |
  |----------|-------------|
  | <= 5 KM | Free |
  | <= 20 KM | Rs. 30 |
  | <= 50 KM | Rs. 60 |
  | > 50 KM | No delivery |
- The bill should show the total amount saved by the user if he/she bought any discounted products.
- The bill should contain all the details provided by the user.
- The bill should contain the shop details as well as the billing date and time.

### Inputs

Input can be in any format or variation but it must include the following.

- Name
- Phone no
- Payment method (cash/card/online)
- Selected items and it's quantity
- Takeaway / Home delivery
- Distance from shop to the delivery address in KM. (if Home delivery is selected)
- Shipping Address (if Home delivery is selected)

### Output

Output will be a bill based on the given input. The bill can be in any format but it must include the following

#### Static data

- Shop name: `GadgetifyWithGSBlr`
- Shop address: `311/5 Akshay nagar, Bangalore, Karnataka, India`
- Shop contact no: `+91 9988776655`

#### Variable data

- Customer name
- Customer phone no
- Items bought, it's quantity, price & discount price
- Total tax
- Total shipping charge (if Home delivery is selected)
- Total amount saved
- Sum amount to be paid
- Payment method used
- Billing date and time
- Shipping Address (if Home delivery is selected)

## Requirements for submission

- Last Submission Date : `30th July 2020`

## How to submit solution?

Follow the steps mentioned in [this](../../CONTRIBUTING.md) file to submit your solution.

## Stuck somewhere?

Then you might want to solve these versions of the problem first.

- [Easy](../../Easy/1.%20Shopping%20Cart%20Problem/README.md)

## Next steps

Solved this problem? Then you might want to checkout the other versions of this problem.

- [Hard](../../Hard/1.%20Shopping%20Cart%20Problem/README.md)

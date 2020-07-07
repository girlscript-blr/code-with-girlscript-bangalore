# Usage Presentation

<!-- Screenshots here -->
### Site Preview
> ![Peek 2020-07-07 18-13](https://user-images.githubusercontent.com/39518771/86783492-00cbf400-c07e-11ea-8ebe-435c317577ee.gif)

### Creating an order
> ![Peek 2020-07-07 18-17](https://user-images.githubusercontent.com/39518771/86783636-353fb000-c07e-11ea-85c5-1de96e65955b.gif)

### Generated bill
> ![Screenshot from 2020-07-07 18-15-40](https://user-images.githubusercontent.com/39518771/86783480-fc9fd680-c07d-11ea-8e8d-3362e3d4b11a.png)


# Local testing

1. Make sure you're in the correct directory:

```
/code-with-girlscript-bangalore/Easy/1. Shopping Cart Problem/solutions/chttrjeankr_Ankur_Chattopadhyay/
```

2. Run `pip install -r requirements.txt` to install Flask

3. Run flask app by

```
export FLASK_APP=app.py
flask run
```

4. Go to `127.0.0.1:5000` to use the shopping app

# Approach

- `shopping_list` and `shop_details` are stored separately that can be changed whenever needed.
- A simple HTML form for inputting customer's choices is generated dynamically based on the `shopping_list`
- Once the user submits the form, the function `app.get_bill()` calculates total bill according to the given criteria in the problem statement.
- Bill is rendered in an HTML template which separates concerns in different `<div>` tags.

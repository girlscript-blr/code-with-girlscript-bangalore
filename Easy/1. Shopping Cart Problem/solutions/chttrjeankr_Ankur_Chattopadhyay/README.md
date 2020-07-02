# Usage Presentation

<!-- Screenshots here -->

# Local testing

1. Make sure you're in the correct directory:

```/code-with-girlscript-bangalore/Easy/1. Shopping Cart Problem/solutions/chttrjeankr_Ankur_Chattopadhyay/

```

2. Run `pip install -r requirements.txt` to install Flask

3. Run flask app by

```
export FLASK_APP=app.py
flask run
```

3. Go to `127.0.0.1:5000` to use the shopping app

# Approach

- `shopping_list` and `shop_details` are stored separately that can be changed whenever needed.
- A simple UI form for inputting customer's choices is generated dynamically based on the `shopping_list`
- Once the user submits the form, the function `app.get_bill()` calculates total bill according to the given criteria in the problem statement.
- Bill is returned in a JSON serialized form, which can be further used in any way the designer likes.

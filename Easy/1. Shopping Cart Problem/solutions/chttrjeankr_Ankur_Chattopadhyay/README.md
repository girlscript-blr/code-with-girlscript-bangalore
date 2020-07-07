# Usage Presentation

<!-- Screenshots here -->
### Site Preview
> ![Peek 2020-07-02 18-15](https://user-images.githubusercontent.com/39518771/86363747-e87e6280-bc94-11ea-9aef-8433f4f809b3.gif)

### Creating an order
> ![Peek 2020-07-02 18-09](https://user-images.githubusercontent.com/39518771/86363724-e2888180-bc94-11ea-9439-8d2143cfdf06.gif)

### Generated bill
> ![Screenshot from 2020-07-02 18-11-45](https://user-images.githubusercontent.com/39518771/86363756-eae0bc80-bc94-11ea-985f-04f3d5307154.png)


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

# COVID-19 Food Supply App - Medium

> Date : 1st September 2020

## Prerequisites

- Basic input output of strings and numbers.
- One of `Class`/`Object`/`Dictionary`/`Map` to store survey details. (Depends on the language you are using)
- Creating and displaying arrays.
- Basic calculation.

## Problem Statement

Mr. Banku Yadav has just started with his NGO. During this Covid-19 pandemic, he decided to do a fundraiser to help the people in need. He found a slum nearby named Nayandahalli where he saw people who were in need of food and ration kits.

Before starting with the fundraiser he thought of exploring the slum and thereby conducted a survey. When Banku Yadav reached Nayandahalli he found out that there were a lot of people and collecting each and everyone’s record manually would become a tedious process. So he thought of creating an app that will make his task easier in conducting the survey. Banku Yadav is not a tech-savvy person to build a survey app.

It is your time to rise and shine as you have a golden opportunity to help Banku Yadav create an app for conducting his survey. Your task is to help Banku Yadav in estimating the quantity of each food item along with its price and the total amount required to be funded based on the total number of people. Refer the sample input and output examples given below to create your app.

#### Monthly Food Stock:

| Product                             | Price(in Rs.) | Monthly Quantity | Total Quantity            |
| ----------------------------------- | ------------- | ---------------- | ------------------------- |
| Rice 1Kg                            | 40            | 30               | Survey results X 30       |
| Dal 1Kg                             | 65            | 30               | Survey results X 30       |
| Cerelac 1 pack                      | 140           | 3                | Survey results X 3        |
| Amul powder 1Kg                     | 240           | 1                | Survey results            |
| Nandini Milk TetraPacks 1lt         | 45            | 8                | Survey results X 8        |
| Bread loaf 1pack                    | 25            | 4                | Survey results X 4        |
| Tiger/Parle G Biscuits 5pieces Pack | 3             | 30               | Survey results X 30       |
| Canned Veggies                      | 100           | 4                | Survey results X 4        |
| Canned Fruits                       | 100           | 4                | Survey results X 4        |
| Medicine Packs                      | 500           | 1                | Survey results            |
| Calcium Sandoz Tablets              | 500           | 1                | As per the survey results |

### Note

> - **Survey results** are as per Required Quantity
> - **Required Quantity** is the total number of food items(in kg or number of units) selected by each individual on taking the Survey.
> - **Monthly Quantity** is the total number of Food item packets to be distributed to an individual for a Month/30 days.

### Inputs

App should allow the user to fill **multiple surveys for multiple users**. Input can be in any format or variation but it must include the following.

- Aadhar Card Number:
- Name:
- Gender: (3 Options: Male, Female, Other)
- Age:
- How much rice in grams he/she eats per day?:
- How much dal in grams he/she eats per day?:
- Any 2 special food item required to be chosen from choices: (choices should be based on Age & Gender selected)

| Age Group                            | Special Food Options                                                           |
| ------------------------------------ | ------------------------------------------------------------------------------ |
| Infants: Below 2years                | Cerelac, Amul powder, Nandini Milk TetraPacks                                  |
| Children: Between 3 to 18 years      | Bread, Tiger/Parle G, Nandini Milk TetraPacks, Canned Fruits, Canned Veggies   |
| Old Age: Above 70 years              | Canned Fruits, Canned Veggies, Nandini Milk TetraPacks, Medicine Packs         |
| Adult Female: Between 18 to 69 years | Canned Fruits, Canned Veggies, Nandini Milk TetraPacks, Calcium Sandoz Tablets |
| Adult Male: Between 18 to 69 years   | Canned Fruits, Canned Veggies, Nandini Milk TetraPacks                         |
| Adult Other: Between 18 to 69 years  | Canned Fruits, Canned Veggies, Nandini Milk TetraPacks, Calcium Sandoz Tablets |

### Output

#### Person Info:

| Age Group                            | No. of People |
| ------------------------------------ | ------------- |
| Infants: Below 2years                | ?             |
| Children: Between 3 to 18 years      | ?             |
| Old Age: Above 70 years              | ?             |
| Adult Female: Between 18 to 69 years | ?             |
| Adult Male: Between 18 to 69 years   | ?             |
| Adult Other: Between 18 to 69 years  | ?             |

#### Food Info:

| Food Item               | Required Quantity | Monthly Quantity | Price (in Rs.) |
| ----------------------- | ----------------- | ---------------- | -------------- |
| Rice in Kg per day      | ?                 | ?                | ?              |
| Dal in Kg per day       | ?                 | ?                | ?              |
| Cerelac                 | ?                 | ?                | ?              |
| Amul powder             | ?                 | ?                | ?              |
| Nandini Milk TetraPacks | ?                 | ?                | ?              |
| Bread                   | ?                 | ?                | ?              |
| Tiger/Parle G Biscuits  | ?                 | ?                | ?              |
| Canned Veggies          | ?                 | ?                | ?              |
| Canned Fruits           | ?                 | ?                | ?              |
| Medicine Packs          | ?                 | ?                | ?              |
| Calcium Sandoz Tablets  | ?                 | ?                | ?              |

#### Total Amount Required = Sum of Prices

### Note

> - **Person Info Table** should display the number of people as per their age category.
> - In the **Food Info Table**, the **Required Quantity** is the sum of number of food items(in kg or number of units) selected by each individual on taking the Survey.
>   - Calculate the following by referring to the **Monthly Food Stock Table**(as above)
>     - **Quantity** = Required Quantity as per Survey X No. of Packets per Food Item
>     - **Price** = Required Quantity X Monthly Quantity X Price from Monthly Food Stock
> - Total Amount can be calculated based on the Sum of Prices in the Food Info Table.

### Example for Calculating Food Info Table & Total Amount Required

After taking survey of 3 Individuals we got to know

- Person A enters or selects
  - 750grams of Rice per day
  - 400grams of Dal per day
  - Nandini Milk TetraPacks
  - Canned Fruits
- Person B enters or selects
  - 500grams of Rice per day
  - 200grams of Dal per day
  - Bread
  - Tiger/Parle G Biscuits
- Person C enters or selects
  - 600grams of Rice per day
  - 250grams of Dal per day
  - Nandini Milk TetraPacks
  - Calcium Sandoz Tablets

#### Food Info:

| Food Item                   | Required Quantity                  | Monthly Quantity | `Price(Rs.) = RequiredQuamtity * Monthly Quantity * Price per unit` |
| --------------------------- | ---------------------------------- | ---------------- | ------------------------------------------------------------------- |
| Rice in Kg per day          | `750+500+600 = 1850grams = 1.85kg` | 30               | `1.85*30*40 = 2220`                                                 |
| Dal in Kg per day           | `400+200+250 = 850grams = 0.85Kg`  | 30               | `0.85*30*65 = 1657.5`                                               |
| Canned Fruits               | 1                                  | 4                | `1*4*100 = 400`                                                     |
| Tiger/Parle G Biscuits      | 1                                  | 30               | `1*30*3 = 90`                                                       |
| Nandini Milk TetraPacks 1lt | 2                                  | 8                | `2*8*45 = 720`                                                      |
| Bread                       | 1                                  | 4                | `1*4*25 = 100`                                                      |
| Calcium Sandoz Tablets      | 1                                  | 1                | `1*1*500 = 500`                                                     |

#### Total Amount Required = Sum of Prices = 2220+1657.5+400+90+720+100+500 = Rs. 5687.5

## Requirements for submission

- A document containing a screenshot showing the results must also be pushed along with final submission. A brief description(not more than 4-5 lines/100 words) should be included containing the approach used for solving the problem.
- Last Submission Date : `30th September 2020`
- If you haven’t filled our [participation form](https://tinyurl.com/codewithgsblr) 📃yet, fill it now.

## How to submit solution?

Follow the steps mentioned in [this](../../CONTRIBUTING.md) file to submit your solution.

## Next steps

Solved this problem? Then you might want to checkout the other versions of this problem.

- [Easy](../../Easy/3.%20COVID-19%20Food%20Supply%20App/README.md)
- [Hard](../../Hard/3.%20COVID-19%20Food%20Supply%20App/README.md)

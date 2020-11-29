# Escapeezy (Event Booking App) - Easy

> Date : 1st December 2020

## Prerequisites

- Basic input output of strings and numbers.
- One of `Class`/`Object`/`Dictionary`/`Map` to store survey details. (Depends on the language you are using)
- Creating and displaying arrays.
- Basic calculation.

## Problem Statement

Mr. Sandeep Kulhari owns an amphitheatre in bangalore. In that amphitheatre he conducts various events and skits. In the pre-covid time, his tickets used to get sold offline. But when the world got hit with covid-19, his work had to be shutted down for a long long time. Due to this,he suffered huge financial stress. Now after eight months of lockdown, Mr. Kulhari got some relief when the government permitted theatres to open.

Despite this good news, Mr. Kulhari is facing some issues with regards to selling his tickets offline, as in this new world everyone is preferring online services. Mr. Kulhari needs your help in developing an application which can help him out in selling his tickets to various events.

### Operation

The app should be able to allow 2 kinds of users to perform 2 operations:

1. Create an Event Hall(Admin)
   Admin should be able to enter the name of the event along with the number of rows & columns to design the seat allocation.

#### Input

- Enter Event Name: String input to enter the event’s name Eg. Janta Circus
- Enter Date & Time of Event: 2nd Dec, 2020
- Number of Rows: 11 (Integer)
- Number of Columns: 15 (Integer)
- Price per Seat in Rs. : 250 (Integer)

#### Output

![Escapeezy Easy Create Event Output](assets/images/escapeezyEasyCreateEventOutput.png)

#### Note

> If Number of Rows exceeds 26, again continue with AA, AB, AC… and so on.

2. Book Seats(Customer)
   Customers should be able to select available seats and the Price to be paid should be calculated as per the number of seats selected.

#### Input

- Enter Number of seats: 2 (Integer)
- Enter Seat Numbers referring below:

![Escapeezy Easy Book Seat Output](assets/images/escapeezyEasyBookSeatOutput.png)

#### Note

> Here **`*`** states that the seat is booked. If you are using a User Interface application then feel free to use different colours or designs as per your wish to differentiate Booked & Available seats.

#### Output

- Display the following message Success scenarios:
  **Seat No. E6, E7 CONFIRMED. Price to be Paid: Rs. 500**
- Display some different error messages as per your choice for Failure scenarios.

## Requirements for submission

- A document containing a screenshot showing the results must also be pushed along with final submission. A brief description(not more than 4-5 lines/100 words) should be included containing the approach used for solving the problem.
- Last Submission Date : `30th December 2020`
- If you haven’t filled our [participation form](https://tinyurl.com/codewithgsblr) 📃yet, fill it now.

## How to submit solution?

Follow the steps mentioned in [this](../../CONTRIBUTING.md) file to submit your solution.

## Next steps

Solved this problem? Then you might want to checkout the other versions of this problem.

- [Medium](../../Medium/6.%Escapeezy/README.md)
- [Hard](../../Hard/6.%Escapeezy/README.md)

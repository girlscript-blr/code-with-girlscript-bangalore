# Escapeezy (Event Booking App) - Hard

> Date : 1st December 2020

## Prerequisites

- Basic input output of strings and numbers.
- One of `Class`/`Object`/`Dictionary`/`Map` to store survey details. (Depends on the language you are using)
- Creating and displaying arrays.
- Basic calculation.
- Reading and writing data to permanent storage. (files, database, etc) Refer [this](http://www.cplusplus.com/doc/tutorial/files/) for using files in C++.
- Complex user interface for implementing different modes and features.

## Problem Statement

Mr. Sandeep Kulhari owns an amphitheatre in bangalore. In that amphitheatre he conducts various events and skits. In the pre-covid time, his tickets used to get sold offline. But when the world got hit with covid-19, his work had to be shutted down for a long long time. Due to this,he suffered huge financial stress. Now after eight months of lockdown, Mr. Kulhari got some relief when the government permitted theatres to open.

Despite this good news, Mr. Kulhari is facing some issues with regards to selling his tickets offline, as in this new world everyone is preferring online services. Mr. Kulhari needs your help in developing an application which can help him out in selling his tickets to various events.

He wants that his app should have the option to add and view new events as an admin, and the customer should be able to book tickets for whichever event they want to attend. He will enter all the details depending on which the app will make seating arrangements and customers will be charged. Kindly have a look on the demands of Mr. Kulhari and help him out!

### Operation

The app should be able to allow the following operations for different users:

1.  Admin Role:

    - Add an Event
      Admin should be able to add events by entering the name of the event along with the number of rows & columns to design the seat allocation for various segments. Event details should be stored in a database or files.

      #### Input

      - Enter Event Name: String input to enter the event’s name Eg. Janta Circus
      - Enter Date & Time of Event: 2nd Dec, 2020 4pm
      - Enter Number of Seat Allocation Segments: 3 (Integer)
        - Enter Name of 1st Segment: Premium
        - Number of Rows: 3 (Integer)
        - Number of Columns: 15 (Integer)
        - Price per Seat in Rs.: 400 (Integer)
        - Enter Name of 1st Segment: Executive
        - Number of Rows: 4 (Integer)
        - Number of Columns: 15 (Integer)
        - Price per Seat in Rs.: 300 (Integer)
        - Enter Name of 1st Segment: Normal
        - Number of Rows: 4 (Integer)
        - Number of Columns: 15 (Integer)
        - Price per Seat in Rs.: 200 (Integer)

      #### Output

      ![Escapeezy Hard Create Event Output](assets/images/escapeezyHardCreateEventOutput.png)

      #### Note

      > If Number of Rows exceeds 26, again continue with AA, AB, AC… and so on.

    - View Multiple Events

      #### Input

      Select the Event to view details: 1. Janta Circus 2. Laxmi Bomb Movie 3. Titanic
      1

      #### Output

      - Event Name: Janta Circus
      - Total Seats Booked in Premium: 16
      - Total Amount Collected from Premium: Rs.6400
      - Total Seats Booked in Executive: 6
      - Total Amount Collected from Executive: Rs.1800
      - Total Seats Booked in Normal: 6
      - Total Amount Collected from Normal: Rs.1200
      - Total Seats Booked: 28
      - Total Amount Collected: Rs.9400

      ![Escapeezy Hard Book Seat Output](assets/images/escapeezyHardBookSeatOutput.png)

2.  Customer Role:

- Book Seats
  Customers should be able to select available seats and the Price to be paid should be calculated as per the number of seats selected in different sections of seat allocation.

#### Input

Select the Event to view details: 1. Janta Circus 2. Laxmi Bomb Movie 3. Titanic
1

- Enter Number of seats for Janta Circus: 2 (Integer)
- Enter Seat Numbers referring below:

![Escapeezy Hard Book Seat Output](assets/images/escapeezyHardBookSeatOutput.png)

#### Note

> Here **`*`** states that the seat is booked. If you are using a User Interface application then feel free to use different colours or designs as per your wish to differentiate Booked & Available seats.

#### Output

- Display the following message Success scenarios:
  **Seat No. E6, E7 CONFIRMED for JANTA CIRCUS**
  **Date & Time: 2nd Dec, 2020 4pm**
  **Price to be Paid: Rs. 600**
- Display some different error messages as per your choice for Failure scenarios.

#### Note

> You can use files or any Database to manipulate the mentioned data

## Requirements for submission

- A document containing a screenshot showing the results must also be pushed along with final submission. A brief description(not more than 4-5 lines/100 words) should be included containing the approach used for solving the problem.
- Last Submission Date : `30th December 2020`
- If you haven’t filled our [participation form](https://tinyurl.com/codewithgsblr) 📃yet, fill it now.

## How to submit solution?

Follow the steps mentioned in [this](../../CONTRIBUTING.md) file to submit your solution.

## Next steps

Solved this problem? Then you might want to checkout the other versions of this problem.

- [Easy](../../Easy/6.%Escapeezy/README.md)
- [Medium](../../Medium/6.%Escapeezy/README.md)

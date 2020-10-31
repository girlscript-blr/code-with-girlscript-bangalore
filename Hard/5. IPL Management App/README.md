# IPL Team Management App - Hard

> Date : 1st November 2020

## Prerequisites

- Basic input output of strings and numbers.
- One of `Class`/`Object`/`Dictionary`/`Map` to store survey details. (Depends on the language you are using)
- Creating and displaying arrays.
- Basic calculation.
- Array filtering.
- Reading and writing data to permanent storage. (files, database, etc) Refer [this](http://www.cplusplus.com/doc/tutorial/files/) for using files in C++.
- Complex user interface for implementing different modes and features.
- Round Robin Algorithm Implementation Java. Refer [this](https://stackoverflow.com/questions/26471421/round-robin-algorithm-implementation-java) (Feel free to search for similar examples in your prefered coding languages).

## Problem Statement

It’s IPL season and we are all pumped about it! The matches on the field are about as competitive as the matches on our Whatsapp groups, with us enthusiastically supporting our favorite teams.

To make the tournament successful, a lot of work and organization is done behind the scene to keep it organized and efficient. Help the BCCI by developing an application that keeps track of **team details, sets up match fixtures, and maintains scores & points table** as the tournament proceeds.

### Inputs

The app should allow the Admin to have 2 roles:

1. **Add Teams** (should be implemented only ones):
   Admin should be able to get a total number of teams playing the tournament, along with team details like the following:

   - Number of Teams playing the tournament:
   - Fill Team1 Details:
     - Name:
     - Captain:
     - Franchise:
     - Home Ground:
   - Fill Team2 Details:
     - Name:
     - Captain:
     - Franchise:
     - Home Ground:
       .
       .
       .
       Soo on till team **n**.

2. **Update Match Results**

- The Generated fixture should be stored in a File/Data table and Admin should be able to update match results after each match.
- Based on the updated match results points should be allocated in another **Points Table**.

### Output

The App should display the following:

1. A Table displaying Team details:

| Sl No. (Autogenerate) | Team Name | Captain | Franchise | Home Ground |
| --------------------- | --------- | ------- | --------- | ----------- |
|                       |           |         |           |             |

2. A Table displaying the fixture of the matches

- Here each team is supposed to play 2 matches with another team, one should be on their home ground another should be on other team’s home ground, i.e. suppose to be an away game for the team.
- Fixture should be created as per [Round Robin Tournament Concept](https://www.youtube.com/watch?v=niXDrhDnGKM).
- Here `Venue` should be the home ground of the Home Team.
- The Table should have additional columns as follows to update match results:
  - **Team Won:** Winning Team name
  - **Result:** Result of the Match _Eg. Chennai Super Kings Won by 21 runs or Kings XI Punbaj Won by 2 wickets or Match Tied but Mumbai Indians won in Super Over_
  - **Man of the Match:** Main performer of the match

| Match Number | Home Team | Away Team | Venue | Team Won | Result | Man of the Match |
| ------------ | --------- | --------- | ----- | -------- | ------ | ---------------- |
|              |           |           |       |          |        |                  |

3. Based on Match Updates a Points table should be generated as follows:

- **2 points** should be awared for every win and **No Points** points for every loss. Matches **won't be tied** as there will be super overs to decide the results.

| Rank | Team Name | No. of Wins | No. of Losses | Points |
| ---- | --------- | ----------- | ------------- | ------ |
|      |           |             |               |        |

### Tables or Files Required

| Sl. No. | Table/ File Name | Description                                                                                                  |
| ------- | ---------------- | ------------------------------------------------------------------------------------------------------------ |
| 1.      | Team Details     | Table/ file containing columns like Team name, Franchise, Captain, Home Ground                               |
| 2.      | Fixtures         | Table/file containing columns like Home Team name, Away Team name, Venue, Team Won, Result, Man of the Match |
| 3.      | Points           | Table/file containing columns Rank, Team name, no. of wins, no. of loss & Points scored                            |

## Requirements for submission

- A document containing a screenshot showing the results must also be pushed along with final submission. A brief description(not more than 4-5 lines/100 words) should be included containing the approach used for solving the problem.
- Last Submission Date : `30th November 2020`
- If you haven’t filled our [participation form](https://tinyurl.com/codewithgsblr) 📃yet, fill it now.

## How to submit solution?

Follow the steps mentioned in [this](../../CONTRIBUTING.md) file to submit your solution.

## Next steps

Solved this problem? Then you might want to checkout the other versions of this problem.

- [Easy](../../Easy/5.%20IPL%20Management%20App/README.md)
- [Medium](../../Medium/5.%20IPL%20Management%20App/README.md)

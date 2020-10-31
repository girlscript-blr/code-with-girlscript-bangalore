# IPL Management App - Medium

> Date : 1st November 2020

## Prerequisites

- Basic input output of strings and numbers.
- One of `Class`/`Object`/`Dictionary`/`Map` to store survey details. (Depends on the language you are using)
- Creating and displaying arrays.
- Basic calculation.
- Array filtering.
- Round Robin Algorithm Implementation Java. Refer [this](https://stackoverflow.com/questions/26471421/round-robin-algorithm-implementation-java) (Feel free to search for similar examples in your prefered coding languages).

## Problem Statement

It’s IPL season and we are all pumped about it! The matches on the field are about as competitive as the matches on our Whatsapp groups, with us enthusiastically supporting our favorite teams.

To make the tournament successful, a lot of work and organization is done behind the scene to keep it organized and efficient. Help the BCCI by developing an application that **registers the teams, sets up the match fixtures and decides on the Home and Away teams** before the tournament begins.

### Inputs

The app should be able to get a total number of teams playing the tournament, along with team details like the following:

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

### Output

The App should display the following:

1. A Table displaying Team details:

| Sl No. (Autogenerate) | Team Name | Captain | Franchise | Home Ground |
| --------------------- | --------- | ------- | --------- | ----------- |
|                       |           |         |           |             |

2. A Table displaying the fixture of the matches

- Here each team is supposed to play 2 matches with another team, one should be on their home ground another should be on other team’s home ground, i.e. suppose to be an away game for the team.
- Fixture should be created as per [Round Robin Tournament Concept](https://www.youtube.com/watch?v=niXDrhDnGKM).
- Here **Venue** should be the home ground of the Home Team.

| Match Number | Home Team | Away Team | Venue |
| ------------ | --------- | --------- | ----- |
|              |           |           |       |

## Requirements for submission

- A document containing a screenshot showing the results must also be pushed along with final submission. A brief description(not more than 4-5 lines/100 words) should be included containing the approach used for solving the problem.
- Last Submission Date : `30th November 2020`
- If you haven’t filled our [participation form](https://tinyurl.com/codewithgsblr) 📃yet, fill it now.

## How to submit solution?

Follow the steps mentioned in [this](../../CONTRIBUTING.md) file to submit your solution.

## Next steps

Solved this problem? Then you might want to checkout the other versions of this problem.

- [Easy](../../Easy/5.%20IPL%20Management%20App/README.md)
- [Hard](../../Hard/5.%20IPL%20Management%20App/README.md)

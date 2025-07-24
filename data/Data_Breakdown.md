# Data Breakdown
TrampOnline produces two separate datasets for any given competition:

## 1. Competitor Dataset
- Contains information on competitors, including their names, club, trampoline (TRI), double-mini trampoline (DMT), tumbling (TUM), and trampoline synchro (TRS) levels, categories, and whether or not they are on a team and/or are a guest.
    - **TRI:**
        - Levels: Novice, Intermediate, Intervanced, Advanced, Elite, and Elite-Pro.
        - Categories: Men, and Women.
    - **DMT:**
        - Levels: 1, 2, 3, 4, 5, and 6.
        - Categories: ?
    - **TUM:**
        - Levels: 1, 2, 3, and 4.
        - Categories: ?
    - **TRS:**
        - Levels: 1, 2, and 3.
        - Categories: ?

## 2. Judge Dataset
- Contains information on judges, including their names, club, level abilities to judge across all TRI judging roles (recorder, marshal, execution, difficulty, synchro, HD, time of flight (ToF), and chair), ability to judge DMT and/or TUM, judging role preferences for TRI only, judging qualifications for all disciplines, the relevant competition, judging availability, and additional notes.

## A Note on the Link Between Both Datasets
Most participants of the competition will likely be in both datasets, however, there is no one unique field that may link the same entries to each other. Relying on the name and club of the participants may be the best option to link data. A duplicate check should be put in place for this reason to account for the unlikely event of two or more people in the same club having the exact same name. In any case, the remainder of this document breaks down the data into the following three categories:
1. Attribute Name
2. Attribute Description
3. Possible Attribute Values
4. Attribute Data Type

## Competitor Dataset Breakdown

### ID
**Attribute Name:** ID

### Name


### Club


### ClassName


### StartOrder



### Discipline


### Team


### Team_Category


### Guest


### flight


### photo_consent
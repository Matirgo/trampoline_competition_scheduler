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
**Attribute Name:** ID.

**Attribute Description:** Five-digit number that acts as the primary key for the dataset. For example, it allows for competitors to have the same name and club. TrampOnline makes use of this to allow the same person to enter multiple disciplines.

**Possible Attribute Values:** 00000 - 99999.

**Attribute Data Type:** Integer (int).

### Name
**Attribute Name:** Name.

**Attribute Description:** The full name of a competitor.

**Possible Attribute Values:** Any combination of Latin letters and common symbols (e.g. ', -, etc.). TrampOnline encodes said symbols. Unclear if numbers can be passed in.

**Attribute Data Type:** String (str).

### Club
**Attribute Name:** Club.

**Attribute Description:** The name or abbreviation of the club, which the competitor will represent at the competition.

**Possible Attribute Values:** Any combination of Latin letters.

**Attribute Data Type:** String (str).

### ClassName
**Attribute Name:** ClassName.

**Attribute Description:** The level of the competitor, followed by the category under which they'll compete. The levels are different depending on the discipline, and category is not present outside of TRI. Competitors may have multiple entries in the dataset if they have signed up to compete in more than one discipline.

**Possible Attribute Values:** There are unique possible attribute values depending on the discipline the ClassName is set to. These are listed below:

- **TRI:** Takes both level and category inputs. There are seven unique levels, and two unique categories. The *"Disability (any category)"* level usually does not take *"Men"* and *"Women"* categories, so the combination of levels and categories amounts to thirteen possible combinations.
    - **Possible levels:**
        1. Novice.
        2. Intermediate.
        3. Intervanced.
        4. Advanced.
        5. Elite.
        6. Elite-Pro.
        7. Disability (any category).
            - **Note:** The *"Disability (any category)"* is manually sorted into levels post hoc if required. It is also usually not a large enough category to justify splitting into Men and Women.
    - **Possible categories:**
        1. Men.
        2. Women.

- **DMT:** Takes only levels, no categories. There are six unique DMT levels.
    1. DMT Level 1.
    2. DMT Level 2.
    3. DMT Level 3.
    4. DMT Level 4.
    5. DMT Level 5.
    6. DMT Level 6.

- **TUM:** Takes only levels, no categories. There are four unique TUM levels.
    1. Tumbling Level 1.
    2. Tumbling Level 2.
    3. Tumbling Level 3.
    4. Tumbling Level 4.

- **TRS:** Takes only levels, no categories. There are four unique TRS levels.
    1. Synchro Level 1.
    2. Synchro Level 2.
    3. Synchro Level 3.
    4. Disability - any category (SYN).

**Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

### StartOrder
**Attribute Name:** StartOrder.

**Attribute Description:** TrampOnline's automatically generated starting order for use with panels. This is currently not widely used in the Irish student trampolining circuit.

**Possible Attribute Values:** 1 - 9999.

**Attribute Data Type:** Integer (int).

### Discipline
**Attribute Name:** Discipline.

**Attribute Description:** The specific event that the competitor has signed up for. There are four unique events that competitors sign up for via TrampOnline, and those are trampoline (TRI), double-mini trampoline (DMT), tumbling (TUM), and synchro (TRS). Competitors may sign up to TRI, DMT, and TUM only once at their specified level, and may sign up to TRS more than once but with different synchro partners. The total amount of signups they are allowed depends on the competition organisers, but is usually capped at two entries.

**Possible Attribute Values:** TRI, DMT, TUM, or TRS.

**Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

### Team
**Attribute Name:**

**Attribute Description:**

**Possible Attribute Values:**

**Attribute Data Type:**

### Team_Category
**Attribute Name:**

**Attribute Description:**

**Possible Attribute Values:**

**Attribute Data Type:**

### Guest
**Attribute Name:**

**Attribute Description:**

**Possible Attribute Values:**

**Attribute Data Type:**

### flight
**Attribute Name:**

**Attribute Description:**

**Possible Attribute Values:**

**Attribute Data Type:**

### photo_consent
**Attribute Name:**

**Attribute Description:**

**Possible Attribute Values:**

**Attribute Data Type:**

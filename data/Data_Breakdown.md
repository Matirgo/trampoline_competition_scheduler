# Data Breakdown
TrampOnline produces two separate datasets for any given competition.

## 1. Competitor Dataset
- Contains information on competitors, including their names, club, trampoline (TRI), double-mini trampoline (DMT), tumbling (TUM), and trampoline synchro (TRS) levels, categories, and whether or not they are on a team and/or are a guest.
    - **TRI:**
        - Levels: Novice, Intermediate, Intervanced, Advanced, Elite, and Elite-Pro.
        - Categories: Men, and Women.
    - **DMT:**
        - Levels: 1, 2, 3, 4, 5, and 6.
    - **TUM:**
        - Levels: 1, 2, 3, and 4.
    - **TRS:**
        - Levels: 1, 2, and 3.

## 2. Judge Dataset
- Contains information on judges, including their names, club, level abilities to judge across all TRI judging roles (recorder, marshal, execution, difficulty, synchro, HD, time of flight (ToF), and chair), ability to judge DMT and/or TUM, judging role preferences for TRI only, judging qualifications for all disciplines, the relevant competition, judging availability, and additional notes.

## A Note on the Link Between Both Datasets
Most participants of the competition will likely be in both datasets, however, there is no one unique field that may link the same entries to each other. Relying on the name and club of the participants may be the best option to link data. A duplicate check should be put in place for this reason to account for the unlikely event of two or more people in the same club having the exact same name. In any case, the remainder of this document breaks down the data into the following three categories:
1. Attribute Name
2. Attribute Description
3. Possible Attribute Values
4. Attribute Data Type

## Competitor Dataset Breakdown

### *ID*
- **Attribute Name:** ID.

- **Attribute Description:** Five-digit number that acts as the primary key for the dataset. For example, it allows for competitors to have the same name and club. TrampOnline makes use of this to allow the same person to enter multiple disciplines.

- **Possible Attribute Values:** 00000 - 99999.

- **Attribute Data Type:** Integer (int).

---

### *Name*
- **Attribute Name:** Name.

- **Attribute Description:** The full name of a competitor.

- **Possible Attribute Values:** Any combination of Latin letters and common symbols (e.g. ', -, etc.). TrampOnline encodes said symbols. Unclear if numbers can be passed in.

- **Attribute Data Type:** String (str).

---

### *Club*
- **Attribute Name:** Club.

- **Attribute Description:** The name or abbreviation of the club, which the competitor will represent at the competition.

- **Possible Attribute Values:** Any combination of Latin letters.

- **Attribute Data Type:** String (str).

---

### *ClassName*
- **Attribute Name:** ClassName.

- **Attribute Description:** The level of the competitor, followed by the category under which they'll compete. The levels are different depending on the discipline, and category is not present outside of TRI. Competitors may have multiple entries in the dataset if they have signed up to compete in more than one discipline.

- **Possible Attribute Values:** There are unique possible attribute values depending on the discipline the ClassName is set to. These are listed below:

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

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *StartOrder*
- **Attribute Name:** StartOrder.

- **Attribute Description:** TrampOnline's automatically generated starting order for use with panels. This is currently not widely used in the Irish student trampolining circuit.

- **Possible Attribute Values:** 1 - 9999.

- **Attribute Data Type:** Integer (int).

---

### *Discipline*
- **Attribute Name:** Discipline.

- **Attribute Description:** The specific event that the competitor has signed up for. There are four unique events that competitors sign up for via TrampOnline, and those are trampoline (TRI), double-mini trampoline (DMT), tumbling (TUM), and synchro (TRS). Competitors may sign up to TRI, DMT, and TUM only once at their specified level, and may sign up to TRS more than once but with different synchro partners. The total amount of signups they are allowed depends on the competition organisers, but is usually capped at two entries.

- **Possible Attribute Values:** TRI, DMT, TUM, or TRS.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *Team*
- **Attribute Name:** Team.

- **Attribute Description:** Indicates whether or not the competitor is part of a team for their club, and if they are, what club that is.

- **Possible Attribute Values:** Any Latin capital letter from A - Z.

- **Attribute Data Type:** String (str).

---

### *Team_Category*
- **Attribute Name:** Team_Category.

- **Attribute Description:** Describes the type of team a competitor is on, be it a regular team, a DMT team, etc. Allows the competition organisers to separate these teams when calculating results.

- **Possible Attribute Values:** Teams, or DMT Teams.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *Guest*
- **Attribute Name:** Guest.

- **Attribute Description:** Indicates whether or not the competitor is a guest competitor for their club. This will either include or exclude their scores from being calculated for who wins the competition cup, shield, etc.

- **Possible Attribute Values:** 0, or 1.
    - 0 indicates that the competitor is not a guest.
    - 1 indicates that the competitor is a guest.

- **Attribute Data Type:** Boolean (bool).

---

### *flight*
- **Attribute Name:** flight.

- **Attribute Description:** Automatically assigned values in-line with the *"StartOrder"* values. Determines what flight the competitor should be on for their category. Is not currently widely used in the Irish student trampolining circuit.

- **Possible Attribute Values:** 1 - 99.

- **Attribute Data Type:** Integer (int).

---

### *photo_consent*
- **Attribute Name:** photo_consent.

- **Attribute Description:** Indicates whether or not the participant has consented to have photos of them taken at the competition.

- **Possible Attribute Values:** 0, or 1.
    - 0 indicates that the competitor has not consented to their photo being taken.
    - 1 indicates that the competitor has consented to their photo being taken.

- **Attribute Data Type:** Boolean (bool).

## Judge Dataset Breakdown

### *id*
- **Attribute Name:** id.

- **Attribute Description:** Five-digit number that acts as the primary key for the dataset. For example, it allows for judges to have the same name and club. Since every judge will only have one entry in this dataset, regardless of their judging capabilities, there is no need for TrampOnline to use this to allow the same person to enter themselves multiple times, although this would allow for it.

- **Possible Attribute Values:** 00000 - 99999.

- **Attribute Data Type:** Integer (int).

---

### *name*
- **Attribute Name:** name.

- **Attribute Description:** The full name of a judge.

- **Possible Attribute Values:** Any combination of Latin letters and common symbols (e.g. ', -, etc.). TrampOnline encodes said symbols. Unclear if numbers can be passed in.

- **Attribute Data Type:** String (str).

---

### *club*
- **Attribute Name:** club.

- **Attribute Description:** The name or abbreviation of the club, which the judge will represent at the competition.

- **Possible Attribute Values:** Any combination of Latin letters.

- **Attribute Data Type:** String (str).

---

### *recorder*
- **Attribute Name:** recorder.

- **Attribute Description:** States if the judge specified their level of competence as a recorder, that is, can they utilise a computer and/or pen and paper to record results as they are called out by the Chair of the Judges' Panel (CJP). This applies to all disciplines.

- **Possible Attribute Values:** There are four options, accounting for the possible combinations of computer and manual recording.
    1. Yes - Computer.
    2. Yes - Manual.
    3. Yes - Either.
    4. No.

    - **Note:** Almost everyone can do recording without any previous exposure to trampoline gymnastics, so an option to allow the competition organisers to overwrite specifications may be beneficial to implement.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *marshal*
- **Attribute Name:** marshal.

- **Attribute Description:** States if the judge specified whether or not they are capable to marshal, that is, can they confirm which competitors are present for a given flight, inform competitors when warm-up time will end, direct competitors to take their one-touch warm-up if they want it, and direct competitors to compete in a timely manner, keeping pace with the panel. This applies to all disciplines.

- **Possible Attribute Values:** Yes, or No.

- **Attribute Data Type:** Str (str), but should be converted into a Boolean (bool).

---

### *judge_form*
- **Attribute Name:** judge_form.

- **Attribute Description:** States if the judge specified their level of competence as an execution judge, that is, can they accurately judge how nice a competitor performs their skills, correctly count up their applied deductions across the routine, and apply any additional deductions as needed, and if so, to what level they would be comfortable judging.

- **Possible Attribute Values:** There are seven attribute levels, accounting for every competitor level, as well as a category stating that the judge is unable and/or unwilling to judge exection at all. They are as follows:
    1. Uber / Pro-Elite / 1.
    2. Elite / 2.
    3. Advanced / 3.
    4. Intervanced / 4.
    5. Intermediate / 5.
    6. Novice / 6.
    7. No.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *judge_difficulty*
- **Attribute Name:** judge_difficulty.

- **Attribute Description:** States if the judge specified their level of competence as a difficulty/tariff judge, that is, can they accurately judge what skills (if any) a competitor has performed, correctly provide a tariff for each skill and a cumulative tariff for the routine, and confirm or deny if the competitor has met the category's requirements for the set and voluntary routines, and if so, to what level they would be comfortable judging.

- **Possible Attribute Values:** There are seven attribute levels, accounting for every competitor level, as well as a category stating that the judge is unable and/or unwilling to judge difficulty/tariff at all. They are as follows:
    1. Uber / Pro-Elite / 1.
    2. Elite / 2.
    3. Advanced / 3.
    4. Intervanced / 4.
    5. Intermediate / 5.
    6. Novice / 6.
    7. No.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *judge_synchro*
- **Attribute Name:** judge_synchro.
 
- **Attribute Description:** States if the judge specified their level of competence as a synchro judge, that is, can they accurately judge how temporally far apart two synchro competitors are from touching the trampoline bed and apply the correct deductions or routine termination decision.

- **Possible Attribute Values:** Yes, or No.

- **Attribute Data Type:** Str (str), but should be converted into a Boolean (bool).

---

### *judge_hd*
- **Attribute Name:** judge_hd.

- **Attribute Description:** States if the judge specified their level of competence as a horizontal displacement (HD) judge, that is, can they accurately judge how far from the centre / into which box the competitor has landed on each of their skills and apply the correct deductions.

- **Possible Attribute Values:** Yes, or No.

- **Attribute Data Type:** Str (str), but should be converted into a Boolean (bool).

---

### *judge_time*
- **Attribute Name:** judge_time.

- **Attribute Description:** States if the judge specified their level of competence as a time of flight (ToF) judge, that is, can they accurately judge how long the competitor has taken to complete their routine, from the beginning of the first skill, to landing their final skill, either via stopwatch or Veriflite.

- **Possible Attribute Values:** Yes, or No.

- **Attribute Data Type:** Str (str), but should be converted into a Boolean (bool).

---

### *judge_chair*
- **Attribute Name:** judge_chair.

- **Attribute Description:** States if the judge specified their level of competence as a chair of judges, that is, can they perform all of the aforementioned judging roles, appropriately enforce the rules of the competition and code of points to both competitors and judges, accurately determine out of how many skills any given routine is, and handle any appeals that may be given, and if so, to what level they would be comfortable chairing.

- **Possible Attribute Values:** There are seven attribute levels, accounting for every competitor level, as well as a category stating that the judge is unable and/or unwilling to judge difficulty/tariff at all. They are as follows:
    1. Uber / Pro-Elite / 1.
    2. Elite / 2.
    3. Advanced / 3.
    4. Intervanced / 4.
    5. Intermediate / 5.
    6. Novice / 6.
    7. No.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *judge_dmt*
- **Attribute Name:** judge_dmt.

- **Attribute Description:** States if the judge specified their level of competence as a DMT judge, that is, can they apply the relevant judging types that they are proficient in to this discipline? Recording and marshalling are the same across disciplines, so these would be applied universally regardless of the answer provided here.

- **Possible Attribute Values:** Yes, or No.

- **Attribute Data Type:** Str (str), but should be converted into a Boolean (bool).

---

### *judge_tum*
- **Attribute Name:** judge_tum.

- **Attribute Description:** States if the judge specified their level of competence as a TUM judge, that is, can they apply the relevant judging types that they are proficient in to this discipline? Recording and marshalling are the same across disciplines, so these would be applied universally regardless of the answer provided here.

- **Possible Attribute Values:** Yes, or No.

- **Attribute Data Type:** Str (str), but should be converted into a Boolean (bool).

---

### *prefer_tri*
- **Attribute Name:** prefer_tri.

- **Attribute Description:** States if the judge has a preferred role to be assigned when judging.

    - **Note:** The judge should be proficient in the type of judging that they indicate they would prefer to do.

- **Possible Attribute Values:** There are 8 judging roles, as well as an option to indicate no preference. The options are as follows:
    1. Recorder.
    2. Marshal.
    3. Execution.
    4. Difficulty.
    5. Synchro.
    6. HD.
    7. Time of Flight.
    8. Chair of Judging Panel.
    9. None.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *qual_tri*
- **Attribute Name:** qual_tri.

- **Attribute Description:** Indicates the highest level of qualification a judge possesses in TRI, if any, and which type of qualification that is.

- **Possible Attribute Values:** There are 18 TRI qualifications. If a qualification is labelled as *"(TRI)"*, it means that there is a qualification of the same name in either DMT and/or TUM disciplines. If there is no TRI label, then that means there is no qualification of the same name in another discipline outside of TRI. They are listed below in the order that TrampOnline lists them.
    1. BG Club Judge (TRI).
    2. BG County Judge.
    3. BG Regional Judge (TRI).
    4. BG National Judge (TRI).
    5. SST Execution.
    6. SST Difficulty.
    7. SUTL Minion.
    8. SUTL Judge.
    9. SUTL God.
    10. Gymnastics Ireland Level One (TRI).
    11. Gymnastics Ireland Level Two (TRI).
    12. Gymnastics Ireland Level Three (TRI).
    13. Gymnastics Ireland Level Four (TRI).
    14. NEUT Level 1.
    15. NEUT Level 2.
    16. NEUT Level 3.
    17. FIG Brevet Judge (TRI).
    18. Club Level 1 Judge.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *qual_dmt*
- **Attribute Name:** qual_dmt.

- **Attribute Description:** Indicates the highest level of qualification a judge possesses in DMT, if any, and which type of qualification that is.

- **Possible Attribute Values:** There are 4 DMT qualifications. All qualifications are labelled with *"(DMT)"*, as there are qualifications of the same name in both TRI and TUM disciplines. They are listed below in the order that TrampOnline lists them.
    1. BG Club Judge (DMT).
    2. BG Regional Judge (DMT).
    3. BG National Judge (DMT).
    4. FIG Brevet Judge (DMT).

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *qual_tum*
- **Attribute Name:** qual_tum.

- **Attribute Description:** Indicates the highest level of qualification a judge possesses in TUM, if any, and which type of qualification that is.

- **Possible Attribute Values:** There are 8 TUM qualifications. All qualifications are labelled with *"(TUM)"*, as there are qualifications of the same name in TRI and sometimes also in DMT disciplines. They are listed below in the order that TrampOnline lists them.
    1. BG Club Judge (TUM).
    2. BG Regional Judge (TUM).
    3. BG National Judge (TUM).
    4. Gymnastics Ireland Level One (TUM).
    5. Gymnastics Ireland Level Two (TUM).
    6. Gymnastics Ireland Level Three (TUM).
    7. Gymnastics Ireland Level Four (TUM).
    8. FIG Brevet Judge (TUM).

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *competition*
- **Attribute Name:** competition.

- **Attribute Description:** States the name of the competition that the dataset is for.

- **Possible Attribute Values:** Any (hopefully legible) alphanumerical string with the name of the competition, and ideally the year to demarcate the specific edition of the competition running.

- **Attribute Data Type:** String (str).

---

### *judge_availability*
- **Attribute Name:** judge_availability.

- **Attribute Description:** States the availability of the judge across the length of the competition, so that they will not be put down to judge during times when they know they will not be available.

- **Possible Attribute Values:** There are seven possible values this attribute can take. These values account for one-day, two-day, and three-day competitions. These values are listed and described below.
    1. Half day
        - Used for a one-day competition to indicate that the judge will only be available for half of the day. Unclear whether it is the first or second half.
    2. Full day
        - Used for a one-day competition to indicate that the judge will be available for the full day.
    3. All weekend
        - Used for a two-day or three-day competition to indicate that the judge will be available for all two or three days in full.
    4. Saturday and Sunday
        - Used for a three-day competition to indicate that the judge will be available for the Saturday and Sunday, but not the Friday.
    5. Friday only
        - Used for a three-day competition to indicate that the judge will be available for only the Friday, but not the Saturday or Sunday.
    6. Saturday only
        - Used for a two-day or three-day competition to indicate that the judge will be available for only the Saturday, but not the Sunday in a two-day competition, and also not the Friday in a three-day competition.
    7. Sunday only
        - Used for a two-day or three-day competition to indicate that the judge will be available for only the Sunday, but not the Saturday in a two-day competition, and also not the Friday in a three-day competition.

- **Attribute Data Type:** String (str), but expressed as a categorical variable in Pandas.

---

### *judge_notes*
- **Attribute Name:** judge_notes.

- **Attribute Description:** Additional comments left by the judges or their clubs. This can be anything from random jokes for the competition organisers to laugh at, or specific requests.

- **Possible Attribute Values:** Any type of string, but usually *"N/A"* or a variant of it.

- **Attribute Data Type:** String (str).
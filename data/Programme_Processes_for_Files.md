# Processing of Files

## Data Import
The programme will first import an Excel (.xls) file from TrampOnline. In the code, this is named as: **"TrampOnline_Sample_Competitors_Not_Encoded.xls"**.
- There is a **"TrampOnline_Sample_Competitors.xls"**, which contains the correctly encoded characters, however, as this is not what TrampOnline will output, this is only used to provide an example of what the data should look like.
- There is also a file named **"TrampOnline_Sample_Judges_Not_Encoded.xls"**, with the correctly encoded alternative being **"TrampOnline_Sample_Judges.xls"**.

## Mojibake Fixes
The programme will convert the .xls file into a .csv file with a similar name: **"01_TrampOnline_Sample_Competitors.csv"**, after fixing the garbled characters. The same is done with the judging dataset, which is named **"02_TrampOnline_Sample_Judges.csv"**.
- To fix the garbled characters and return them to normal, a map of corrupted characters has been made, along with a function that goes through them and fixes any incorrectly encoded characters.
- This file is then read into the programme as a Pandas data frame.

## Data Type Adjustments
The **"01_TrampOnline_Sample_Competitors.csv"** file will be sanity checked, and its data will be type converted into more appropriate data types for working with the data. A .csv file of this is created and outputted as: **"03_Updated_Sample_TrampOnline_Data.csv"**.

## Organisation
The newly created **"03_Updated_Sample_TrampOnline_Data.csv"** will be assigned as the new data frame. It will then be sorted by discipline, levels within the discipline, competitor name, and finalyl competitor club, before being outputted as **"04_Organised_Sample_TrampOnline_Data.csv"**.
- LORE: I couldn't figure out for a while why this file wasn't encoding data properly, until I realised I had another output in the code that overwrote this file and didn't have an encoding designation. It made me think of coconuts.
    - See *"coconut.jpg"* in the Team Fortress 2 files.

## Competitor List
The **"04_Organised_Sample_TrampOnline_Data.csv"** will be used to create the first organised .xlsx file titled **"05_Grouped_Competitors_by_Discipline.xlsx"**. It's an Excel file that will contain between 1 - 4 sheets, depending on the categories that competitors have signed up for, and have them spread out across a number of flights that was deemed appropriate for the number in the category.

## Flights
The same **"04_Organised_Sample_TrampOnline_Data.csv"** will then be used to apply the correct flight numbers to the competitors, and to remove any duplicates that may occur (this code can create such duplicates). The updated .csv file will be almost identical, with the exception of the *"flights"* column containing the correct flight numbers for the competitors. This will be saved as **"06_Organised_Sample_TrampOnline_Data_with_Flights.csv"**.
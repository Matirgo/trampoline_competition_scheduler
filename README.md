# trampoline_competition_scheduler
Repository for a trampoline gymnastics competition scheduler suitable for automatically organising universit-level competitions.

## Current Version
### Capabilities
The current version of the programme is capable of doing the following operations.
- Import data from a TrampOnline-based .xls Excel file.
- Correctly encode any corrupted characters, such as names with special characters like accents, or the ampersand (&) symbol.
- Organise competitors by discipline (TRA, DMT, TUM, and TRS), level within the discipline, name, and club.
- Perform flight calculations based on the number of competitors in each level and category.
  - There is no functionality to merge multiple categories together just yet.
- Export this organised list into a stylised .xlsx Excel format.
  - There are some minor aesthetic issues with border lines for flights, but the logic is sound.

### Next Major Steps
The data is not being merged with judging data yet, but the competitor data itself is ready to be scheduled.
- The programme currently does not take into account judges and what they are able or not able to judge.
  - The dataset must be updated to include judging information.
- There is no scheduling logic put in place yet.

## Future
Future versions should include scheduling algorithms, error handling, and customisable inputs such as length per competitor/flight, number of available panels, etc, time constraints or blocked off sections of time, etc.

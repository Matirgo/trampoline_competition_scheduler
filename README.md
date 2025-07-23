# trampoline_competition_scheduler
Repository for a trampoline gymnastics competition scheduler suitable for automatically organising universit-level competitions.

## Current Version
### Capabilities
The current version of the programme is capable of doing the following operations.
- Import data from a .csv file.
- Organise competitors by trampoline level and category.
- Export this organised list in both .csv format, and also in a premitively stylised xlsx (Excel) format.

### Next Major Steps
The current version only works with trampoline competitors, and is not based on TrampOnline formatting. The below steps outline the most important updates to follow.
- Update the data import and processing steps to be in line with the way TrampOnline presents its data.
  - The category column must be merged with the trampoline level column.
  - The first name and surname columns must be merged into one name column.
  - New columns for clubs and teams should be added.
- The programme currently does not take into account judges and what they are able or not able to judge.
  - The dataset must be updated to include judging information.

## Future
Future versions should include scheduling algorithms, error handling, and customisable inputs such as length per competitor/flight, number of available panels, etc, time constraints or blocked off sections of time, etc.

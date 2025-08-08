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
  - I.e. There are only eight competitors in the Novice level across both categoires, so Novice Men and Novice Women are combined.
- Export this organised list into a stylised .xlsx Excel format.
  - There are some minor aesthetic issues with border lines for flights, but the logic is sound.

### Next Major Steps
- **WIP - Matas:** Provide a full breakdown of what the programme can do, as well as future features to be implemented.
- **WIP - Matas:** The programme currently does not take into account judges and what they are able or not able to judge.
  - The dataset must be updated to include judging information.
- **Not started - Matas:** There is no scheduling logic put in place yet.
- **Not started - Anyone:** Include a required medal counter!

#### Frontend and Backend
The application may work well with a frontend or a backend. Users may appreciate such a display as opposed to one that is run from the command line, or from an IDE. With this in mind, there are a variety of other tasks that may be done.
- **Not started - Anyone:** Front end design.
  - A sample designed may be mocked up for the website, be that coded up or done through Figma or another similar tool.
- **Not started - Anyone:** Back end functionality.
  - The current software is able to perform flight scheduling. Code can be added so that any valid .xls file can be uploaded and output should be returned to the user.

## Future
Future versions should include scheduling algorithms, error handling, and customisable inputs such as length per competitor/flight, number of available panels, etc, time constraints or blocked off sections of time, etc. Take into account medal requirements too.

## Known Issues
- Flight formatting
  - The line boxes surrounding each flight tend to not fully encapsulate most groups.
- Low entries formatting glitch.
  - If there are no more than two competitors in any category for a given discipline, the flight formatting code does not work. Once three competitors are present in the same category in that discipline, this problem appears to disappear.
- The programme does not take into account how to handle special characters, such as fadas and apostrophes. Code to account for this must be added.

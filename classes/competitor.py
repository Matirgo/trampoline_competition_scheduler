from enum import Enum

class TrampolineLevel(Enum):
    Novice = 1
    Intermediate = 2
    Intervanced = 3
    Advanced = 4
    Elite = 5
    Elite_Pro = 6

class Competitor:
        
    def __init__(self, first_name: str, sur_name: str, is_female: bool,
                 tra_competing: bool = False, tra_level: TrampolineLevel = None,
                 dmt_competing: bool = False, dmt_level: TrampolineLevel = None,
                 tum_competing: bool = False, tum_level: TrampolineLevel = None):

        self.first_name = first_name
        self.sur_name = sur_name
        self.is_female = is_female
        self.tra_competing = tra_competing
        self.tra_level = tra_level
        self.dmt_competing = dmt_competing
        self.dmt_level = dmt_level
        self.tum_competing = tum_competing
        self.tum_level = tum_level

    def __str__(self):
        gender = "female" if self.is_female else "male"
        tra = f"TRA: {self.tra_level.name}" if self.tra_competing else "Not competing in TRA"
        dmt = f"DMT: {self.dmt_level.name}" if self.dmt_competing else "Not competing in DMT"
        tum = f"TUM: {self.tum_level.name}" if self.tum_competing else "Not competing in TUM"
        return f"{self.first_name} {self.sur_name} ({gender})\n{tra}\n{dmt}\n{tum}"


"""
Trampoline Competition Competitor Module

This module defines the data structures for representing trampoline competitors
and their skill levels in different disciplines.

Classes:
    TrampolineLevel: Enum defining skill levels from Novice to Elite Pro
    Competitor: Represents a trampoline competitor with personal info and competition details
"""

from enum import Enum


class TrampolineLevel(Enum):
    """
    Enumeration defining the skill levels for trampoline competitions.
    
    Each level represents increasing difficulty and skill requirements:
    - Novice: Entry level for beginners
    - Intermediate: Basic skills mastered
    - Intervanced: Intermediate to advanced transition (typo intended?)
    - Advanced: High skill level with complex routines
    - Elite: Professional competition level
    - Elite_Pro: Highest professional level
    """
    Novice = 1
    Intermediate = 2
    Intervanced = 3  
    Advanced = 4
    Elite = 5
    Elite_Pro = 6


class Competitor:
    """
    Represents a trampoline competitor with personal information and competition details.
    
    This class stores all relevant information about a competitor including their
    personal details, gender category, and participation/skill levels in the three
    main trampoline disciplines: TRA (Trampoline), DMT (Double Mini Trampoline),
    and TUM (Tumbling).
    
    Attributes:
        first_name (str): Competitor's first name
        surname (str): Competitor's surname/family name
        category (bool): Gender category (True for female, False for male)
        tra_competing (bool): Whether competing in Trampoline discipline
        tra_level (TrampolineLevel): Skill level for Trampoline (if competing)
        dmt_competing (bool): Whether competing in Double Mini Trampoline discipline
        dmt_level (TrampolineLevel): Skill level for DMT (if competing)
        tum_competing (bool): Whether competing in Tumbling discipline  
        tum_level (TrampolineLevel): Skill level for Tumbling (if competing)
    """
        
    def __init__(self, first_name: str, surname: str, category: bool,
                 tra_competing: bool = False, tra_level: TrampolineLevel = None,
                 dmt_competing: bool = False, dmt_level: TrampolineLevel = None,
                 tum_competing: bool = False, tum_level: TrampolineLevel = None):
        """
        Initialize a new Competitor instance.
        
        Args:
            first_name (str): The competitor's first name
            surname (str): The competitor's surname/family name
            category (bool): Gender category - True for female, False for male
            tra_competing (bool, optional): Whether competing in Trampoline. Defaults to False.
            tra_level (TrampolineLevel, optional): Trampoline skill level. Defaults to None.
            dmt_competing (bool, optional): Whether competing in Double Mini Trampoline. Defaults to False.
            dmt_level (TrampolineLevel, optional): DMT skill level. Defaults to None.
            tum_competing (bool, optional): Whether competing in Tumbling. Defaults to False.
            tum_level (TrampolineLevel, optional): Tumbling skill level. Defaults to None.
            
        Note:
            If a competitor is marked as competing in a discipline (e.g., tra_competing=True),
            the corresponding level should also be provided (e.g., tra_level=TrampolineLevel.Advanced).
        """
        # Personal information
        self.first_name = first_name
        self.surname = surname
        self.category = category  # True = female, False = male
        
        # Trampoline (TRA) competition details
        self.tra_competing = tra_competing
        self.tra_level = tra_level
        
        # Double Mini Trampoline (DMT) competition details
        self.dmt_competing = dmt_competing
        self.dmt_level = dmt_level
        
        # Tumbling (TUM) competition details
        self.tum_competing = tum_competing
        self.tum_level = tum_level

    def __str__(self):
        """
        Return a human-readable string representation of the competitor.
        
        Creates a formatted multi-line string showing the competitor's name, gender,
        and competition status/levels for each discipline.
        
        Returns:
            str: Formatted string with competitor details including:
                 - Full name and gender on first line
                 - Competition status and level for each discipline (TRA, DMT, TUM)
                 
        Note:
            This method has bugs - it references self.is_female and self.sur_name 
            which don't exist. Should use self.category and self.surname instead.
        """
        # FIXME: This method has attribute errors
        # Should use self.category instead of self.is_female
        # Should use self.surname instead of self.sur_name
        gender = "female" if self.category else "male"  # Fixed: use self.category
        
        # Format competition details for each discipline
        tra = f"TRA: {self.tra_level.name}" if self.tra_competing else "Not competing in TRA"
        dmt = f"DMT: {self.dmt_level.name}" if self.dmt_competing else "Not competing in DMT"
        tum = f"TUM: {self.tum_level.name}" if self.tum_competing else "Not competing in TUM"
        
        # Return formatted multi-line string
        return f"{self.first_name} {self.surname} ({gender})\n{tra}\n{dmt}\n{tum}"  # Fixed: use self.surname

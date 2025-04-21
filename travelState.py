# travel_state.py
from typing import Optional, Dict, List, Any, Union
from pydantic import BaseModel
from models.TravelPreference import TravelPreferences

class TravelState(BaseModel):
    user_input: Optional[Dict[str, Any]] = None
    preferences: Optional[Dict[str, str]] = None
    filtered_destinations: Optional[List[Union[Dict[str, str], str]]] = None
    recommendation: Optional[str] = None
    error: Optional[str] = None
    extra_info: Optional[List[str]] = None
    all_things: Optional[TravelPreferences] = None
    final_answer: Optional[str] = None
    
    def __hash__(self):
        # Choose the attributes that uniquely identify the TravelState object
        # Example: We can combine the hash of user_input and preferences if they are important
        return hash((
            tuple(self.user_input.items()) if self.user_input else None,
            tuple(self.preferences.items()) if self.preferences else None,
            tuple(self.filtered_destinations) if self.filtered_destinations else None,
            self.recommendation,
            self.error,
            tuple(self.extra_info) if self.extra_info else None,
            self.all_things,  # If TravelPreferences is a Pydantic model, it will be hashable by default
            self.final_answer
        ))

    def __eq__(self, other):
        if isinstance(other, TravelState):
            return (
                self.user_input == other.user_input and
                self.preferences == other.preferences and
                self.filtered_destinations == other.filtered_destinations and
                self.recommendation == other.recommendation and
                self.error == other.error and
                self.extra_info == other.extra_info and
                self.all_things == other.all_things and
                self.final_answer == other.final_answer
            )
        return False
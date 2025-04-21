from pydantic import BaseModel
from typing import Optional
from datetime import date

class TravelPreferences(BaseModel):
    theme: Optional[str] = None
    total_budget: Optional[float] = None
    per_day_budget: Optional[float] = None
    budget_type: Optional[str] = None
    preferred_location: Optional[str] = None
    international_travel: Optional[bool] = None
    max_travel_distance: Optional[str] = None
    environment_type: Optional[str] = None
    avoid_regions: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    flexibility: Optional[bool] = None
    traveler_type: Optional[str] = None
    accommodation: Optional[str] = None
    activity: Optional[str] = None
    weather: Optional[str] = None

    def __hash__(self):
        return hash(tuple(self.__dict__.values()))

    def __eq__(self, other):
        return isinstance(other, TravelPreferences) and self.__dict__ == other.__dict__
from travelState import TravelState
from langchain_core.prompts import ChatPromptTemplate

def destiExtractorList(input_dict: dict) -> list[str]:
    destinations_info = []
    for i in input_dict.get("results", []):
        destinations_info.append(i["content"])
    return destinations_info

def generate_travel_prompt_from_state(state: TravelState) -> ChatPromptTemplate:
    prefs = state.all_things
    if not prefs:
        return "Error: No travel preferences provided."

    start_date_str = prefs.start_date.strftime("%B %d, %Y") if prefs.start_date else "N/A"
    end_date_str = prefs.end_date.strftime("%B %d, %Y") if prefs.end_date else "N/A"

    prompt = f"""
I want you to act as a personalized travel itinerary planner.

Here are my preferences:
- Theme: {prefs.theme or "N/A"}
- Total Budget: ${prefs.total_budget if prefs.total_budget is not None else "N/A"}
- Per Day Budget: ${prefs.per_day_budget if prefs.per_day_budget is not None else "N/A"}
- Budget Type: {prefs.budget_type or "N/A"}
- Preferred Location: {prefs.preferred_location or "N/A"}
- Open to International Travel: {"Yes" if prefs.international_travel else "No"}
- Maximum Distance Willing to Travel: {prefs.max_travel_distance or "N/A"}
- Preferred Environment Type: {prefs.environment_type or "N/A"}
- Avoid These Regions: {prefs.avoid_regions or "None"}
- Travel Dates: From {start_date_str} to {end_date_str}
- Flexible Dates: {"Yes" if prefs.flexibility else "No"}
- Traveler Type: {prefs.traveler_type or "N/A"}
- Accommodation Preference: {prefs.accommodation or "N/A"}
- Primary Activity of Interest: {prefs.activity or "N/A"}
- Preferred Weather: {prefs.weather or "N/A"}

Please generate a detailed day-by-day travel itinerary based on these inputs, including destination suggestions, travel time, daily activity plans, and estimated expenses.
"""

    return prompt.strip()
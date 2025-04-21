# # # from tavily import TavilyClient
# # # from typing import Dict
# # # from decouple import config
# # # from travelState import TravelState
# # # tavily = TavilyClient(api_key=config("TAVILY_API_KEY"))

# # # newState = TravelState(
# # #     user_input={"mood": "relaxing", "continent": "Europe", "budget": "$1000"},
# # #     preferences={"mood": "relaxing", "continent": "Europe", "budget": "$1000"},
# # #     filtered_destinations=None,
# # #     recommendation="Paris is a great choice for a relaxing trip in Europe with a budget of $1000.",
# # #     error=None,
# # #     extra_info=None
# # # )

# # # def fetch_destinations_from_tavily(state: TravelState) -> TravelState:
# # #     prefs = state.preferences
# # #     query = f"List 5 {prefs['mood']} travel destinations in {prefs['continent']} under a {prefs['budget']} budget"
    
# # #     results = tavily.search(query=query)
# # #     with open("results.txt", "w", encoding="utf-8") as f:
# # #         f.write(str(results))  # Write the results to a file for debugging purposes. You can remove this line later.
# # #     destinations = []
# # #     for r in results.get("results", []):
# # #         destinations.append({"name": r.get("title"), "link": r.get("url")})
    
# # #     state.filtered_destinations = destinations
# # #     return state

# # # # print("Fetching destinations...")
# # # # print(newState)
# # # # print(".........................................................")

# # # # print(fetch_destinations_from_tavily(newState).model_dump_json(indent=2))


# # # # print(".........................................................")

# # import json
# # with open("results.json", "r", encoding="utf-8") as f:
# #     results = json.load(f)

# # def destiExtractorList(input_dict: dict) -> list[str]:
# #     destinations_info = []
# #     for i in results.get("results", []):
# #         destinations_info.append(i["content"])
# #     return destinations_info

# # destinations = destiExtractorList(results)

# # print(destinations)

# from datetime import datetime

# def generate_travel_prompt(
#     theme,
#     total_budget,
#     per_day_budget,
#     budget_type,
#     preferred_location,
#     international_travel,
#     max_travel_distance,
#     environment_type,
#     avoid_regions,
#     start_date,
#     end_date,
#     flexibility,
#     traveler_type,
#     accommodation,
#     activity,
#     weather
# ):
#     start_date_str = datetime.strptime(start_date, "%Y-%m-%d").strftime("%B %d, %Y")
#     end_date_str = datetime.strptime(end_date, "%Y-%m-%d").strftime("%B %d, %Y")

#     prompt = f"""
# I want you to act as a personalized travel itinerary planner.

# Here are my preferences:
# - Theme: {theme}
# - Total Budget: ${total_budget}
# - Per Day Budget: ${per_day_budget}
# - Budget Type: {budget_type}
# - Preferred Location: {preferred_location}
# - Open to International Travel: {"Yes" if international_travel else "No"}
# - Maximum Distance Willing to Travel: {max_travel_distance}
# - Preferred Environment Type: {environment_type}
# - Avoid These Regions: {avoid_regions if avoid_regions else "None"}
# - Travel Dates: From {start_date_str} to {end_date_str}
# - Flexible Dates: {"Yes" if flexibility else "No"}
# - Traveler Type: {traveler_type}
# - Accommodation Preference: {accommodation}
# - Primary Activity of Interest: {activity}
# - Preferred Weather: {weather}

# Please generate a detailed day-by-day travel itinerary based on these inputs, including destination suggestions, travel time, daily activity plans, and estimated expenses.
# """

#     return prompt.strip()

# prompt = generate_travel_prompt(
#     theme="Romantic",
#     total_budget=3000,
#     per_day_budget=250,
#     budget_type="Mid-range",
#     preferred_location="Italy",
#     international_travel=True,
#     max_travel_distance="Within Europe",
#     environment_type="City",
#     avoid_regions="None",
#     start_date="2025-06-10",
#     end_date="2025-06-20",
#     flexibility=False,
#     traveler_type="Couple",
#     accommodation="Boutique stay",
#     activity="Wine tasting / food tours",
#     weather="Warm/Sunny"
# )

# print(prompt)

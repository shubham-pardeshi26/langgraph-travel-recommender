from Settings import env_creds
from travelState import TravelState
from ExtraTools import destiExtractorList

def fetch_destinations_from_tavily(state: TravelState) -> TravelState:
    prefs = state.all_things
    
    query = f"List 5 {prefs.theme} travel destinations in {prefs.preferred_location} under a {prefs.total_budget} budget"
    results = env_creds.travily_client.search(query=query)
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write(str(results))  # Write the results to a file for debugging purposes. You can remove this line later.
    destinations = destiExtractorList(results)
    state.extra_info = destinations
    
    return state

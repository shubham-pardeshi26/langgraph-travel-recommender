from travelState import TravelState
from prompts.ExtractNamePrompt import EXTRACT_PLACES_PROMPT 
from Settings import env_creds 

def extract_names_from_tavily(state: TravelState) -> TravelState:
    content = state.extra_info
    chain = EXTRACT_PLACES_PROMPT | env_creds.llm | env_creds.parser

    try:
        places = chain.invoke({"content": content})
        # Convert to expected internal format
        state.filtered_destinations = [p for p in places]
    except Exception as e:
        state.error = f"Place extraction failed: {str(e)}"
    
    return state


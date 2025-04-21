from travelState import TravelState
from Settings import env_creds 
from ExtraTools import generate_travel_prompt_from_state
from dummyStates import dummy_state_final
import markdown  # Import the markdown library for conversion

def RecommenderFinal(state: TravelState) -> TravelState:
    FINAL_PROMPT_ITERNARY = generate_travel_prompt_from_state(state=state)
    try:
        fin_ans = env_creds.llm.invoke(FINAL_PROMPT_ITERNARY)  
        # Convert to expected internal format
        state.final_answer = fin_ans.content
    except Exception as e:
        state.error = f"Place extraction failed: {str(e)}"
    
    return state

# fin_state = RecommenderFinal(dummy_state_final)
# # print(fin_state.final_answer)
# print(fin_state.error)

# Convert markdown to HTML using markdown library
# html_content = markdown.markdown(fin_state.final_answer)

# with open("output.html", "w") as file:  # Save HTML content to a file for verification
#     file.write(fin_state.final_answer)
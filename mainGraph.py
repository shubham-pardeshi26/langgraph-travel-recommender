from langgraph.graph import StateGraph, END
from travelState import TravelState
from DestiFromTavilyAgent import fetch_destinations_from_tavily
from NameAcquireAgent import extract_names_from_tavily
from RecommederAgent import RecommenderFinal

ResearchState = TravelState()

graph_builder = StateGraph(ResearchState)

graph_builder.add_node("tavily_content", fetch_destinations_from_tavily)
graph_builder.add_node("extract_names_from_tavily", extract_names_from_tavily)
graph_builder.add_node("final_showdown_node_for_iternary",RecommenderFinal)


graph_builder.set_entry_point("tavily_content")  # if your UI is not ready
graph_builder.add_edge("tavily_content", "extract_names_from_tavily")
graph_builder.add_edge("extract_names_from_tavily", "final_showdown_node_for_iternary")

# graph_builder.add_edge("final_showdown_node_for_iternary", END)

# Build the graph
travel_buddy = graph_builder.compile()

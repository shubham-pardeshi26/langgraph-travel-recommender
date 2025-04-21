import streamlit as st
from datetime import date
from models.TravelPreference import TravelPreferences
from travelState import TravelState

# Function to collect travel preferences from user input in Streamlit form
def get_travel_preferences():
    st.title("Travel Preferences Form")

    # Collecting travel preferences using Streamlit widgets
    theme = st.selectbox("Theme of the Trip", ["Romantic", "Adventure", "Cultural"])
    total_budget = st.number_input("Total Budget (USD)", min_value=0.0)
    per_day_budget = st.number_input("Per Day Budget (USD)", min_value=0.0)
    budget_type = st.selectbox("Budget Type", ["Luxury", "Mid-range", "Budget"])
    preferred_location = st.text_input("Preferred Location (Country/Region)")
    international_travel = st.checkbox("Allow International Travel")
    max_travel_distance = st.text_input("Max Travel Distance (e.g., 'Within Europe')")
    environment_type = st.selectbox("Preferred Environment", ["City", "Nature", "Beach"])
    avoid_regions = st.text_input("Regions to Avoid")
    start_date = st.date_input("Start Date", min_value=date.today())
    end_date = st.date_input("End Date", min_value=date.today())
    flexibility = st.checkbox("Flexible Dates?")
    traveler_type = st.selectbox("Traveler Type", ["Solo", "Couple", "Family"])
    accommodation = st.selectbox("Accommodation Type", ["Hotel", "Hostel", "Airbnb", "Resort"])
    activity = st.text_input("Preferred Activities")
    weather = st.selectbox("Preferred Weather", ["Sunny", "Rainy", "Mild", "Cold"])

    # Create TravelPreferences model instance based on user input
    preferences = TravelPreferences(
        theme=theme,
        total_budget=total_budget,
        per_day_budget=per_day_budget,
        budget_type=budget_type,
        preferred_location=preferred_location,
        international_travel=international_travel,
        max_travel_distance=max_travel_distance,
        environment_type=environment_type,
        avoid_regions=avoid_regions,
        start_date=start_date,
        end_date=end_date,
        flexibility=flexibility,
        traveler_type=traveler_type,
        accommodation=accommodation,
        activity=activity,
        weather=weather,
    )

    # Create TravelState instance with the travel preferences
    travel_state = TravelState(all_things=preferences)

    # Display the travel state for user review
    st.subheader("Your Travel Preferences")
    st.write(travel_state)

    return travel_state

# Run the function to collect travel preferences and display them
if __name__ == "__main__":
    travel_state = get_travel_preferences()

from travelState import TravelState, TravelPreferences
from datetime import date
dummy_state_1 = TravelState(
    user_input={"mood": "relaxing", "continent": "Europe", "budget": "$1000"},
    preferences={"mood": "relaxing", "continent": "Europe", "budget": "$1000"},
    filtered_destinations=None,
    recommendation="Paris is a great choice for a relaxing trip in Europe with a budget of $1000.",
    error=None,
    extra_info=None
)

dummy_state_2 = TravelState(
    user_input={"mood": "relaxing", "continent": "Europe", "budget": "$1000"},
    preferences={"mood": "relaxing", "continent": "Europe", "budget": "$1000"},
    filtered_destinations=None,
    recommendation="Paris is a great choice for a relaxing trip in Europe with a budget of $1000.",
    error=None,
    extra_info=['Consider underrated European cities like Varna and Ljubljana for a cheap summer vacation in Europe for under $1,000. Vilnius, Lithuania, is a budget-friendly gem with UNESCO sites, cozy cafés, and cheap public transportation. Explore the charming city of Sibiu, Romania, with its scenic medieval architecture and affordable accommodations and activities.', "Whether it's historic Prague, scenic Dubrovnik, or charming Budapest, budget travelers can explore Europe affordably without compromising on experiences. Wander cobblestone streets, savor local cuisine, laze on sunny beaches, and soak in vibrant cultures without straining your wallet in these cheap European destinations under $1000 for a vacation!", "Europe offers affordable vacation spots that won't break the bank, allowing travelers to explore historical gems and cultural delights. Stay at recommended accommodations with comprehensive amenities based on research for a comfortable and budget-friendly European vacation. Explore hidden gems like Leipzig, Lake Ohrid, Bansko, and more for a wallet-friendly journey through Europe's varied", "Are you craving an unforgettable travel experience without draining your savings? Look no further than these incredible budget-friendly, under $1000, tours to Europe that we've meticulously analyzed to find the absolute best. From price-conscious itineraries and rave guest ratings to top-notch service, captivating destinations, and exciting activities, these handpicked budget organized tours", "U.S. News considered average hotel prices, flight deals, available vacation packages, affordable attractions and overall accessibility – plus user votes – to rank the best cheap European vacations. Use the Bratislava Card to gain entrance to more than 20 museums and attractions (including the famous Bratislava Castle), plus you'll enjoy extra perks like store and restaurant discounts and a city walking tour. You can visit many of the Czechia city's most popular attractions without charge, including Old Town Square, the Charles Bridge and Petřín Hill; explore them all on a complimentary walking tour. A three-day Vilnius Pass costs about $60 and includes entrance to more than 20 museums and attractions (like Gediminas Castle Tower), a two-hour city bike rental, a bus tour, discounts at select restaurants and more."]
)


dummy_state_final = TravelState(
    user_input={"mood": "relaxing", "continent": "Europe", "budget": "$1000"},
    preferences={"mood": "relaxing", "continent": "Europe", "budget": "$1000"},
    filtered_destinations=None,
    recommendation="Paris is a great choice for a relaxing trip in Europe with a budget of $1000.",
    error=None,
    extra_info=['Consider underrated European cities like Varna and Ljubljana for a cheap summer vacation in Europe for under $1,000. Vilnius, Lithuania, is a budget-friendly gem with UNESCO sites, cozy cafés, and cheap public transportation. Explore the charming city of Sibiu, Romania, with its scenic medieval architecture and affordable accommodations and activities.', "Whether it's historic Prague, scenic Dubrovnik, or charming Budapest, budget travelers can explore Europe affordably without compromising on experiences. Wander cobblestone streets, savor local cuisine, laze on sunny beaches, and soak in vibrant cultures without straining your wallet in these cheap European destinations under $1000 for a vacation!", "Europe offers affordable vacation spots that won't break the bank, allowing travelers to explore historical gems and cultural delights. Stay at recommended accommodations with comprehensive amenities based on research for a comfortable and budget-friendly European vacation. Explore hidden gems like Leipzig, Lake Ohrid, Bansko, and more for a wallet-friendly journey through Europe's varied", "Are you craving an unforgettable travel experience without draining your savings? Look no further than these incredible budget-friendly, under $1000, tours to Europe that we've meticulously analyzed to find the absolute best. From price-conscious itineraries and rave guest ratings to top-notch service, captivating destinations, and exciting activities, these handpicked budget organized tours", "U.S. News considered average hotel prices, flight deals, available vacation packages, affordable attractions and overall accessibility – plus user votes – to rank the best cheap European vacations. Use the Bratislava Card to gain entrance to more than 20 museums and attractions (including the famous Bratislava Castle), plus you'll enjoy extra perks like store and restaurant discounts and a city walking tour. You can visit many of the Czechia city's most popular attractions without charge, including Old Town Square, the Charles Bridge and Petřín Hill; explore them all on a complimentary walking tour. A three-day Vilnius Pass costs about $60 and includes entrance to more than 20 museums and attractions (like Gediminas Castle Tower), a two-hour city bike rental, a bus tour, discounts at select restaurants and more."],
    all_things = TravelPreferences(
                        theme="Romantic",
                        total_budget=3000,
                        per_day_budget=250,
                        budget_type="Mid-range",
                        preferred_location="Italy",
                        international_travel=True,
                        max_travel_distance="Within Europe",
                        environment_type="City",
                        avoid_regions=None,
                        start_date=date(2025, 6, 10),
                        end_date=date(2025, 6, 20),
                        flexibility=False,
                        traveler_type="Couple",
                        accommodation="Boutique stay",
                        activity="Wine tasting / food tours",
                        weather="Warm/Sunny"
                    ),
    final_answer=None
)

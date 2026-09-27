# AI Travel Agent
# Beginner-friendly Python project

DESTINATIONS = {
    "budget": [
        {
            "name": "Goa",
            "type": "Beach",
            "budget": 8000,
            "description": "Beautiful beaches, nightlife and relaxing coastal experiences."
        },
        {
            "name": "Mysore",
            "type": "Heritage",
            "budget": 6000,
            "description": "A cultural destination famous for palaces, temples and local food."
        },
        {
            "name": "Pondicherry",
            "type": "Beach",
            "budget": 9000,
            "description": "A peaceful coastal destination with French architecture and cafes."
        }
    ],

    "moderate": [
        {
            "name": "Manali",
            "type": "Mountain",
            "budget": 15000,
            "description": "A popular mountain destination with scenic views and adventure activities."
        },
        {
            "name": "Jaipur",
            "type": "Heritage",
            "budget": 12000,
            "description": "Known for forts, palaces, markets and rich Rajasthani culture."
        },
        {
            "name": "Kerala",
            "type": "Nature",
            "budget": 14000,
            "description": "Famous for backwaters, greenery, beaches and peaceful landscapes."
        }
    ],

    "luxury": [
        {
            "name": "Kashmir",
            "type": "Mountain",
            "budget": 30000,
            "description": "A beautiful destination known for mountains, lakes and scenic valleys."
        },
        {
            "name": "Andaman",
            "type": "Beach",
            "budget": 35000,
            "description": "A tropical destination with beaches, islands and water activities."
        }
    ]
}


def suggest_destinations(budget):
    """Suggest destinations based on the user's budget."""

    suggestions = []

    for category in DESTINATIONS.values():
        for destination in category:
            if destination["budget"] <= budget:
                suggestions.append(destination)

    return suggestions


def generate_itinerary(destination, days):
    """Generate a simple day-by-day travel itinerary."""

    activities = {
        "Goa": [
            "Visit Baga Beach",
            "Explore Fort Aguada",
            "Enjoy a sunset at a beach",
            "Visit Panjim",
            "Explore local markets"
        ],

        "Mysore": [
            "Visit Mysore Palace",
            "Visit Chamundi Hill",
            "Explore Devaraja Market",
            "Visit St. Philomena's Church",
            "Enjoy local Mysore food"
        ],

        "Pondicherry": [
            "Visit Promenade Beach",
            "Explore White Town",
            "Visit Sri Aurobindo Ashram",
            "Explore local cafes",
            "Visit Paradise Beach"
        ],

        "Manali": [
            "Explore Mall Road",
            "Visit Hadimba Temple",
            "Visit Solang Valley",
            "Explore Old Manali",
            "Enjoy mountain activities"
        ],

        "Jaipur": [
            "Visit Amber Fort",
            "Explore City Palace",
            "Visit Hawa Mahal",
            "Explore local markets",
            "Visit Jantar Mantar"
        ],

        "Kerala": [
            "Explore Kochi",
            "Visit Munnar",
            "Enjoy a backwater experience",
            "Explore local villages",
            "Relax at a scenic location"
        ],

        "Kashmir": [
            "Explore Srinagar",
            "Enjoy Dal Lake",
            "Visit Mughal Gardens",
            "Explore Gulmarg",
            "Enjoy mountain scenery"
        ],

        "Andaman": [
            "Explore Port Blair",
            "Visit Radhanagar Beach",
            "Enjoy water activities",
            "Explore local islands",
            "Relax at the beach"
        ]
    }

    if destination not in activities:
        return ["Explore the destination and enjoy local attractions."]

    plan = []

    for i in range(days):
        activity = activities[destination][i % len(activities[destination])]
        plan.append(f"Day {i + 1}: {activity}")

    return plan


def calculate_budget(total_budget, days):
    """Divide the travel budget into major categories."""

    accommodation = total_budget * 0.35
    food = total_budget * 0.20
    transport = total_budget * 0.20
    activities = total_budget * 0.15
    emergency = total_budget * 0.10

    return {
        "Accommodation": accommodation,
        "Food": food,
        "Transport": transport,
        "Activities": activities,
        "Emergency": emergency
    }


def travel_tips(destination):
    """Return useful travel tips."""

    tips = [
        "Carry a valid ID while travelling.",
        "Keep some emergency money separately.",
        "Check the weather before travelling.",
        "Keep important documents safely.",
        "Respect local culture and traditions.",
        "Avoid carrying unnecessary valuables."
    ]

    if destination == "Goa":
        tips.append("Carry sunscreen and comfortable beachwear.")

    elif destination == "Manali":
        tips.append("Carry warm clothes, especially during winter.")

    elif destination == "Kashmir":
        tips.append("Carry warm clothing and comfortable shoes.")

    elif destination == "Kerala":
        tips.append("Carry an umbrella and light comfortable clothing.")

    return tips
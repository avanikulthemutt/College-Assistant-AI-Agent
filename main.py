from travel_agent import (
    suggest_destinations,
    generate_itinerary,
    calculate_budget,
    travel_tips
)


def display_destinations(destinations):
    """Display recommended destinations."""

    if not destinations:
        print("\nSorry! No destinations found within your budget.")
        return

    print("\n========== RECOMMENDED DESTINATIONS ==========")

    for i, destination in enumerate(destinations, start=1):
        print(f"\n{i}. {destination['name']}")
        print(f"   Type: {destination['type']}")
        print(f"   Estimated Budget: ₹{destination['budget']}")
        print(f"   About: {destination['description']}")


def main():

    print("\n======================================")
    print("       AI TRAVEL AGENT")
    print("======================================")

    name = input("\nEnter your name: ")

    print(f"\nHello {name}! 👋")
    print("I am your simple AI Travel Agent.")

    while True:

        print("\n========== TRAVEL MENU ==========")
        print("1. Get destination suggestions")
        print("2. Generate itinerary")
        print("3. Plan your budget")
        print("4. Get travel tips")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        # Destination suggestions
        if choice == "1":

            try:
                budget = float(input("Enter your travel budget (₹): "))

                destinations = suggest_destinations(budget)

                display_destinations(destinations)

            except ValueError:
                print("Please enter a valid number.")

        # Itinerary
        elif choice == "2":

            destination = input("Enter your destination: ")
            
            try:
                days = int(input("How many days will you travel? "))

                if days <= 0:
                    print("Number of days must be greater than 0.")
                    continue

                itinerary = generate_itinerary(destination, days)

                print("\n========== YOUR ITINERARY ==========")

                for day in itinerary:
                    print(day)

            except ValueError:
                print("Please enter a valid number of days.")

        # Budget planning
        elif choice == "3":

            try:
                total_budget = float(
                    input("Enter your total travel budget (₹): ")
                )

                days = int(
                    input("Enter number of travel days: ")
                )

                budget_plan = calculate_budget(total_budget, days)

                print("\n========== BUDGET PLAN ==========")

                for category, amount in budget_plan.items():
                    print(f"{category}: ₹{amount:.2f}")

                daily_budget = total_budget / days

                print(f"\nApproximate daily budget: ₹{daily_budget:.2f}")

            except ValueError:
                print("Please enter valid numbers.")

        # Travel tips
        elif choice == "4":

            destination = input("Enter your destination: ")

            tips = travel_tips(destination)

            print("\n========== TRAVEL TIPS ==========")

            for i, tip in enumerate(tips, start=1):
                print(f"{i}. {tip}")

        # Exit
        elif choice == "5":

            print("\nThank you for using the AI Travel Agent! ✈️")
            print("Have a safe and enjoyable journey!")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
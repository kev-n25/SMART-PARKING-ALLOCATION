# nash_parking.py

ALPHA = 0.6
BETA = 0.4

def find_equilibrium(spots):
    """
    spots = [
        { "cost": 20, "crowding": 0.3 },
        ...
    ]
    """

    for s in spots:
        cost = s.get("cost", 0)
        crowding = s.get("crowding", 1)

        s["utility"] = ALPHA * cost + BETA * crowding * 100

    min_utility = min(s["utility"] for s in spots)

    for s in spots:
        s["is_optimal"] = (s["utility"] == min_utility)

    return spots

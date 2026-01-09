ALPHA = 0.6
BETA = 0.4

def find_equilibrium(spots):
    for s in spots:
        s["utility"] = ALPHA * s["cost"] + BETA * s["crowding"] * 100

    # ALWAYS choose exactly one optimal spot
    min_index = min(range(len(spots)), key=lambda i: spots[i]["utility"])

    for i, s in enumerate(spots):
        s["is_optimal"] = (i == min_index)

    return spots

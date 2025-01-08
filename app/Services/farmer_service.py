def calculate_distance_cost(distance, volume):
    return 0.05 * volume if distance <= 50 else 0.06 * volume

def calculate_price(volume, distance, is_bonus, semester):
    base_price = 1.80 if semester == "first" else 1.95
    cost_per_km = calculate_distance_cost(distance, volume)
    bonus = 0.01 * volume if is_bonus else 0
    return (volume * base_price) - cost_per_km + bonus
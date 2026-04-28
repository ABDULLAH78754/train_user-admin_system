
def calculate_fare(route, start_station, end_station):
    stations = list(route.keys())

    if start_station not in stations or end_station not in stations:
        return None, None

    start_index = stations.index(start_station)
    end_index = stations.index(end_station)

    distance = 0

    # Forward direction
    if start_index < end_index:
        for i in range(start_index + 1, end_index + 1):   # 👈 skip start
            distance += route[stations[i]]

    # Reverse direction
    else:
        for i in range(start_index - 1, end_index - 1, -1):  # 👈 skip start
            distance += route[stations[i]]

    fare = distance * 0.14
    return distance, fare
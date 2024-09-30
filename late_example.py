from event_tree import Event, EventTree


# Define events
get_up_late = Event(name="Get up late?")
car_starts = Event(name="Car starts?")
bus_available = Event(name="Bus available?")
roads_clear_car = Event(name="Roads clear (car)?")
roads_clear_bus = Event(name="Roads clear (bus)?")
late = Event(name="Late for work!")
not_late = Event(name="Not late for work!")

# Create the event tree
event_tree = EventTree()

# Add connections (edges) between events
event_tree.add_edge(from_event=get_up_late, to_event=car_starts, probability=0.1)
event_tree.add_edge(from_event=get_up_late, to_event=not_late, probability=0.9)
event_tree.add_edge(from_event=car_starts, to_event=roads_clear_car, probability=0.9)
event_tree.add_edge(from_event=car_starts, to_event=bus_available, probability=0.1)
event_tree.add_edge(from_event=bus_available, to_event=roads_clear_bus, probability=0.95)
event_tree.add_edge(from_event=bus_available, to_event=late, probability=0.05)
event_tree.add_edge(from_event=roads_clear_car, to_event=not_late, probability=0.4)
event_tree.add_edge(from_event=roads_clear_car, to_event=late, probability=0.6)
event_tree.add_edge(from_event=roads_clear_bus, to_event=not_late, probability=0.4)
event_tree.add_edge(from_event=roads_clear_bus, to_event=late, probability=0.6)

# Display paths to the consequences
event_tree.display_paths_and_probabilities(get_up_late, [late, not_late])

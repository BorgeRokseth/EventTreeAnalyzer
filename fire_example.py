from event_tree import EventTree, Event


# Define events
hazard_event = Event(name="Fire breakout?")
fast_spread = Event(name="Fire spreads fast?")
sprinkler_fail = Event(name="Sprinkler fails?")
evac_fails = Event(name="Workers cant be evacuated?")
fatalities = Event(name="Multiple fatalities!")
material_damage = Event(name="Significant material loss!")
fire_controlled = Event(name="Fire controlled!")
fire_contained = Event(name="Fire contained")
no_consequences = Event(name="No fire!")

# Create the event tree
event_tree = EventTree()

# Add connections (edges) between events
event_tree.add_edge(from_event=hazard_event, to_event=fast_spread, probability=0.1)
event_tree.add_edge(from_event=hazard_event, to_event=no_consequences, probability=0.9)
event_tree.add_edge(from_event=fast_spread, to_event=sprinkler_fail, probability=0.8)
event_tree.add_edge(from_event=fast_spread, to_event=fire_contained, probability=0.2)
event_tree.add_edge(from_event=sprinkler_fail, to_event=evac_fails, probability=0.01)
event_tree.add_edge(from_event=sprinkler_fail, to_event=fire_controlled, probability=0.99)
event_tree.add_edge(from_event=evac_fails, to_event=fatalities, probability=0.3)
event_tree.add_edge(from_event=evac_fails, to_event=material_damage, probability=0.7)


# Display paths to the consequences
event_tree.display_paths_and_probabilities(
    hazard_event,
    [fatalities, material_damage, fire_controlled, fire_contained, no_consequences]
)
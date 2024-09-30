class Event:
    def __init__(self, name: str):
        self.name = name


class Edge:
    def __init__(self, from_event: Event, to_event: Event, probability: float):
        self.from_event = from_event
        self.to_event = to_event
        self.probability = probability


class EventTree:
    def __init__(self):
        self.edges = []

    def add_edge(self, from_event: Event, to_event: Event, probability: float):
        # Create a directed edge between two events with the given probability
        self.edges.append(Edge(from_event, to_event, probability))

    def find_all_paths(self, start_event: Event, end_event: Event):
        # Find all possible paths from a starting event to an ending event
        paths = []
        self._dfs(start_event, end_event, [], 1.0, paths)
        return paths

    def display_paths_and_probabilities(self, start_event, consequences):
        paths = []
        for consequence in consequences:
            self._dfs(start_event, consequence, [], 1, paths)

        consequence_probabilities = {}
        for path, prob in paths:
            final_consequence = path[-1]
            if final_consequence not in consequence_probabilities:
                consequence_probabilities[final_consequence] = 0
            consequence_probabilities[final_consequence] += prob

        # Print paths and total probabilities
        for path, prob in paths:
            print(f"Path: {' -> '.join(event.name for event in path)}, Probability: {prob:.5f}")

        # Print summary of total probabilities for each consequence
        print("\nTotal Probabilities for Consequences:")
        for consequence, total_prob in consequence_probabilities.items():
            print(f"{consequence.name}: {total_prob:.5f}")

    def _dfs(self, current_event, target_event, path, path_prob, paths):
        path = path + [current_event]  # Append the current event to the path

        # If the target event is reached, store the current path and its probability
        if current_event == target_event:
            paths.append((path, path_prob))  # Store the complete path and its probability
            return  # Backtrack to explore other paths

        # Traverse all edges from the current event
        for edge in self.edges:
            if edge.from_event == current_event:  # Check if there's an outgoing edge from the current event
                self._dfs(edge.to_event, target_event, path, path_prob * edge.probability, paths)  # Recursive call


from copy import deepcopy

class top_trading_cycle:
    def __init__(self):
        self.participants = []
        self.phase1_ready = False
        self.phase2_ready = False
        self.finalPairs = []
        self.unmatched_goods = []
        self.unmatched_participants = []
        self.edges = []
        self.next_request = None

    def __str__(self):
        if self.phase1_ready == False:
            return "\nYou should first call .get_participants_and_goods() function.\n"
        elif self.phase2_ready == False:
            return "\nYou should call .top_trading_cycle_matcher() function.\n"
        else:
            output = str()
            sorted_list = sorted(self.finalPairs, key=lambda x: x[0])
            output += "\nMatched pairs:\n"
            for pair in sorted_list:
                output += f"participant{pair[0]} is mathced with goods{pair[1]}.\n"
            return output

    def get_participants_and_goods(self):
        participants_num = int(input("What is the number of participants? "))
        for participant in range(participants_num):
            participant_prefences = list(
                map(
                    int,
                    input(
                        f"Type {participants_num} goods based on the preferences of the participant{participant} from left to right and separate each one with a space: "
                    ).split(),
                )
            )
            self.participants.append(participant_prefences)
            self.unmatched_goods.append(participant)
            self.unmatched_participants.append(participant)
            self.edges.append([participant, self.participants[participant][0]])
        self.phase1_ready = True
        self.phase2_ready = False
        self.next_request = [0 for index in range(len(self.participants))]

    def cycle_detection(self):
        def BFS(node, path):
            def get_neighbors(node):
                neighbors = []
                for edges in self.edges:
                    if edges[0] == node:
                        neighbors.append(edges[1])
                return neighbors

            nonlocal cycle
            this_path = deepcopy(path)
            for neighbor in get_neighbors(node):
                if len(cycle) != 0:
                    return cycle[0]
                if neighbor not in visited_nodes:
                    visited_nodes.append(neighbor)
                    neighbor_path = deepcopy(this_path)
                    neighbor_path.append(neighbor)
                    BFS(neighbor, neighbor_path)
                else:
                    if neighbor in path:
                        start = this_path.index(neighbor)
                        cycle = this_path[start:]

        cycle = []
        visited_nodes = []
        for node in self.unmatched_participants:
            visited_nodes.append(node)
            BFS(node, [node])
            if len(cycle):
                return cycle

    def top_trading_cycle_matcher(self):
        def find_edge_tail(node):
            for edge in self.edges:
                if edge[0] == node:
                    return edge[1]

        def update_edges():
            self.edges = []
            for node in self.unmatched_participants:
                for good in self.participants[node][self.next_request[node] :]:
                    if good in self.unmatched_goods:
                        self.edges.append([node, good])
                        break
                    self.next_request[node] += 1

        while len(self.unmatched_participants):
            cycle = self.cycle_detection()
            for node in cycle:
                self.unmatched_participants.remove(node)
                good = find_edge_tail(node)
                self.unmatched_goods.remove(good)
                self.finalPairs.append([node, good])
            update_edges()
        self.phase2_ready = True


TTC = top_trading_cycle()
TTC.get_participants_and_goods()
TTC.top_trading_cycle_matcher()
print(TTC)
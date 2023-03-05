import math

# Ieroapostoloi kai Kanivaloi

# Ftiaxoume mia katastasi gia arxi


class State():
    def __init__(self, kanivaloiArxi, ieroapostoloiArxi, karavi, kanivaloiTelos, ieroapostoloiTelos):
        self.kanivaloiArxi = kanivaloiArxi
        self.ieroapostoloiArxi = ieroapostoloiArxi
        self.karavi = karavi
        self.kanivaloiTelos = kanivaloiTelos
        self.ieroapostoloiTelos = ieroapostoloiTelos
        self.parent = None
# An petuxame ton stoxo vgazei true (kanenas sta aristera)

    def is_goal(self):
        if self.kanivaloiArxi == 0 and self.ieroapostoloiArxi == 0:
            return True
        else:
            return False
# An einai egkuro einai true (diladi an ierapostoloi einai perissoteroi h isoi me tous kanivalous se opoiodipote meros)

    def is_valid(self):
        if self.ieroapostoloiArxi >= 0 and self.ieroapostoloiTelos >= 0 \
           and self.kanivaloiArxi >= 0 and self.kanivaloiTelos >= 0 \
           and (self.ieroapostoloiArxi == 0 or self.ieroapostoloiArxi >= self.kanivaloiTelos) \
           and (self.ieroapostoloiTelos == 0 or self.ieroapostoloiTelos >= self.kanivaloiTelos):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.kanivaloiArxi == other.kanivaloiArxi and self.ieroapostoloiArxi == other.ieroapostoloiArxi \
            and self.karavi == other.karavi and self.kanivaloiTelos == other.kanivaloiTelos \
            and self.ieroapostoloiTelos == other.ieroapostoloiTelos

    def __hash__(self):
        return hash((self.kanivaloiArxi, self.ieroapostoloiArxi, self.karavi, self.kanivaloiTelos, self.ieroapostoloiTelos))

# Oles oi katastaseis


def successors(cur_state):
    children = []
    if cur_state.karavi == 'left':
        new_state = State(cur_state.kanivaloiArxi, cur_state.ieroapostoloiArxi - 2, 'right',
                          cur_state.kanivaloiTelos, cur_state.ieroapostoloiTelos + 2)
        # 2 ieroapostoloi pane apo aristera sta deksia
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.kanivaloiArxi - 2, cur_state.ieroapostoloiArxi, 'right',
                          cur_state.kanivaloiTelos + 2, cur_state.ieroapostoloiTelos)
        # 2 kanivaloi pane apo aristera sta deksia
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.kanivaloiArxi - 1, cur_state.ieroapostoloiArxi - 1, 'right',
                          cur_state.kanivaloiTelos + 1, cur_state.ieroapostoloiTelos + 1)
        # 1 ieroapostolos kai 1 kanivalos pane apo aristera sta deksia
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.kanivaloiArxi, cur_state.ieroapostoloiArxi - 1, 'right',
                          cur_state.kanivaloiTelos, cur_state.ieroapostoloiTelos + 1)
        # 1 ieroapostolos paei apo aristera sta deksia
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.kanivaloiArxi - 1, cur_state.ieroapostoloiArxi, 'right',
                          cur_state.kanivaloiTelos + 1, cur_state.ieroapostoloiTelos)
        # 1 kanivalos paei apo aristera sta deksia
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    else:
        new_state = State(cur_state.kanivaloiArxi, cur_state.ieroapostoloiArxi + 2, 'left',
                          cur_state.kanivaloiTelos, cur_state.ieroapostoloiTelos - 2)
        # 2 ieroapostoloi pane apo deksia sta aristera
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.kanivaloiArxi + 2, cur_state.ieroapostoloiArxi, 'left',
                          cur_state.kanivaloiTelos - 2, cur_state.ieroapostoloiTelos)
        # 2 kanivaloi pane apo deksia sta aristera
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.kanivaloiArxi + 1, cur_state.ieroapostoloiArxi + 1, 'left',
                          cur_state.kanivaloiTelos - 1, cur_state.ieroapostoloiTelos - 1)
        # 1 ieroapostolos kai 1 kanivalos pane apo deksia sta aristera
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.kanivaloiArxi, cur_state.ieroapostoloiArxi + 1, 'left',
                          cur_state.kanivaloiTelos, cur_state.ieroapostoloiTelos - 1)
        # 1 ieroapostolos paei apo deksia sta aristera
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
        new_state = State(cur_state.kanivaloiArxi + 1, cur_state.ieroapostoloiArxi, 'left',
                          cur_state.kanivaloiTelos - 1, cur_state.ieroapostoloiTelos)
        # 1 kanivalos paei apo deksia sta aristera
        if new_state.is_valid():
            new_state.parent = cur_state
            children.append(new_state)
    return children

# xrisi tis anazitisis kata vathos (breadth-first search)


def breadth_first_search():
    initial_state = State(3, 3, 'left', 0, 0)
    if initial_state.is_goal():
        return initial_state
    frontier = list()
    explored = set()
    frontier.append(initial_state)
    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            return state
        explored.add(state)
        children = successors(state)
        for child in children:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return None

# Ena loop me tin sosti seira pou tha emfanizontai


def print_solution(solution):
    path = []
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        print("(" + str(state.kanivaloiArxi) + "," + str(state.ieroapostoloiArxi)
              + "," + state.karavi + "," + str(state.kanivaloiTelos) + "," +
              str(state.ieroapostoloiTelos) + ")")

# Kalountai oi sunartiseis kai emfanizetai i lusi


def main():
    solution = breadth_first_search()
    print("Ieroapostoloi kai Kanivaloi lusi:")
    print("(kanivaloiArxi,ieroapostoloiArxi,karavi,kanivaloiTelos,ieroapostoloiTelos):")
    print_solution(solution)


if __name__ == "__main__":
    main()

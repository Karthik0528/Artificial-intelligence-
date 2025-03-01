from collections import deque

def is_valid(state):
    """Check if the state is valid (no missionaries eaten)."""
    m1, c1, b, m2, c2 = state

    # Ensure no negative values and boat is correctly positioned
    if min(m1, c1, m2, c2) < 0 or b not in [0, 1]:
        return False

    # Missionaries cannot be outnumbered by cannibals on either side
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2):
        return False

    return True

def generate_next_states(state):
    """Generate all possible valid moves from the current state."""
    m1, c1, b, m2, c2 = state
    next_states = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Possible boat moves

    for m, c in moves:
        if b == 1:  # Boat on left side
            new_state = (m1 - m, c1 - c, 0, m2 + m, c2 + c)
        else:  # Boat on right side
            new_state = (m1 + m, c1 + c, 1, m2 - m, c2 - c)

        if is_valid(new_state):
            next_states.append(new_state)

    return next_states

def solve_missionaries_cannibals(initial_state, goal_state):
    """Solve the problem using BFS."""
    queue = deque([(initial_state, [])])  # (current_state, path)
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        # Check if goal reached
        if state == goal_state:
            return path + [state]

        # Generate next states
        for next_state in generate_next_states(state):
            queue.append((next_state, path + [state]))

    return None  # No solution found

# Input
initial_state = (3, 3, 1, 0, 0)  # (Missionaries Left, Cannibals Left, Boat, Missionaries Right, Cannibals Right)
goal_state = (0, 0, 0, 3, 3)  # (All moved to the right side)

solution = solve_missionaries_cannibals(initial_state, goal_state)

# Output solution
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")

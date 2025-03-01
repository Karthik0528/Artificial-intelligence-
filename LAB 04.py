from itertools import permutations

def solve_cryptarithmetic():
    letters = 'SENDMORY'  # Unique letters in the equation
    for perm in permutations(range(10), len(letters)):  # Generate digit assignments
        mapping = dict(zip(letters, perm))

        # Ensure no leading zeroes
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        # Convert words to numbers
        send = mapping['S']*1000 + mapping['E']*100 + mapping['N']*10 + mapping['D']
        more = mapping['M']*1000 + mapping['O']*100 + mapping['R']*10 + mapping['E']
        money = mapping['M']*10000 + mapping['O']*1000 + mapping['N']*100 + mapping['E']*10 + mapping['Y']

        if send + more == money:
            print(f"SOLUTION FOUND: {mapping}")
            print(f"{send} + {more} = {money}")
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()

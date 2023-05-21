
def switch_a(switch_state):
    switch_state[1] = "on" if switch_state[1] == "off" else "off"
    switch_state[3] = "on" if switch_state[3] == "off" else "off"
    return switch_state

def switch_b(switch_state):
    switch_state[2] = "on" if switch_state[2] == "off" else "off"
    switch_state[4] = "on" if switch_state[4] == "off" else "off"
    return switch_state

def switch_c(switch_state):
    switch_state[1] = "on" if switch_state[1] == "off" else "off"
    switch_state[2] = "on" if switch_state[2] == "off" else "off"
    switch_state[3] = "on" if switch_state[3] == "off" else "off"
    switch_state[4] = "on" if switch_state[4] == "off" else "off"
    return switch_state

def switch_d(switch_state):
    switch_state[1] = "on" if switch_state[1] == "off" else "off"
    switch_state[4] = "on" if switch_state[4] == "off" else "off"
    return switch_state

def switch_e(switch_state):
    switch_state[1] = "off"
    switch_state[2] = "off"
    switch_state[3] = "off"
    switch_state[4] = "off"
    return switch_state


def main(original_state, expected_output):
    # Order of switches to check
    switches = ['a', 'b', 'c', 'd', 'e']

    # Try disabling each switch one by one and check if the output matches the expected output
    for switch in switches:
        # make a copy of the original state dudududu
        temp_state = original_state.copy()

        # C# mechanics switch statement equivalent
        if switch == 'e':
            temp_state = switch_c(temp_state)
            temp_state = switch_a(temp_state)
            temp_state = switch_d(temp_state)
            temp_state = switch_b(temp_state)
            if temp_state == expected_output:
                print('process flow, c, a, d, b')

        elif switch == 'c':
            temp_state = switch_e(temp_state)
            temp_state = switch_a(temp_state)
            temp_state = switch_d(temp_state)
            temp_state = switch_b(temp_state)
            if board_state == expected_output:
                print('process flow, e, a, d, b')

        elif switch == 'a':
            temp_state = switch_e(temp_state)
            temp_state = switch_c(temp_state)
            temp_state = switch_d(temp_state)
            temp_state = switch_b(temp_state)
            if board_state == expected_output:
                print('process flow, e, c, d, b')

        elif switch == 'd':
            temp_state = switch_e(temp_state)
            temp_state = switch_c(temp_state)
            temp_state = switch_a(temp_state)
            temp_state = switch_b(temp_state)
            if board_state == expected_output:
                print('process flow, e, c, a, b')

        elif switch == 'b':
            temp_state = switch_e(temp_state)
            temp_state = switch_c(temp_state)
            temp_state = switch_a(temp_state)
            temp_state = switch_d(temp_state)
            if temp_state == expected_output:
                print('process flow, e, c, a, d')

        # Check if the modified board state matches the expected output
        if temp_state == expected_output:
            return switch  # Return the switch that needs to be disabled

    return "No switch found"  # Return this if no switch needs to be disabled

if __name__ == "__main__":
    board_state = {1: "off", 2: "on", 3: "off", 4: "off", }
    expect_result = {1: "on", 2: "on", 3: "off", 4: "on", }
    switch_to_disable = main(board_state, expect_result)
    print("Switch to disable:", switch_to_disable)

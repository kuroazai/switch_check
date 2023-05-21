

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
    # temp_switch = switch_e(original_state_v2)
    # print('switch e', board_state)
    #
    # temp_switch = switch_c(temp_switch)
    # print('switch c', temp_switch)
    #
    # temp_switch = switch_a(temp_switch)
    # print('switch a', temp_switch)
    #
    # temp_switch = switch_d(temp_switch)
    # print('switch d', temp_switch)
    #
    # temp_switch = switch_b(original_state_v2)
    # print('switch b', temp_switch,)
    # original_state = board_state.copy()  # Create a copy of the original board state
    #
    # print('result', temp_switch, )
    # Try disabling each switch one by one and check if the output matches the expected output
    
    switches = ['a', 'b', 'c', 'd', 'e']  # Order of switches to check

    # Try disabling each switch one by one and check if the output matches the expected output
    for switch in switches:

        board_state = original_state.copy()

        if switch == 'e':
            board_state = switch_c(board_state)
            board_state = switch_a(board_state)
            board_state = switch_d(board_state)
            board_state = switch_b(board_state)
            if board_state == expected_output:
                print('process flow, c, a, d, b')

        elif switch == 'c':
            board_state = switch_e(board_state)
            board_state = switch_a(board_state)
            board_state = switch_d(board_state)
            board_state = switch_b(board_state)
            if board_state == expected_output:
                print('process flow, e, a, d, b')

        elif switch == 'a':
            board_state = switch_e(board_state)
            board_state = switch_c(board_state)
            board_state = switch_d(board_state)
            board_state = switch_b(board_state)
            if board_state == expected_output:
                print('process flow, e, c, d, b')

        elif switch == 'd':
            board_state = switch_e(board_state)
            board_state = switch_c(board_state)
            board_state = switch_a(board_state)
            board_state = switch_b(board_state)
            if board_state == expected_output:
                print('process flow, e, c, a, b')

        elif switch == 'b':
            board_state = switch_e(board_state)
            board_state = switch_c(board_state)
            board_state = switch_a(board_state)
            board_state = switch_d(board_state)
            if board_state == expected_output:
                print('process flow, e, c, a, d')

        # Check if the modified board state matches the expected output
        if board_state == expected_output:
            return switch  # Return the switch that needs to be disabled

    return "No switch found"  # Return this if no switch needs to be disabled

if __name__ == "__main__":
    board_state = {1: "off", 2: "on", 3: "off", 4: "off", }
    expected_output = {1: "on", 2: "on", 3: "off", 4: "on", }
    switch_to_disable = main(board_state, expected_output)
    print("Switch to disable:", switch_to_disable)

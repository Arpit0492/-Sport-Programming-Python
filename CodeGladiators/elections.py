
def convert_to_int(ele):
    return int(ele)


t = int(input())
tc_ans = []
for tc in range(t):
    states_phases = input()  # r and c
    phases = input()
    phase_wise_seats = [convert_to_int(x) for x in phases.strip().split(' ')]
    elec_phases = sum(1 for ph in phase_wise_seats if ph > 0)
    max_phase = max(phase_wise_seats)
    phase_seats_sum = sum(phase_wise_seats)

    states = input()
    state_wise_seats = [convert_to_int(x) for x in states.strip().split(' ')]
    elec_states = sum(1 for ph in state_wise_seats if ph > 0)
    max_state = max(state_wise_seats)
    state_seats_sum = sum(state_wise_seats)


    for j in state_wise_seats:
        for k in phase_wise_seats:
            phase_wise_seats[k] -= 1

    if phase_seats_sum == state_seats_sum and elec_phases >= max_state and elec_states >= max_phase:
        tc_ans.append('YES')
    else:
        tc_ans.append('NO')

for ans in tc_ans:
    print(ans)

'''
3
3 3
3 2 1
1 2 2
3 2
2 1 0
1 2
4 4
4 4 4 1
4 4 4 1
'''
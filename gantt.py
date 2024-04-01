##################################################################'''
# Nicholas Rios - 0perating Systems Gantt Chart Project
#
#Requirements:
# 1. Generate 10 Processes
# 2. id, random number burst, arrival time (0...11)
#
# Functions:
# 1. FCFS
# 2. SRTF
# 3. Round Robin (q=2)

# Calculate:
# 1. Average wait time
# 2. Average turnaround time
#
##############################################################################
import random

class Process:
    def __init__(self, id, arrival_time):
        self.id = id
        self.burst = random.randint(1, 30)
        self.arrival_time = arrival_time


def generate_processes():
    '''
    Generates 10 processes with arrival times between 0 and 11

    :return: A list of processes with incremented id, random arrival_time between 0-11, and randomized burst between 1-30
    '''
    processes = []
    for i in range(10):
        processes.append(Process(i + 1, random.randint(0,11)))

    return processes


def calculate_wait_time(gantt_chart):
    '''
    Calculates the turnaround time for each process in a gantt chart

    :param gantt_chart: A list of 10 tuples containing the process id, process arrival time, start time, end time, and remaining burst time.
    :return: A dictionary where keys are process_ids, and values are integers representing the wait time for a given process_id
    '''
    wait_time = {}
    for i in range(len(gantt_chart)):
        process_id, start_time, _, arrival_time, _ = gantt_chart[i]
        wait_time[process_id] = max(start_time - arrival_time, 0) 
    return wait_time


def calculate_turnaround_time(gantt_chart):
    '''
    Calculates the waiting time for each process in a given gantt chart

    :param gantt_chart: A list of 10 tuples containing the process id, process arrival time, start time, end time, and remaining burst time.
    :return: A dictionary where keys are process_ids, and values are integers representing the turnaround time for a given process_id 
    '''
    turnaround_time = {}
    for i in range(len(gantt_chart)):
        process_id, start_time, end_time, _, _ = gantt_chart[i]
        turnaround_time[process_id] = end_time - start_time
    return turnaround_time
    

def calculate_avg_wait_time(gantt_chart):
    '''
    Calculates the average wait time for a given gantt chart

    :param gantt_chart: A list of 10 tuples containing the process id, process arrival time, start time, end time, and remaining burst time
    :return: The average wait time of the gantt chart as an integer
    '''
    total_wait_time = sum(max(start_time - arrival_time, 0) for _, start_time, _, arrival_time, _ in gantt_chart)
    return total_wait_time // 10


def calculate_avg_turnaround_time(gantt_chart):
    '''
    Calculates the average turnaround time for a given gantt chart

    :param gantt_chart: A list of 10 tuples containing the process id, process arrival time, start time, end time, and remaining burst time
    :return: The average turnaround time of the gantt chart as an integer
    '''
    total_turnaround_time = sum(end_time - start_time for _, start_time, end_time, _, _ in gantt_chart)
    return total_turnaround_time // 10



###############################################################
# FCFS
###############################################################
def create_fcfs_gantt(processes):
    '''
    Creates gantt chart with first-come, first-served scheduling algorithm

    :param processes: A list of Process objects representing the processes to be scheduled
    :return: A list of tuples containing the process id, process arrival_time, process schedule start_time, and process schedule end_time.
    '''
    processes.sort(key=lambda x: x.arrival_time)

    curr_time = 0
    gantt_chart = []

    for process in processes:
        start_time = max(curr_time, process.arrival_time)
        end_time = start_time + process.burst
        curr_time = end_time

        remaining_burst = process.burst - process.burst 

        gantt_chart.append((process.id, start_time, end_time, process.arrival_time, remaining_burst))

    return gantt_chart


# Generating a gantt chart for output
fcfs_gantt = create_fcfs_gantt(generate_processes())
print("                FCFS GANTT CHART")
print("| Process | Arrival | Start | End  |  Rem. Burst  |")
print("---------------------------------------------------")

# Printing the FCFS gantt chart data
for process_id, start_time, end_time, arrival_time, burst in fcfs_gantt:
    print(f"|   P{process_id:<3}  |    {arrival_time:<4} | {start_time:<5} | {end_time:<4} | {burst:<12} |")
print("---------------------------------------------------")

# Calculating wait time and turnaround time for FCFS
fcfs_wait_time = calculate_wait_time(fcfs_gantt)
fcfs_turnaround_time = calculate_turnaround_time(fcfs_gantt)

# Sorting the wait time and turnaround time dictionaries by process ID
sorted_fcfs_wait_time = dict(sorted(fcfs_wait_time.items()))
sorted_fcfs_turnaround_time = dict(sorted(fcfs_turnaround_time.items()))

# Printing wait time and turnaround time for each process in FCFS
print("| Process |    Wait Time   |    Turnaround Time   |")
print("---------------------------------------------------")
for process_id in sorted_fcfs_wait_time.keys():
    wait = fcfs_wait_time[process_id]
    turnaround = fcfs_turnaround_time[process_id]
    print(f"| P{process_id:<6} | {wait:<11} ms | {turnaround:<17} ms |")
print("---------------------------------------------------")

# Printing average wait time and average turnaround time for FCFS
print(f"Average Wait Time: {calculate_avg_wait_time(fcfs_gantt)} ms")
print(f"Average Turnaround Time: {calculate_avg_turnaround_time(fcfs_gantt)} ms")

print("***************************************************\n")



###############################################################
# SRTF
###############################################################
def create_srtf_gantt(processes):
    '''
    Creates gantt chart with shortest-remaining time first scheduling algorithm

    :param processes: A list of Process objects representing the processes to be scheduled
    :return: A list of tuples containing the process id, process arrival_time, process schedule start_time, process schedule end_time, and remaining burst time.
    '''
    processes.sort(key=lambda x: x.arrival_time)

    gantt_chart = []
    curr_time = 0
    remaining_processes = list(processes)

    while remaining_processes:
        available_processes = [process for process in remaining_processes if process.arrival_time <= curr_time]

        # If no processes are available at the current time, continue until one arrives
        if not available_processes:
            curr_time = min(process.arrival_time for process in remaining_processes)
            continue
        
        # Finding the process with the shortest remaining burst time
        shortest_process = min(available_processes, key=lambda x: x.burst)  
        start_time = curr_time
        end_time = curr_time + 1
        remaining_burst = shortest_process.burst - 1

        # Checking if current short process has the same id as the previous one to group them in the same row 
        if gantt_chart and gantt_chart[-1][0] == shortest_process.id:
            # If the last gantt_chart entry has the same id as the current shortest_process, mutate the end time and remaining burst time
            gantt_chart[-1] = (gantt_chart[-1][0], gantt_chart[-1][1], end_time, gantt_chart[-1][3], remaining_burst)
        else:
            # If the current shortest_process.id is different from the last one, append the new process to the Gantt chart
            gantt_chart.append((shortest_process.id, start_time, end_time, shortest_process.arrival_time, remaining_burst))

        # Updating the current time and remaining burst time of the currently shortest process
        curr_time = end_time
        if remaining_burst == 0:
            remaining_processes.remove(shortest_process)
        else:
            remaining_processes.remove(shortest_process)
            shortest_process.burst = remaining_burst
            remaining_processes.append(shortest_process)

    return gantt_chart 


# Generating a gantt chart for output
srtf_gantt = create_srtf_gantt(generate_processes())

print("                SRTF GANTT CHART")
print("| Process | Arrival | Start | End  |  Rem. Burst  |")
print("---------------------------------------------------")

# Printing the SRTF gantt chart data
for process_id, start_time, end_time, arrival_time, burst in srtf_gantt:
    print(f"|   P{process_id:<3}  |    {arrival_time:<4} | {start_time:<5} | {end_time:<4} | {burst:<12} |")
print("---------------------------------------------------")

# Calculating wait time and turnaround time for SRTF
srtf_wait_time = calculate_wait_time(srtf_gantt)
srtf_turnaround_time = calculate_turnaround_time(srtf_gantt)

# Sorting the wait time and turnaround time dictionaries by process ID
sorted_srtf_wait_time = dict(sorted(srtf_wait_time.items()))
sorted_srtf_turnaround_time = dict(sorted(srtf_turnaround_time.items()))

# Printing wait time and turnaround time for SRTF
print("| Process |    Wait Time   |    Turnaround Time   |")
print("---------------------------------------------------")
for process_id in sorted_srtf_wait_time.keys():
    wait = srtf_wait_time[process_id]
    turnaround = srtf_turnaround_time[process_id]
    print(f"| P{process_id:<6} | {wait:<11} ms | {turnaround:<17} ms |")

# Printing average wait time and average turnaround time for SRTF
print(f"Average Wait Time: {calculate_avg_wait_time(srtf_gantt)} ms")
print(f"Average Turnaround Time: {calculate_avg_turnaround_time(srtf_gantt)} ms")

print("***************************************************\n")



###############################################################
# ROUND ROBIN
###############################################################
def create_round_robin_gantt(processes):
    '''
    Creates gantt chart with the round robin scheduling algorithm

    :param processes: A list of Process objects representing the processes to be scheduled
    :return: A list of tuples containing the process id, process arrival_time, process schedule start_time, and process schedule end_time.
    '''
    processes.sort(key=lambda x: x.arrival_time)
    
    queue = processes[:]
    quantum = 3
    curr_time = 0
    gantt_chart = []

    while queue:
        process = queue.pop(0)
        start_time = max(curr_time, process.arrival_time)

        if process.burst <= quantum:
            end_time = start_time + process.burst
            curr_time = end_time

            gantt_chart.append((process.id, start_time, end_time, process.arrival_time, process.burst))
        else:
            end_time = start_time + quantum
            curr_time = end_time

            gantt_chart.append((process.id, start_time, end_time, process.arrival_time, process.burst))

            process.burst -= quantum
            queue.append(process)

    return gantt_chart


# Generating a gantt chart for output
round_robin_gantt = create_round_robin_gantt(generate_processes())
print("              ROUND ROBIN GANTT CHART")
print("| Process | Arrival | Start | End  |  Rem. Burst  |")
print("---------------------------------------------------")

# Printing the Round Robin gantt chart data
for process_id, start_time, end_time, arrival_time, burst in round_robin_gantt:
    print(f"|   P{process_id:<3}  |    {arrival_time:<4} | {start_time:<5} | {end_time:<4} | {burst:<12} |")
print("---------------------------------------------------")

# Calculating wait time and turnaround time for Round Robin
rr_wait_time = calculate_wait_time(round_robin_gantt)
rr_turnaround_time = calculate_turnaround_time(round_robin_gantt)

# Sorting the wait time and turnaround time dictionaries by process ID
sorted_rr_wait_time = dict(sorted(rr_wait_time.items()))
sorted_rr_turnaround_time = dict(sorted(rr_turnaround_time.items()))

# Printing wait time and turnaround time for Round Robin
print("| Process |    Wait Time   |    Turnaround Time   |")
print("---------------------------------------------------")
for process_id in sorted_srtf_wait_time.keys():
    wait = rr_wait_time[process_id]
    turnaround = rr_turnaround_time[process_id]
    print(f"| P{process_id:<6} | {wait:<11} ms | {turnaround:<17} ms |")

# Printing average wait time and average turnaround time for Round Robin
print(f"Average Wait Time: {calculate_avg_wait_time(round_robin_gantt)} ms")
print(f"Average Turnaround Time: {calculate_avg_turnaround_time(round_robin_gantt)} ms")

print("***************************************************\n")
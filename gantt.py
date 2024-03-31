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

    :return:  list of processes with incremented id, random arrival_time between 0-11, and randomized burst between 1-30
    '''
    processes = []
    for i in range(10):
        processes.append(Process(i + 1, random.randint(0,11)))
    return processes


def create_fcfs_gantt(processes):
    '''
    Creates gantt chart with first-come, first-served scheduling algorithm

    :param processes: A list of Process objects representing the processes to be scheduled.
    :return: A list of tuples containing the process id, process arrival_time, process schedule start_time, and process schedule end_time.
    '''
    processes.sort(key=lambda x: x.arrival_time)

    curr_time = 0
    gantt_chart = []

    for process in processes:
        start_time = max(curr_time, process.arrival_time)
        end_time = start_time + process.burst
        gantt_chart.append((process.id, start_time, end_time, process.arrival_time))
        curr_time = end_time

    return gantt_chart

def create_srtf_gantt(processes):
    '''
    Creates gantt chart with shortest-remaining time first scheduling algorithm

    :param processes: A list of Process objects representing the processes to be scheduled.
    :return: A list of tuples containing the process id, process arrival_time, process schedule start_time, and process schedule end_time.
    '''
    processes.sort(key=lambda x: x.arrival_time)

    queue = []
    gantt_chart = []

    return gantt_chart

def create_round_robin_gantt(processes):
    '''
    Creates gantt chart with the round robin scheduling algorithm

    :param processes: A list of Process objects representing the processes to be scheduled.
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



##################################################################
# FCFS
##################################################################
fcfs_gantt = create_fcfs_gantt(generate_processes())
print("       FCFS GANTT CHART")
print("| Process | Arrival | Start | End  |")
print("------------------------------------")

# Printing the fcfs gantt chart data
for process_id, start_time, end_time, arrival_time in fcfs_gantt:
    print(f"|   P{process_id:<3}  |    {arrival_time:<4} | {start_time:<5} | {end_time:<4} |")

print("************************************\n")



##################################################################
# SRTF
##################################################################
srtf_gantt = create_srtf_gantt(generate_processes())

print("       SRTF GANTT CHART")
print("| Process | Arrival | Start | End  |")
print("------------------------------------")

# Printing the srtf gantt chart data
for process_id, start_time, end_time, arrival_time in srtf_gantt:
    print(f"|   P{process_id:<3}  |    {arrival_time:<4} | {start_time:<5} | {end_time:<4} |")

print("************************************\n")



##################################################################
# ROUND ROBIN
##################################################################
round_robin_gantt = create_round_robin_gantt(generate_processes())
print("       ROUND ROBIN GANTT CHART")
print("| Process | Arrival | Start | End  | Rem. Burst |")
print("-------------------------------------------------")

# Printing the round robin gantt chart data
for process_id, start_time, end_time, arrival_time, burst in round_robin_gantt:
    print(f"|   P{process_id:<3}  |    {arrival_time:<4} | {start_time:<5} | {end_time:<4} | {burst:<10} |")


print("************************************")

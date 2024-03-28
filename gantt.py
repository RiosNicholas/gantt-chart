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


def fcfs_gantt(processes):
    '''
    Creates gantt chart with first-come, first-served algorithm

    :param processes:
    :return:
    '''
    processes.sort(lambda x: x.arrival_time)
    curr_time = 0
    gantt_chart = []

    for process in processes:

def srtf_gantt(processes):
    '''
    Creates gantt chart with first-come, first-served algorithm

    :param processes:
    :return:
    '''
    processes.sort(lambda x: x.arrival_time)
    pass

def round_robin_gantt(processes):
    '''
    Creates gantt chart with first-come, first-served algorithm

    :param processes:
    :return:
    '''
    processes.sort(lambda x: x.arrival_time)
    pass

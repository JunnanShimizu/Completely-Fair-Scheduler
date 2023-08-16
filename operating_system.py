# Junnan Shimizu
# 3/20/22
# Project_Three
# Course: CS337
#
# import random
# import process
# import scheduler
# import RBTree
# import pandas as pd
#
#
# def kernel(selected_scheduler, processes, quantum, verbose=True):
#     cpu = []
#     ready = RBTree.RBTree()
#     time = 0
#     average_wait_time = 0
#     average_turnaround_time = 0
#
#     scheduler.add_ready(processes, ready, time)
#
#     while ready.get_size() > 0:
#         time = selected_scheduler(processes, ready, cpu, time, quantum)
#
#     for current in processes:
#         average_wait_time += current.get_wait_time()
#         average_turnaround_time += current.get_turnaround_time()
#
#     average_wait_time = average_wait_time / len(processes)
#     average_turnaround_time = average_turnaround_time / len(processes)
#
#     df = pd.DataFrame(cpu)
#     df = df.append({'Wait_Time': average_wait_time, 'Turnaround_Time': average_turnaround_time},
#                    ignore_index=True)
#     df.to_csv("results.csv", index=False)

"""
For this problem, use the same data set as in the previous problem.
Your task now is to run the greedy algorithm that schedules jobs
(optimally) in decreasing order of the ratio (weight/length).
In this algorithm, it does not matter how you break ties. You
should report the sum of weighted completion times of the
resulting schedule --- a positive integer --- in the box below.
"""
from __future__ import division

def cmp_jobs(ja,jb):
##    result = cmp(ja[-1],jb[-1])
##    if result == 0:
##        result = cmp(ja[0],jb[0])
    return cmp(ja[-1],jb[-1]) or cmp(ja[0],jb[0])
    
def jobs_schedule_by_ratio(jobs):
    jobs.sort(cmp_jobs,reverse=True)
    comp_time = 0
    weighted_comp_time = 0
    
    for job in jobs:
        weight = job[0]
        length = job[1]
        comp_time += length 
        weighted_comp_time += comp_time * weight
    return weighted_comp_time
    

############################
if __name__ == "__main__":
    num_of_jobs = 0
    idx = True
    jobs = []
    
    with open("jobs.txt") as f:
        for line in f:
            if idx:
                num_of_jobs = int(line)
                idx = False
            else:
                job = [int(num) for num in line.split()]
                weight = job[0]
                length = job[1]
                jobs.append([weight,length,weight/length]) #create jobs list by [weight,length,ratio]
    print len(jobs),num_of_jobs
    print jobs_schedule_by_ratio(jobs)

"""
In this programming problem and the next you'll code up the greedy 
algorithms from lecture for minimizing the weighted sum of completion
times.. Download the text file here. This file describes a set of 
jobs with positive and integral weights and lengths. It has the 
format
[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...
For example, the third line of the file is "74 59", indicating that 
the second job has weight 74 and length 59. You should NOT assume 
that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that 
schedules jobs in decreasing order of the difference (weight - length). 
Recall from lecture that this algorithm is not always optimal. 
IMPORTANT: if two jobs have equal difference (weight - length), 
you should schedule the job with higher weight first. 
Beware: if you break ties in a different way, you are likely to 
get the wrong answer. You should report the sum of weighted completion
times of the resulting schedule --- a positive integer --- in the box below.

ADVICE: If you get the wrong answer, try out some small test cases 
to debug your algorithm (and post your test cases to the discussion forum)!
"""
def cmp_jobs(ja,jb):
##    result = cmp(ja[-1],jb[-1])
##    if result == 0:
##        result = cmp(ja[0],jb[0])
    return cmp(ja[-1],jb[-1]) or cmp(ja[0],jb[0])
    
def jobs_schedule(jobs):
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
                jobs.append([weight,length,weight-length])
    print len(jobs),num_of_jobs
    print jobs_schedule(jobs)



    
            

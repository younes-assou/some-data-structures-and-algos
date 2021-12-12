# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def sift_down(i,data,size):
    minindex = i
    l = 2*i+1
    r = 2*i+2

    if l<size:
        if data[l][0] < data[minindex][0]:
            minindex = l
        elif data[l][0] == data[minindex][0]:
            if data[l][1] < data[minindex][1]:
                minindex = l

    if r<size:
        if data[r][0] < data[minindex][0]:
            minindex = r
        elif data[r][0] == data[minindex][0]:
            if data[r][1] < data[minindex][1]:
                minindex = r

    if i != minindex:
        data[i], data[minindex] = data[minindex], data[i]
        sift_down(minindex,data,size)

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [(0,i)for i in range(n_workers)]
    for job in jobs:
        result.append(AssignedJob(next_free_time[0][1], next_free_time[0][0]))
        next_free_time[0] = (next_free_time[0][0]+job, next_free_time[0][1])
        sift_down(0,next_free_time,n_workers)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

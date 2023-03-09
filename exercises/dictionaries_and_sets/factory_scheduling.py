from collections import defaultdict

T, N = map(int, input().split())
tasks = []

for _ in range(N):
    tasks.append(tuple(map(int, input().split())))

time_moments = defaultdict(lambda: 0)

for s, e in tasks:
    time_moments[s] += 1
    time_moments[e] -= 1

time_moments = list(time_moments.items())
time_moments.sort()

active_tasks = 0
time_span = 0
max_time_span = 0
total = 0
prev_t = 0

for t, active in time_moments:
    time_span = t - prev_t

    # if there are no active tasks the time between prev_t and t is spent 
    # doing nothing
    if active_tasks == 0:
        total += time_span
        if time_span > max_time_span:
            max_time_span = time_span

    active_tasks += active
    prev_t = t

print(total, max_time_span)

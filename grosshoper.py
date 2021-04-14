n = 10000
jumps = 10

def count_trajectories(n, jumps):
    traj = [0] * (n + 1)

    for i in range(1, jumps + 1):
        traj[i] = 2**(i-1)

    for i in range(jumps + 1, n + 1):
        for j in range(jumps + 1):
            traj[i] += traj[i-j]
    return traj

print(count_trajectories(n, jumps))
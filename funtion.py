from math import pow
time_1_lenh=22*pow(10,-9)
time_1_congdoan=5*pow(10,-9)
def step_by_step(n):
    Step=n*time_1_lenh
    return Step
def pipelining(n):
    pipe=5*time_1_congdoan+(n-1)*time_1_congdoan
    return pipe
def tile(Step,pipe):
    tile=pipe/Step
    return tile

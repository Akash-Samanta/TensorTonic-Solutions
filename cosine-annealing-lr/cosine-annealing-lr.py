import math
def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    """
    Compute the learning rate using cosine annealing.
    """
    if current_step == 0:
        return base_lr 
    if current_step == total_steps:
        return min_lr

    return min_lr + ((base_lr - min_lr) / 2) * (1 + math.cos(math.pi * current_step / total_steps) )
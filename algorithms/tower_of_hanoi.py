def hanoi_tower(n_disks, current_rod, goal_rod, aux_rod):
    """Move n_disks from current_rod to goal_road."""
    if n_disks == 1:
        return 1

    hanoi_tower(n_disks-1, current_rod, aux_rod, goal_rod)
    hanoi_tower(n_disks-1, aux_rod, goal_rod, current_rod)

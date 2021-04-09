def hanoi_tower(n_disks, current_rod, goal_rod, aux_rod):
    """Move n_disks from current_rod to goal_road."""
    if n_disks == 1:
        print("Move disk 1 from rod", current_rod, "to rod", goal_rod)
        return 1

    hanoi_tower(n_disks-1, current_rod, aux_rod, goal_rod)
    print("Move disk", n_disks,"from rod", current_rod, "to rod", goal_rod)
    hanoi_tower(n_disks-1, aux_rod, goal_rod, current_rod)

n = 3
hanoi_tower(n, 1, 2, 3)

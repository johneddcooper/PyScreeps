def cantor_pair(n1, n2):
    """
    Cantor pairing to ensure no task priority collisions
    """
    return int(0.5 * (n1 + n2) * (n1 + n2 + 1) + n2)

def edit_distance_2(source:str, target:str) -> int:
    if source == 0:
        return len(target)
    elif target == 0:
        return len(source)
    
    delta = int(source[-1] != target[-1])
    return min(
        edit_distance_2(source[:-1], target[:-1]) + delta,
        edit_distance_2(source, target[:-1]) + 1,
        edit_distance_2(source[:-1], target) + 1,
    )
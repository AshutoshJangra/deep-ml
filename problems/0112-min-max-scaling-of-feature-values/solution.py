def min_max(x: list[int]) -> list[float]:
    mn = min(x)
    mx = max(x)
    rs = []
    if mn == mx:
        return [0.0 for _ in x]
    for i in x:
        rs.append((i - mn)/(mx - mn))
    return rs
	pass
def answer(L, R):
    if not (2 * L <= R):
        return -1
    return (L, 2 * L)

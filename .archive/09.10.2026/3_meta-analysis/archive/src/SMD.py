
def SMD(n1, n2, y1, y2, sd1, sd2):
    sd = (
        (((n1 - 1) * sd1**2) + ((n2 - 1) * sd2**2))
        / (n1 + n2 - 2)
    )
    sp = np.sqrt(sd)
    return round((np.abs(y1 - y2) / sp), 3)

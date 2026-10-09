def seSMD(n1, n2, smd):
    se = np.sqrt(
        (n1 + n2)/(n1*n2)
        + smd**2/(2*(n1+n2-2))
    )
    se = round(se, 3)
    return se

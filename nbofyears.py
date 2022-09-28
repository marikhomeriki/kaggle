from numpy import percentile


def nb_year(p0, percent, aug, p):
    years = 0
    percent = percent/100
    while p0 < p:
        p0 = p0 + p0*percent + aug
        years += 1

    return years


p0 = 1000
percent = 2
aug = 50
p = 1200
print(nb_year(p0, percent, aug, p))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500, 5, 100, 5000))

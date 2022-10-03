def area_or_perimeter(l, w):
    if l == w:
        return l*w
    else:
        return 2*(l+w)


l = 3
w = 3
print(area_or_perimeter(l, w))

l = 3
w = 2
print(area_or_perimeter(l, w))

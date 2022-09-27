def count_substring(string, sub_string):
    length = len(string)
    x = string.find(sub_string)
    n = 0
    while x != -1:
        string = string[x+1:]
        x = string.find(sub_string)
        n += 1
    return n


string = 'ABCDCDC'
sub_string = 'CDC'

print(count_substring(string, sub_string))

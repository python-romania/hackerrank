# Merge the tools

def merge_the_tools(s_, k_):
    parts = [s_[i:i+k_] for i in range(0, len(s_), k_)]
    for part in parts:
        keep = remove_subsequent(part)
        print("".join(keep))


def remove_subsequent(part_):
    keep_ = []
    rm_ = []
    for x in list(part_):
        if x not in keep_:
            keep_.append(x)
        else:
            rm_.append(x)
    return keep_


string = "AABCAAADA"
k = 3

merge_the_tools(string, k)

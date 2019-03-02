def pageCount(n, p):
    half_pages = n // 2 # in => 6 = 6 // 2 = 3
    half_page = p // 2 # in => 2 = 2 // 1 = 1
    diff = half_pages - half_page # 3 - 1 = 2 -> display smaller half_page

    if diff <= half_page:
        return diff
    else:
        return half_page

    # or return min(diff, half_page)


pages = int(input())
page = int(input())

print(pageCount(pages, page))

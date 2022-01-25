def uniqueList(list):
    ans = []

    for i in list:
        if i not in ans:
            ans.append(i)

    return ans

print(uniqueList([2, 4, 4, 4, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8, 8, 8]))
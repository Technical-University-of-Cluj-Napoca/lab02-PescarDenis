from collections import defaultdict
def group_anagrams(strs : list[str]) ->list[list[str]] :
    ans = defaultdict(list)

    for s in strs : 
        key = "".join(sorted(s))
        ans[key].append(s)
    return list(ans.values())

#print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_anagrams(["a"]))

def find_shortest_longest_list():
    l = ["go", "hello", "hi", "klp", "npj"]
    shortest = l[0]
    longest = l[0]
    for i in l:
        if len(i) < len(shortest):
            shortest = i
        elif len(i) > len(longest):
            longest = i
    return shortest, longest


print(find_shortest_longest_list())

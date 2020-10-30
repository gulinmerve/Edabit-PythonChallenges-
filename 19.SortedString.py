lst=[ [ "A", 6, 5, 3 ], [ "C", 4, 4, 0 ], [ "B", 1, 4, -3 ],[ "D", 6, 5, 0 ]]
print(sorted(lst, key=lambda lst:lst[1:], reverse=True))
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
            print('does it get here again')
        flist.append(print_i)
    # print(flist)
    return flist
# make_functions()
functions = make_functions()
# print(functions)
for f in functions:
    print(f)
    f()
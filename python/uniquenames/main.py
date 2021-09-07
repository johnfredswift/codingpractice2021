def unique_names(names1, names2):
    unique_names_list = []
    for name in names1:
        if not unique_names_list.__contains__(name):
            unique_names_list.append(name)
    for name in names2:
        if not unique_names_list.__contains__(name):
            unique_names_list.append(name)
    return unique_names_list

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
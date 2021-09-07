def group_by_owners(files):
    owners = {}
    #iterate over the dict once, this should be an O(n)
    for file, owner in files.items():
        if owner in owners:
            #append to 2d array in dict of existing owner
            newFilesList = owners[owner].append(file)
        else:
            #add new k,[v] to owners
            owners[owner] = [file]
        

    return owners


if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
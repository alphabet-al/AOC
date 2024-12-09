from collections import defaultdict

def sparse(data):
    sparse_lst = []
    for i, blk in enumerate(data):
        if i % 2 == 0:
            id = i // 2
            
            sparse_lst = sparse_lst + [id] * blk
        else:
            sparse_lst = sparse_lst + ['.'] * blk
            
    return sparse_lst

def condense(sparse_lst):    
    l = 0
    r = len(sparse_lst) - 1

    while l < r:
                
        if sparse_lst[l] != '.':
            l += 1

        if sparse_lst[r] == '.':
            r -= 1

        if sparse_lst[l] == '.' and sparse_lst[r] != '.':
            
            sparse_lst[l] = sparse_lst[r]
            sparse_lst[r] = '.'
            l += 1
            r -= 1
        
    return sparse_lst


def checksum(disk_map):
    count = 0
    for i, id in enumerate(disk_map):
        if id != '.':
            count += i * id

    return count


def defrag(sparse_lst):
    openings = []    # list of openings 
    file_blocks = []    # list of file blocks 
    l = 0
    r = 1

    while r < len(sparse_lst):
        
        if sparse_lst[l] == sparse_lst[r]:
            r += 1
        else:
            if all(item == "." for item in sparse_lst[l:r]):
                openings.append(( len(sparse_lst[l:r]), l)) # (size of space block, index of space block)
                # print(sparse_lst[l:r])
            elif all(item != "." for item in sparse_lst[l:r]):
                file_blocks.append((sparse_lst[l], len(sparse_lst[l:r]), l)) # (id, size of space block, index of space block)
                # print(sparse_lst[l:r])
            l = r
        
        
    if l < len(sparse_lst):
        if all(item == "." for item in sparse_lst[l:r]):
            openings.append((len(sparse_lst[l:r]), l))
            # print(sparse_lst[l:r])
        
        elif all(item != "." for item in sparse_lst[l:r]):
            file_blocks.append((sparse_lst[l], len(sparse_lst[l:r]), l))    
            # print(sparse_lst[l:r])


    for file in reversed(file_blocks):
        id, length, index = file
        for i, (freespace, free_index) in enumerate(openings):
            if free_index > index:
                break
            # print(i, (freespace, free_index))
            if length <= freespace:
                sparse_lst[index:index + length] = ['.'] * length
                sparse_lst[free_index:free_index + length] = [id] * length
                if freespace - length != 0:
                    freespace = freespace - length
                    free_index = free_index + length
                    openings[i] = (freespace, free_index)
                else:
                    openings.pop(i)
                
                break
    

    return sparse_lst
  


def main(data):
    sparse_lst = sparse(data)
    # print(sparse_lst)
    # disk_map = condense(sparse_lst) # part 1
    disk_map = defrag(sparse_lst) # part 2
    return checksum(disk_map)
    

if __name__ == "__main__":
    # path = r"C:\AOC\2024\day_09\test_data.txt" 
    path = r"C:\AOC\2024\day_09\data.txt" 

    with open(path, "r") as f:
        data = [int(x) for x in f.read()]
    
    ans = main(data)
    print(f"Checksum: {ans}")
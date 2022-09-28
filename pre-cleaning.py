"""
Early data cleaning for CS287 proj 1. Goal here is to get a general look at what the data looks like
"""
NUM_FILES = 1431
found_strings = set()


#removes number from end of string, also strip whitespace
def stripNum(line: str) -> str:
    for i in range(len(line)):
        if line[i] in nums:
            return line[:i].strip()
    
    #no num found, return line
    return line.strip()

for i in range(NUM_FILES):
    # create file name
    file_name = f'./reports/{i:06d}.dat'
    
    #open file
    with open(file_name) as curr:
        # strip lines by new line
        lines = curr.read().split('\n')
        
        # filter lines

        #first only keep lines with multi space
        lines = filter(lambda line: "  " in line, lines)

        # now remove ERROR MODE
        lines = filter(lambda line: "ERROR MODE" not in line, lines)

        #now remove the numbers, we are only looking for the unique error types, also strip whitespace
        lines = [stripNum(line) for line in lines]

        
        if len(lines) == 0:
            print(f'No lines found for {file_name}')
        
        #convert to a set, union with found_strings
        lines = set(lines)

        found_strings = found_strings.union(lines)


#now write to a new file

with open("unique_lines.txt", "w+") as f:
    for line in found_strings:
        f.write(f'{line}\n')
        


print(found_strings, len(found_strings))
input_list = []
file = 'Adv24Input.txt'
with open(file,'r') as f:
    for row in f.readlines():
        input_list.append(row.strip())

##input_list = ['0/2','2/2','2/3','3/4','3/5','0/1','10/1','9/10']
mapped_list = [list(map(int,row.split("/"))) for row in input_list]

def recurse(parts,last_part):
    mxscore = 0
    mxparts = []
    for i,part in enumerate(parts):
        match = (part[0] == last_part or part[1] == last_part)
        if match:
            non_match_part = part[1] if part[0]==last_part else part[0]
            remainder = part + recurse(parts[:i] + parts[i+1:],non_match_part)
            if sum(remainder) > mxscore:
                mxscore = sum(remainder)
                mxparts = remainder
    return mxparts

def recurse_part_two(parts,last_part):
    mxscore = 0
    mxparts = []
    mxlen = 0
    mxpartslen = []
    for i,part in enumerate(parts):
        match = (part[0] == last_part or part[1] == last_part)
        if match:
            non_match_part = part[1] if part[0]==last_part else part[0]
            remainder, remainder_ln = recurse_part_two(parts[:i] + parts[i+1:],non_match_part)
            remainder = part + remainder
            remainder_ln = part + remainder_ln
            if sum(remainder) > mxscore:
                mxscore = sum(remainder)
                mxparts = remainder
            if len(remainder_ln) > mxlen:
                mxlen = len(remainder_ln)
                mxpartslen = remainder_ln
            elif len(remainder_ln) == mxlen:
                if sum(remainder_ln) > sum(mxpartslen):
                    mxlen = len(remainder_ln)
                    mxpartslen = remainder_ln
    return mxparts, mxpartslen

##part_one = recurse(mapped_list,0)
part_one, part_two = recurse_part_two(mapped_list,0)

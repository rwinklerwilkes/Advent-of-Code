import math, csv

##Day Two
def calc_chksum(matrix):
    cksum = 0
    for row in matrix:
        min_val = None
        max_val = None
        for cell in row:
            if not min_val or cell < min_val:
                min_val = cell
            if not max_val or cell > max_val:
                max_val = cell
        cksum += max_val-min_val
    return cksum

def calc_mod_chksum(matrix):
    cksum = 0
    for row in matrix:
        check = sorted(row,reverse=True)
        for i in range(len(check)):
            for j in range(i+1,len(check)):
                if check[i] % check[j] == 0:
                    cksum += math.floor(check[i]/check[j])
    return cksum
    
file = "Cksum Input.txt"
file_in = []
fi = [[5,1,9,5],[7,5,3],[2,4,6,8]]
fi2 = [[5,9,2,8],[9,4,7,3],[3,8,6,5]]
with open(file, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        file_in.append([int(i) for i in row])

part_one = calc_chksum(file_in)
part_two = calc_mod_chksum(file_in)

x, y, z, n = int(input()), int(input()), int(input()), int(input())

print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1)])


#finding substring -ex 2

def count_substring(string, substring):
    return (sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))


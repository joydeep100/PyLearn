def check_pairs(ar):
    l = len(ar)
    uniq_ele = set(ar)

    p_count=0
    for i in uniq_ele:
        count=0;
        for j in ar:
            if j==i:
                count+=1
        if count//2>=1:
            p_count+=(count//2)        

    return(p_count)

def check_pairs_wo_sets(ar):
    l = len(ar)
    dict = {}

    for i in range(l):
        count=1
        if ar[i] in dict.keys():    #made mistake to define i here instead of ar[i]
            continue
        for j in range(i+1,l):
            if ar[j]==ar[i]:
                count+=1
        if count//2>=1:
            s=ar[i]
            dict[s]=count//2

    p_count=0
    for i in dict.values():
        p_count+=i;

    return(p_count)  

ar=[1,2,1,2,1,1,1,1,1,9,9,1,2]

print(check_pairs(ar))
print(check_pairs_wo_sets(ar))
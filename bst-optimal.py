data = [0.05, 0.4, 0.08, 0.04, .1, .1, .23]

def optimal_BST(data,s,e, o={}):
    if len(data) == 1:
        o[(s,e)] = data[0]
        return data[0]
    
    elif len(data) == 0:
        o[(s,e)] = 0
        return 0
    
    else:
        m = 0
        for i in range(data):
            if i == len(data) - 1:
                l = data[:i]
                su = sum(l)
                
                lo = optimal_BST(l,s,i,o)
                o[(s,i)] = lo
                
                po =  lo + su + data[i]
                
            else: 
                l = data[:i]
                r = data[i+1:]
                su = sum(l) + sum(r)
                
                if (s,i) not in o:
                    lo = optimal_BST(l,s,i,o)
                    o[(s,i)] = lo
                else:
                    lo = o[(s,i)]
                
                if (i,e) not in o:
                    ro = optimal_BST(r,i,e,o)
                    o[(i,e)] = ro
                else:
                    ro = o[(i,e)]
                
                po = lo + ro + su + data[i]   
            
            if po > m:
                m = po

        return m
    
optimal_BST(data, 0, len(data))
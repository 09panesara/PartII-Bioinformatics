import numpy as np

def nussinov_mat(s):
    delta = {'A': {'A': 0, 'C': 0, 'G': 0, 'U': 1}, 'C': {'A': 0, 'C': 0, 'G': 1, 'U': 0},
             'G': {'A': 0, 'C': 1, 'G': 0, 'U': 0}, 'U': {'A': 1, 'C': 0, 'G': 0, 'U': 0}}
    s = [c for c in s]
    n = len(s)
    mat = np.zeros((n,n))

    # # intialise
    # for i in range(n):
    #     mat[i,i] = 0
    #     mat[i,i-1] = 0

    for col in range(1,n):
        j = col
        i = 0
        while (j<n):
            delta_ij = delta[s[i]][s[j]]
            gamma_ij = max(max(mat[i,j-1], mat[i+1,j-1] + delta_ij), mat[i+1,j])
            for k in range(i+1,j):
                gamma_ij = max(gamma_ij, mat[i,k]+mat[k+1,j])
            mat[i][j] = gamma_ij
            i+=1
            j+=1

    return mat

rna = 'GGUCCAC'
res = nussinov_mat(rna)
print(res)

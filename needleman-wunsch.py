from Bio.SubsMat import MatrixInfo
import numpy as np

class NeedlemanWunsch:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def needleman_wunsch(self, gap_penalty, match_mismatch_scores):
        str1 = self.str1
        str2 = self.str2

        m = len(str1) + 1 # +1 for space at start of string, str1 goes along side (rows)
        n = len(str2) + 1 # str2 goes along top (columns)

        # initialisation of alignment matrix
        algnmnt_mtx = np.zeros((m,n), dtype=int)
        for i in range(m):
            algnmnt_mtx[i][0] = gap_penalty * i

        for j in range(n):
            algnmnt_mtx[0][j] = gap_penalty * j

        # initialisation of pointer matrix
        ptr_mtx = np.zeros((m,n), dtype=object)

        for i in range(1, m):
            for j in range(1, n):
                v1 = algnmnt_mtx[i-1][j]+gap_penalty
                v2 = algnmnt_mtx[i][j-1]+gap_penalty
                scr = match_mismatch_scores.get((str1[i-1], str2[j-1]))
                if scr == None:
                    scr = match_mismatch_scores.get((str2[j-1], str1[i-1]))
                v3 = algnmnt_mtx[i-1][j-1] + scr # diagonal
                ptr_val = max(v1, v2, v3)
                algnmnt_mtx[i][j] = ptr_val
                if ptr_val == v1:
                    ptr_mtx[i][j] = 'UP'
                elif ptr_val == v2:
                    ptr_mtx[i][j] = 'LEFT'
                else:
                    ptr_mtx[i][j] = 'DIAG'

        print (np.matrix(algnmnt_mtx))
        print (np.matrix(ptr_mtx))

nw = NeedlemanWunsch('AGTTCA', 'ACCGTT')
nw.needleman_wunsch(-1, MatrixInfo.blosum50)
# The alphabet product

# I have four positive integers, A, B, C and D, where A < B < C < D. The input is a list of the 
# integers A, B, C, D, AxB, BxC, CxD, DxA in some order. Your task is to return the value of D.

# ------------------------------Solution------------------------------

def alphabet(ns):
    ns = sorted(ns)
    return ns[7] // ns[2 if ns[2] != ns[0] * ns[1] else 3]
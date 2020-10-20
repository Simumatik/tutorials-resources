if initialize:
    L1_out = [0, 0, 0]
    L2_out = [0, 0, 0]
    L3_out = [0, 0, 0]
else:
    if (x1[0] - x0[0]) > 20:
        L1_out = L1_in
        L2_out = L2_in
        L3_out = L3_in
    else:
        L1_out = [0, 0, 0]
        L2_out = [0, 0, 0]
        L3_out = [0, 0, 0]
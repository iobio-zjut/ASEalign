# -*- coding: utf-8 -*-

import os
import time

begintime = time.time()
tdbPath = "/share/home/zhanglab/xxy/LF/MMthreader/pdb_20/tdb_eig/"
codePath = "/share/home/zhanglab/xxy/LF/MMthreader/pdb_20/strsum_eigen_1"
with open("/share/home/zhanglab/xxy/LF/MMthreader/pdb_20/cluster_20", "r") as f:
    for i in f:
        str = i.split()[0]
        os.system(
            codePath+" /share/home/zhanglab/public/databases/pdb_2020-08/" + str + ".pdb " +
            "/share/home/zhanglab/xxy/LF/MMthreader/pdb_20/dssp/" + str + ".dssp " +
            tdbPath + str + ".tdb " +
            tdbPath + str + ".eig")

endtime = time.time()
run_time = endtime - begintime
print('该循环程序运行时间：',run_time)
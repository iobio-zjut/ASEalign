# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 19:36:34 2015

@author: chaofn
"""
import os

"""
这个程序的目的是将linux下/ifs/home/fanchao/Manesh_pdb目录中的所有文件（一共有215个文件）
批处理
将pdb文件生成dssp文件

"""
#listdir返回文件名的列表
g=open("/share/home/zhanglab/xxy/LF/MMthreader/pdb_20/cluster_56805","r")
for line0 in g:
    str0=line0.split()[0]
    print(str0)
  

    input_file="/share/home/zhanglab/public/databases/pdb_2020-08/"+str0+".pdb"
    output_file="/share/home/zhanglab/xxy/LF/MMthreader/pdb_20/dssp/"+str0+".dssp"
    os.system('/share/home/zhanglab/xxy/environment/anaconda/bin/dssp -i %s -o %s' %(input_file,output_file))
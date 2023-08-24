# -*- coding: utf-8 -*-
'''
@Time    : 2021/11/10 22:01
@Author  : yossie
@File    : run_template70.py
'''
import os
import time

import os
import time
import sys

type = sys.argv[1]
NAME_Path = sys.argv[2]
rootPath = "/share/home/zhanglab/xxy/LF/MMthreader/test1/test_" + type + "_140/"
basicPath = "/share/home/zhanglab/xxy/meta_contact/test_291/database/"#数据路径
srcPath = '/share/home/zhanglab/xxy/Threader/Engerthread/file_basic/'#脚本路径
def run_blast(name):#序列比对，寻找大于等于30%的序列
    os.chdir(rootPath)
    os.system("mkdir " + "./" + name)
    os.chdir("/share/home/zhanglab/xxy/Threader/Engerthread/ncbi-blast-2.10.1+/bin")
    os.system("./blastp -query " + basicPath + "Fasta/" + name + ".fasta" +
              " -out " + rootPath + name + "/" + name + "_30.blast -db ./makeblastdb_pdb_afdb_rename/makeblastdb -outfmt 6 -evalue 1e-5 -num_threads 5")


def run_choose30(name):#该函数的作用是根据BLAST比对结果，筛选出与查询序列相似度大于等于30%的同源序列，并将其命名保存在rootPath+name/name_Name_holomogy.txt文件中。
    blastPath = rootPath + name + "/" + name + "_30.blast"
    namePath = rootPath + name + "/" + name + "_Name_holomogy.txt"
    os.system("touch " + namePath)
    with open(blastPath, "r") as fastaFile:
        for nowline in fastaFile.readlines():
            if (float(nowline[14:21]) > 30.0):
                a = nowline[7:13]
                # print(a)
                with open(namePath, "a+") as WriteFile:
                    WriteFile.write(a + "\n")


def run_delete(name):#该函数的作用是根据前面的筛选结果，从PDB70数据库中删除同源序列，将剩余的非同源序列保存在rootPath+name/name_Name_noholomogy.txt文件中。
    namePath = rootPath + name + "/" + name + "_Name_holomogy.txt"
    reasultPath = rootPath + name + "/" + name + "_Name_noholomogy.txt"
    PDB70namePath = "/share/home/zhanglab/xxy/LF/MMthreader/cluster_56805"

    os.system("touch " + reasultPath)
    with open(namePath, "r") as nameFile:
        delete = set()
        for line1 in nameFile.readlines():
            delete.add(line1.strip())
        write = open(reasultPath, 'a')
        with open(PDB70namePath, 'r') as ff:
            for line1 in ff.readlines():
                if line1.strip() not in delete:
                    write.write(line1)
        write.close()


def run_namelist(name):#根据前面筛选出的非同源序列名，生成一个包含这些序列名的文本文件，保存在rootPath+name/name_NameLong.txt中。
    g = open(rootPath + name + "/" + name + "_Name_noholomogy.txt", "r")
    for line0 in g:
        str0 = line0.split()[0]
        str1 = "/share/home/zhanglab/xxy/Threader/Engerthread/database/AFDB_20W/tdb_eig_" + type + '/ '
        str = str1 + str0
        k = open(rootPath + name + "/" + name + "_NameLong.txt", "a+")
        k.writelines(str + "\n")

def run_exe(name):
    reasultName = "reasults_" + type
    begintime = time.time()
    # contactName = "metaContact"
    line2 = '/share/home/zhanglab/xxy/meta_contact/test_291/MMthreader/code/eigenthreader_src/src_xxy/eigenthreader_'+type + " -m" + name + " -c9 -C0 -t20 -z1250 " + " -F" + \
            basicPath + "ss2/" + name + ".ss2 " + \
            basicPath + "Fasta/" + name + ".fasta " + \
            basicPath + "contact08/" + name + ".txt " + \
            rootPath + name + "/" + reasultName + "/sort.txt " + \
            rootPath + name + "/" + name + "_NameLong.txt"
    print(line2)
    os.system("mkdir " + rootPath + name + "/" + reasultName)
    os.chdir(rootPath + name + "/" + reasultName)
    os.system(line2)
    endtime = time.time()
    run_time = endtime - begintime
    k = open(rootPath + "run_time.txt", "a+")
    k.writelines(name + "\t" + str(run_time) + "\n")
    print('runtime:', run_time)


if __name__ == '__main__':
    with open(NAME_Path, "r")as ff:
        for line in ff.readlines():
            # print(line.strip())
            testName = line.strip()
            run_blast(testName)
            run_choose30(testName)
            run_delete(testName)
            run_namelist(testName)
            run_exe(testName)

# encoding: utf-8
import os
fastanamePath = "/share/home/zhanglab/xxy/LF/MMthreader/list1.txt"
contactName = "reasults_self_0.3"
rootPath = "/share/home/zhanglab/xxy/LF/MMthreader/test1/test_self_0.3_140/"
def get_TMscoreresults(line1):
    sort_path = '/share/home/zhanglab/xxy/LF/MMthreader/test1/test_self_0.3_140/' + line1 + '/reasults_self_0.3/sort.txt'
    list = []
    with open(sort_path, 'r')as sortFile:
        num = 1
        for line in sortFile.readlines():
            line = line.strip()
            line = line[-6:]  # get name
            list.append(line)  # list === 10name
            num += 1
            if (num > 10):
                break
    tem_list = []
    tem_list.append(line1)
    for i in list:
        file_dir = rootPath + line1 + "/" + contactName +'/'+ line1 + "_" + i + '.model.pdb'
        na2 = "/share/home/zhanglab/xxy/Threader/Engerthread/TMalign /share/home/zhanglab/public/databases/pdb_2020-08/" + line1 + ".pdb " + file_dir + " > " + rootPath + line1 + "/TMscoreresults"
        os.system(na2)
        g = open(rootPath + line1 + "/TMscoreresults", "r")
        n = 0
        for line2 in g:
            n = n + 1
            if n == 14:
                TMscore1 = line2.split("(")[0]
                TMscore2 = TMscore1.split()[1]
                TMscore = TMscore2
                tem_list.append(TMscore)
                os.system("rm " + rootPath + line1 + "/TMscoreresults")
    with open(rootPath + "/TMsocre_" + contactName + "_1.txt", "a") as ff:
        for i in tem_list:
            if len(i) == 7:
                ff.write("%s\t" % i)
            else:
                ff.write("%s\n")
                ff.write("%s\t" % i)
if __name__ == '__main__':
    f = open(fastanamePath, "r")
    for line0 in f:
        a = line0.split()[0]
        get_TMscoreresults(a)

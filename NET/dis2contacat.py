import numpy as np
import scipy.signal as signal
# 读取距离文件，计算距离和并保存到文件
with open('distance.txt') as f, open('profile.txt', "w") as outfile:
    for line in f:
        lineDist_comma = []
        res = line.split()[0]
        res1 = res.split(',')[0]
        res2 = res.split(',')[1]
        lineDist = line.split()[1:]
        lineDist = list(map(float, lineDist))
        dist_sum = sum(lineDist[1:13])
        outfile.write(str(res1) + '\t' + str(res2) + '\t' + str(dist_sum)+ '\n')
# 读取 profile.txt 文件，按距离大小排序并保存到 contact.txt 文件中
contact_path = 'profile.txt'
contact2_path = 'contact.txt'
all_data = []
res_pair = []
with open(contact_path, 'r', encoding='utf-8') as dd:
    lines = dd.readlines()
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):  # 忽略空行和注释行
            continue
        line = line.split()
        if len(line) != 3:  # 数据格式不正确
            print(f"数据格式错误：{line}")
            continue
        x, y, z = line[0], line[1], float(line[2])
        res_pair.append(x)
        res_pair.append(y)
        res_pair.append(z)
        all_data.append(res_pair)
        res_pair = []
    all_data = sorted(all_data, key=lambda x: x[2], reverse=True)
with open(contact2_path, 'a+', encoding='utf-8') as yy:
    for i in all_data:
        if float(i[0]) < float(i[1]):
            yy.write(f"{i[0]} {i[1]} 0 8 {i[2]}\n")

## NET:

Purpose: Given an input sequence, the purpose is to predict the contacts between amino acids in the protein.

```bash
sh pathreader.sh #inputfold  outputfold
#1.run msa_search.sh 
#msa_make.sh
#2.run delete_greater.py 
#3.run predict_cpu.py
#Generation distance.txt
#run dis2contact.py
#Convert the distance.txt file to the contact.txt file as required.
python dis2contact.py
```

## Template detection section：

```bash
#get dssp
1.run_dssp0.py
#get tdb,eig
2.run_eig02.py

#3.run test_MMthreader.py
python  /share/home/zhanglab/xxy/LF/MMthreader/test_MMthreader.py self_0.3 /share/home/zhanglab/xxy/LF/MMthreader/list1.txt

#4use TMscore
run_top10_TM.py
```


#!/bin/sh
#设置运行环境
module load anaconda
source activate pytorch
echo $2"=-=-=-=-=-=-=-= begin =-=-=-=-=-=-=-="
cd $2
mkdir predict_dist

echo "=={=======> Predict distance =={=======>"
distance="$2/distance.txt"
if [ ! -s $distance ]; then
	cd $1/Predict_dist/msa_search
	sh msa_search.sh $1 $2
	
	echo "Round 0: 01  Predict distance"
	cp $1/Predict_dist/delete_greater.py $2/predict_dist
	cd $2/predict_dist
	python delete_greater.py $1

	cd $1/Predict_dist/zfjwoT
	python predict_cpu.py $2/predict_dist/msa2.a3m $2/predict_dist $2/predict_dist/ran64.a3m $2/distance.txt
else
	echo "Round 0: 01  'distance.txt' already exit ..."
fi

conda deactivate 
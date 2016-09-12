python generate_final4.py 0.0
cd ..
t=`python parser.py 7 | tail -n 5`
echo $t" "$i >> out
cd scripts/

python generate_final4.py 0.05
cd ..
t=`python parser.py 7 | tail -n 5`
echo $t" "$i >> out
cd scripts/


for i in `seq 10 5 60`; do
	python generate_final4.py 0.$i
	cd ..
	t=`python parser.py 7 | tail -n 5`
	echo $t" "$i >> out
	cd scripts/
done
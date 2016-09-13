python generate_final3.py 0.0 
cd ..
t=`python parser.py 6 | tail -n 6`
echo $t" "0
cd scripts/

echo ""
python generate_final3.py 0.05 
cd ..
t=`python parser.py 6 | tail -n 6`
echo $t" "5
cd scripts/


for i in `seq 10 5 80`; do
	echo ""
	python generate_final3.py 0.$i 
	cd ..
	t=`python parser.py 6 | tail -n 6`
	echo $t" "$i
	cd scripts/
done
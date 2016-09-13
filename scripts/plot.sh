# python t.py 0.0 
# cd ..
# t=`python parser.py 6 | tail -n 6`
# echo $t" "0
# cd scripts/

echo ""
python t.py 0.95
cd ..
t=`python parser.py 7 | tail -n 6`
echo $t" "5
cd scripts/


for i in `seq 90 -5 20`; do
	echo ""
	python t.py 0.$i 
	cd ..
	t=`python parser.py 7 | tail -n 6`
	echo $t" "$i
	cd scripts/
done
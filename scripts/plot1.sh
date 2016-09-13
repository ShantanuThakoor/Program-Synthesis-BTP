for i in `seq 1 1 10`; do
	python generate_final41.py 0.4 0.6 
	cd ..
	t=`python parser.py 71 | tail -n 6`
	echo $t
	echo ""
	cd scripts/
done;
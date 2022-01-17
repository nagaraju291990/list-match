input=$1
list_file=$2
output=$3


#echo $input

mkdir $output -p

for file in $input/*
do
  f=$(basename "$file")
  echo "Running $f"
  #python3 t1_t2_t3_match_and_replace.py $file $list_file > "$3/$f".out
  python3 t1_t2_t3_match_and_replace-xls.py $file $list_file > "$3/$f".out
done

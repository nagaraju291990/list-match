input=$1
list_file=$2
output=$3


#echo $input

mkdir $output -p

for file in $input/*
do
  f=$(basename "$file")
  echo "Running $f"
  python3 accr_match_replace.py $list_file $file  > "$3/$f".out
done

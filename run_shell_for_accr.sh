input=$1
list_file=$2
output=$3


#echo $input

mkdir $output -p

for file in $input/*
do
  f=$(basename "$file")
  echo "Running $f"
  python3 accr_match_and_replace.py $file $list_file > "$3/$f".out
done

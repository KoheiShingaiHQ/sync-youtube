mkdir -p 'output'
mkdir -p 'storage'

if [ $# -ne 2 ]; then
  echo "Usage: $ sh diff.sh {YouTube Video 1} {YouTube Video 2}" 1>&2
  exit 1
fi

id1=$1
id2=$2

python3 cnt_wav.py $id1 $id2 &&
python3 diff_wav.py $id1 $id2 &&
Rscript peak.R $id1 &&
Rscript peak.R $id2 &&
python3 peak_wav.py $id1
#rm -rf ./storage/$id*

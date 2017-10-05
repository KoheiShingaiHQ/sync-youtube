mkdir -p 'output'
mkdir -p 'storage'

if [ $# -ne 1 ]; then
  echo "Usage: $ sh waveform.sh {YouTube Video ID}" 1>&2
  exit 1
fi

id=$1

python youtubedl.py $id &&
python mp3_to_wav.py $id &&
python plot_wav.py $id ||
python3 edge_wav.py $id &&
rm -rf ./storage/$id*


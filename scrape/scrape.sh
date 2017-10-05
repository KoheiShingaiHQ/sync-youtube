mkdir -p 'output'
mkdir -p 'storage'

if [ $# -ne 1 ]; then
  echo "Usage: $ sh scrape.sh {Target URL}" 1>&2
  exit 1
fi

url=$1
hash=`echo -n $url | shasum -a 256`

npm start -- $url ${hash:0:6} | sed -e '1,4d' > ./storage/${hash:0:6}.json &&
# python detect_lang.py ${hash:0:6} &&
python3 edge.py ${hash:0:6} &&
python3 diff.py ${hash:0:6}
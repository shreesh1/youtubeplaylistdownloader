python3 links.py $1 | grep -o 'watch.*' | cut -d '&' -f 1 | sed 's/^/https:\/\/www.youtube.com\//'

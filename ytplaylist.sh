python3 links.py | grep -o 'watch.*' | cut -d '&' -f 1 | sed 's/^/https:\/\/www.youtube.com\//'

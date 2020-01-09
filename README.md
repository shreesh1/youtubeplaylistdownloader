# youtubeplaylistdownloader
--------------------------------------------------------------------
***Currently only for linux users***
command to extract the list

python3 links.py | grep -o 'watch.*' | cut -d '&' -f 1 | sed 's/^/https:\/\/www.youtube.com\//'

put this command in bash and run the line a list of links would come out


--------------------------------------------------------------------

Requirements:
bs4:pip3 install bs4


-------------------------------------------------------------------

languages used:
python
bash

-------------------------------------------------------------------

downloading coming soon

-------------------------------------------------------------------

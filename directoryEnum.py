import requests 
import sys 

#Wordlist.txt in current directory. COuld also be chaged to argument
sub_list = open("wordlist.txt").read() 
directories = sub_list.splitlines()

# domain passed in as argument
for dir in directories:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html" 
    r = requests.get(dir_enum)
    if r.status_code==404: 
        #print(f'404 at {dir}')
        pass
    else:
        print("Valid directory:" ,dir_enum)
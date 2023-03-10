import random

lower_case='abcdefghijklmnopqrstuvwxyz'
upper_case='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers="0123456789"
symbols='!@#$%^&*?/'

use_for=lower_case+upper_case+numbers+symbols
#adsffd
length_pass=8
password="".join(random.sample(use_for,length_pass)) 
print('your password generated=',password)

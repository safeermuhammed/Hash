
"""This program will calculate the hashes of all the files in the specific directory"""


import subprocess
#import hashlib
cmd =input("Enter the command : ")
trial = subprocess.run(["powershell","-Command",cmd])
#Pwoershell command : Get-FileHash -Algorithm MD5 -Path (Get-ChildItem "filepath\*.*" -Recurse -force)

import hashlib as priyank
from pyscript import document

    
def sha1_converter(event):      
    pwd = document.getElementById('sha1_input').value
    alex = priyank.sha3_512(pwd.encode('utf-8'))
    priya = alex.digest()
    print(priya)
    output_div = document.getElementById('sha1_output')
    output_div.innerText = priya
    
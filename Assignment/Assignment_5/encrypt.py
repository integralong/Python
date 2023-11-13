#Lauren Song
#U79789182
#Encrypting text

encrypt_code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
                'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
                'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
                'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
                'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
                'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
                'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
                'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
                'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
                '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
                '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
                '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
                ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
                "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
                '{':'[','[':'{','}':']',']':'}'}


def encrypt_contents(text):
    encrypted_text = ""
    for char in text:
        if char.isspace():
            encrypted_text += char
        elif char in encrypt_code:
            encrypted_text += encrypt_code[char]
        else:
            encrypted_text += char
            
    return encrypted_text

input_file_name = input('Enter the name of file (in .txt format):')
with open(input_file_name, 'r') as input_file:
    text = input_file.read()

    encrypted_contents = encrypt_contents(text)

output_file_name = input('Enter the name of encrypted file:')

with open(output_file_name, 'w') as output_file:
    output_file.write(encrypted_contents)



print(f'{output_file_name} is encrypted!')

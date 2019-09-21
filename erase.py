with open('htmltags.txt','r') as file:
    text = file.read()

print(text.replace('1','').replace('(','').replace(',','').replace(')','').replace('\'','').replace(' ',''))

file.close()

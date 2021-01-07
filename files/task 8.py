def write_to(filename,text):
    file1 = open(filename,'w')
    file1.write(text)

write_to('text.txt','hellow!')
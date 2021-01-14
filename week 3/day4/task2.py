mails = ['hello sophie how are you',
         'hello pls help me!!!',
         'Sophie, production is dows go to work!!!',
         'sophie, i need your help',
         'SOS!!! come to work pls',
         'good night, Sophie',
         'SALES!Lining lala',
         'Nikes China Buy right now',
         'HeLP Sophie',
         'Hey sophie how are you',
         'Please come with me'
         ]
def filter(mail_list:list):
    for sentence in mail_list:
        sentence = sentence.lower()
        if 'help' in sentence or 'sos' in sentence or 'urgent' in sentence or sentence.endswith('!!!'):
            f1 = open('spam.txt','a')
            f1.write(sentence +'\n')
        elif sentence.startswith('sales') or 'buy right now' in sentence:
            f1 = open('spam.txt','a')
            f1.write(sentence + '\n')
        else:
            f2 = open('mails.txt','a')
            f2.write(sentence +'\n')
filter(mails)

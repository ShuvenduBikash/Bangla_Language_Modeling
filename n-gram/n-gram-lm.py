import re
import codecs

bigram = {}
trigram = {}
            
with codecs.open('D:\\SD14\\data\\CrawledSentences\\BanglaPedia\\a.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        sentences = line[:-1].split('।')
        for sentence in sentences:
            sentence = re.sub("[' ']+", " ", sentence)    
            if sentence[0] == ' ':
                sentence = sentence[1:]
                
            words = re.findall('[\\u0980-\\u09E0]+', sentence) 
            if len(words)<3:
                continue
            
            for i in range(len(words)-1):
                key = words[i]+" "+words[i+1]
                if key in bigram:
                    bigram[key]+=1
                else:
                    bigram[key]=1
                    
                # trigram
                if i<len(words)-2:
                    key = words[i]+" "+words[i+1]+" "+words[i+2]
                    if key in trigram:
                        trigram[key]+=1
                    else:
                        trigram[key]=1
                
     
with codecs.open('bigram.txt', mode='w', encoding='utf-8') as f:
    for key in bigram.keys():
        f.write(key+" "+str(bigram[key])+'\n')
        
with codecs.open('trigram.txt', mode='w', encoding='utf-8') as f:
    for key in trigram.keys():
        f.write(key+" "+str(trigram[key])+'\n')
        
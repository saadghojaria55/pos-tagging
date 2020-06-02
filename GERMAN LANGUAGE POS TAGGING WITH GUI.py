import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import ne_chunk, pos_tag
from tkinter import *
from tkinter import Label,Entry,Button,Frame
from tkinter import messagebox

###########FRAME INITIALIZATIONS#####################
root=Tk()
root.geometry("600x300")
root.title("GERMAN TAGGING")
Tops=Frame(root, width=1600)
Tops.pack(side=TOP)
f1=Frame(root,width=600,height=300,padx=40,pady=40)
f1.pack(side=LEFT,fill=Y,expand=True)

qtvar = StringVar(root)
qtvar.set(0)
qtvar1 = StringVar(root)
qtvar1.set("")
tag=StringVar()
noun=StringVar()
verb=StringVar()
chunk=StringVar()
###########################################################
####################GUI PART ##############################
L1=Label(f1, text="Enter German Sentence",font=('times',20,'bold'),padx=10,pady=10).grid(row = 5, column =0)
txt=Entry(f1, font=('times',16,'bold'),textvariable=qtvar1,relief='solid').grid(row=6,column=0)

L3=Label(f1, font=('arial', 16, 'bold'),bd=10,anchor="w",fg="dark green",textvariable=tag).grid(row=9, column=0)
#noun=Label(f1, text="Nouns are:",font=('times',20,'bold'),padx=10,pady=10).grid(row = 11, column =0)
L4=Label(f1, font=('arial', 16, 'bold'),bd=10,anchor="w",fg="dark green",textvariable=noun).grid(row=10, column=0)
#verb=Label(f1, text="Verbs are:",font=('times',20,'bold'),padx=10,pady=10).grid(row = 11, column =0)
L5=Label(f1, font=('arial', 16, 'bold'),bd=10,anchor="w",fg="dark green",textvariable=verb).grid(row=11, column=0)
#chuncked=Label(f1, text="Chuncked Sentence:",font=('times',20,'bold'),padx=10,pady=10).grid(row = 12, column =0)
L6=Label(f1, font=('arial', 16, 'bold'),bd=10,anchor="w",fg="dark green",textvariable=chunk).grid(row=12, column=0)

################FUNCTIONS#####################################


def done():
     root.destroy()



#Sentence Splitting
def convert():
    global text
    text=(qtvar1.get())
    sentences = sent_tokenize(text, language='german')
    for i, s in enumerate(sentences):
        print(i+1, '-->', s)
    	
    #POS Tagging
    
    def pos2string(tagged): return ' '.join(['/'.join(p) for p in tagged])
    
    for i, s in enumerate(sentences):
        tagged = nltk.pos_tag(word_tokenize(s, language='german'))
        tagged=pos2string(tagged)
        print(tagged)
        tag.set("Tagged sentence is:"+tagged)
    	
    def pos_filter(tagged, type = 'NN'): return [x[0] for x in tagged if x[1].startswith(type)]
    
    print('Nouns:')
    for i, s in enumerate(sentences):
        l1=pos_filter(nltk.pos_tag(word_tokenize(s, language='german')), 'NN')
        l1=' '.join(l1)
        #print(i+1, '-->', pos_filter(nltk.pos_tag(word_tokenize(s, language='german')), 'NN'))
    print(l1)
    noun.set(l1)
    print('Verbs:')
    for i, s in enumerate(sentences):
        l2=pos_filter(nltk.pos_tag(word_tokenize(s, language='german')), 'VB')
        
    print(l2)
    verb.set(l2)	
    #NER
    
    def ner_tag(chunked): return [c[0]+'/0' if type(c) == tuple else c.leaves()[0][0]+'/'+c.label() for c in chunked]
    
    for i, s in enumerate(sentences):
        chunked = ne_chunk(pos_tag(word_tokenize(s, language='german')))
        l3=ner_tag(chunked)
        #print(i+1, '-->', ' '.join(ner_tag(chunked)))
        l3=' '.join((l3))
        print(l3)
        chunk.set(l3)
#################BUTTONS######################################
btnAdd=Button(f1,bd=5,fg="black",font=('times',10,'bold'),width=5,text="Convert",bg="white",command=convert,padx=4,pady=4,state='active')
btnAdd.grid(row=7,column=0)   
btnExit=Button(f1,bd=5,fg="black",font=('times',10,'bold'),width=5,text="Done",bg="white",command=done,padx=4,pady=4).grid(row=7,column=1)

##############################################################

    
root.mainloop()
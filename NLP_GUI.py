### main components :
## Tkinter gui framework , sentiment analysis , pos tagging 

import tkinter as tk
from tkinter import * 
from tkinter import ttk 
import tkinter.filedialog
from tkinter.scrolledtext import *


### NLP packages
import textblob

from textblob import TextBlob
from textblob import *
# import spacy
# nlp = spacy.load('en')



window = Tk()
window.title('NLP GUI')
window.geometry("800x600")


# ## label
# lable11 = Label(window,text = "NLP_GUI")
# lable11.grid(row = 0, column =1)

## Tab layout

tab_top = ttk.Notebook(window)
tab1 = ttk.Frame(tab_top)
tab2 = ttk.Frame(tab_top)
tab3 = ttk.Frame(tab_top)



### add tab to notebook

tab_top.add(tab1,text = "NLP Analysis")
tab_top.add(tab2,text = "File Processing")
tab_top.add(tab3,text = "About")

tab_top.pack(expand = 1, fill = "both")

### tab for NLP Analysis

lablel1 = Label(tab1, text = "NLP Analysis", padx = 5, pady = 5)
lablel1.grid(column = 0, row = 0)

### tab for File processing
lablel2 = Label(tab2, text = "File processing", padx = 5, pady = 5)
lablel2.grid(column = 0, row = 0)

### tab for about
lablel3 = Label(tab3, text = "About author", padx = 5, pady = 5)
lablel3.grid(column = 0, row = 0)

#### Functions defined for each button clicked

### textblob has all inbuilt functions for tokenizing , pos tags , sentiment scoring


def get_tokens():
	raw_text = str(raw_entry.get())
	text = TextBlob(raw_text)
	text_tokens = text.words
	result = " \n Tokens : {}".format(text_tokens)
	## diaply for tab1
	tab1_display.insert(tk.END, result)

def get_pos_tags():
	raw_text = str(raw_entry.get())
	text = TextBlob(raw_text)
	text_pos_tags = text.tags
	result = "\nPOS TAGGING:{}".format(text_pos_tags)
	tab1_display.insert(tk.END, result)


def get_sentiment_score():
	raw_text = str(raw_entry.get())
	new_text = TextBlob(raw_text)
	text_sent = "subjectivity , polarity :{}".format(new_text.sentiment)
	#result = "\n Sentiment scores : {}".format(text_sent.sentiment)
	tab1_display.insert(tk.END, text_sent)

# def get_entities():
# 	raw_text = str(raw_entry.get())
# 	text = nlp(raw_text)
# 	text_entity = [(ent.text, ent.label_) for ent in text.ents]
# 	result = "\n Entities : {}".format(text_entity)
# 	tab1_display.insert(tk.END, result)

def clear_reset():
	entry1.delete(0, END)

def clear_result():
	tab1_display.delete('1.0', END)





### main NLP code
l1 = Label(tab1, text = "Enter text for Analysis")
l1.grid(row=1, column = 0)

raw_entry = StringVar()
entry1 = Entry(tab1, textvariable = raw_entry , width =50)
entry1.grid(column = 2, row = 1)

## buttons for NLP tab 
btn1 = Button(tab1 , text = "Tokenizer", width = 12 , bg = '#03A9F4', fg = '#FFF' , command = get_tokens)
btn1.grid(row = 4, column = 0, padx = 10, pady = 10)

btn2 = Button(tab1 , text = "POS TAG", width = 12 , bg = '#03A9F4', fg = '#FFF',command =get_pos_tags)
btn2.grid(row = 4, column = 1, padx = 10, pady = 10)

btn3 = Button(tab1 , text = "Sentiment", width = 12 , bg = '#03A9F4', fg = '#FFF', command =get_sentiment_score)
btn3.grid(row = 4, column = 2, padx = 10, pady = 10)

# btn4 = Button(tab1 , text = "Entities", width = 12 , bg = '#03A9F4', fg = '#FFF', command=get_entities)
# btn4.grid(row = 5, column = 0, padx = 10, pady = 10)

btn5 = Button(tab1 , text = "Reset", width = 12 , bg = '#03A9F4', fg = '#FFF', command =clear_reset)
btn5.grid(row = 5, column = 1, padx = 10, pady = 10)

btn6 = Button(tab1 , text = "Clear All", width = 12 , bg = '#03A9F4', fg = '#FFF', command =clear_result)
btn6.grid(row = 5, column = 2, padx = 10, pady = 10)


### display screen/window for showing results based on tab selection

tab1_display = ScrolledText(tab1, height = 10)
tab1_display.grid(row = 7, column = 0, columnspan = 3, padx = 5, pady = 5)


### file reading tab

### functions for open files
def open_file():
	file1 = tk.filedialog.askopenfilename(filetypes = (("Text Files",".txt"),("All Files", "*")))
	read_text = open(file1).read()
	display_file.insert(tk.END, read_text)

def get_file_tokens():
	raw_text = display_file.get('1.0', tk.END)
	text = TextBlob(raw_text)
	text_tokens = text.words
	result = " \n Tokens : {}".format(text_tokens)
	## display for tab2
	tab2_display_text.insert(tk.END, result)

def get_file_pos_tags():
	raw_text = display_file.get('1.0', tk.END)
	text = TextBlob(raw_text)
	text_pos_tags = text.tags
	result = "\nPOS TAGGING:{}".format(text_pos_tags)
	tab2_display_text.insert(tk.END, result)

def get_file_sentiment_score():
	raw_text = display_file.get('1.0', tk.END)
	new_text = TextBlob(raw_text)
	text_sent = "subjectivity , polarity :{}".format(new_text.sentiment)
	#result = "\n Sentiment scores : {}".format(text_sent.sentiment)
	tab2_display_text.insert(tk.END, text_sent)

def clear_text_file():
	display_file.delete('1.0', END)

def clear_display_result():
	tab2_display_text.delete('1.0', END)


l2 = Label(tab2, text = "Open file for Processing")
l1.grid(row=1, column = 1)

### display for file open
display_file = ScrolledText(tab2, height = 10)
display_file.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 3)

### button for file open tab 
b0 = Button(tab2 , text = "Open File", width = 12 , bg = '#03A9F4', fg = '#FFF', command =open_file)
b0.grid(row = 3, column = 0, padx = 10, pady = 10)


# b1 = Button(tab2 , text = "NLP Analysis", width = 12 , bg = '#03A9F4', fg = '#FFF', command =nlp_analysis)
# b1.grid(row = 3, column = 0, padx = 10, pady = 10)

b2 = Button(tab2 , text = "Tokenizer", width = 12 , bg = '#03A9F4', fg = '#FFF', command =get_file_tokens)
b2.grid(row = 3, column = 1, padx = 10, pady = 10)

b3 = Button(tab2 , text = "POS TAG", width = 12 , bg = '#03A9F4', fg = '#FFF', command =get_file_pos_tags)
b3.grid(row = 3, column = 2, padx = 10, pady = 10)

b4 = Button(tab2 , text = "SentimentAnalysis", width = 12 , bg = '#03A9F4', fg = '#FFF', command =get_file_sentiment_score)
b4.grid(row = 4, column = 0, padx = 10, pady = 10)

b5 = Button(tab2 , text = "Reset", width = 12 , bg = '#03A9F4', fg = '#FFF', command =clear_text_file)
b5.grid(row = 4, column = 1, padx = 10, pady = 10)

b6 = Button(tab2 , text = "CLear All", width = 12 , bg = '#03A9F4', fg = '#FFF', command =clear_display_result)
b6.grid(row = 4, column = 2, padx = 10, pady = 10)

# b7 = Button(tab2 , text = "Open File", width = 12 , bg = '#03A9F4', fg = '#FFF', command =open_file)
# b7.grid(row = 3, column = 0, padx = 10, pady = 10)



### display results for tab2 
tab2_display_text = ScrolledText(tab2, height = 10)
tab2_display_text.grid(row = 7, column = 0,columnspan=3, padx = 5, pady=5)
tab2_display_text.config(state=NORMAL)




### about tab

about_lablel = Label(tab3, text = " AUTHOR : SUNIL JOSHI , NLP GUI V.0.0.1 \n ", padx = 5, pady = 5)

about_lablel.grid(column = 0, row=1)



window.mainloop()




































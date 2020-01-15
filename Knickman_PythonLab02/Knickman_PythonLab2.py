#!/usr/bin/env python
# coding: utf-8

# In[5]:


def celsius_to_fahrenheit(param_float):                                                                       
    return param_float * 1.8 + 32.0

print("Convert Celsius to Fahrenheit.")
cel_float = float(input("Enter a Celsius temp:"))
fah_float = celsius_to_fahrenheit(cel_float)
print(cel_float," degrees Celsius converts to ",fah_float," degrees Fahrenheit")


# In[7]:


def are_anagrams(word1, word2):
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)
    return word1_sorted == word2_sorted

print("Anagram Test")
two_words = input("Enter two space-separated words: ")
word1, word2 = two_words.split()

if are_anagrams(word1,word2):
    print("The words are anagrams.")
else:
    print("The words are NOT anagrams.")


# In[15]:


def make_word_list(a_file):
    word_list = []
    for line_str in a_file:
        line_list = line_str.split()
        for word in line_list:
            if word != "--":
                word_list.append(word)
    return word_list

def make_unique(word_list):
    unique_list = []
    
    for word in word_list:
        if word not in unique_list:
            unique_list.append(word)
            
    return unique_list

gba_file = open("gettysburg.txt","r")
speech_list = make_word_list(gba_file)

print(speech_list)
print("Speech Length: ", len(speech_list))
print("Unique Length: ", len(make_unique(speech_list)))


# In[28]:


def reverse_doc(file):
    doc_elems = []
    for line_str in file:
        line_list = line_str.split()
        for word in line_list:
            if word != "--":
                doc_elems.append(word)
    doc_elems
    
    rev_elems = []
    
    for elem in doc_elems:
        rev_elems.append(elem[::-1])
        
    rev_elems
    rev_doc = " ".join(rev_elems)
    return rev_doc

speech_file = open("gettysburg.txt","r")
print(reverse_doc(speech_file))


# In[ ]:





from nltk_data.corpora import words
from collections import Counter
#import numpy as np

#from nltk.corpus import english_words

#define public variables
#input letters
#shortened english word list (ppwl)

#ew = english_words
#ew = corpora.words('en')
#w = words.words('en')


#print("fine" in words)

#############################################################
### THESE DONT NEED TO BE CALLED AGAIN
#############################################################
def splithalves():
    with open('sorted_by_length.txt') as i:
        #with_newlines = i.readlines()
        arr = i.readlines()

    




    arr4 = []
    arr8 = []
    for j in range(len(arr)):
        if len(arr[j])>=9:
            arr8.append(arr[j])
        else:
            arr4.append(arr[j])

    print()
    print("a4 lem", len(arr4))
    print("a4 0", arr4[0])
    print("a4 1", arr4[1])
    print("a4 2", arr4[len(arr4)-1])

    print()
    print("a8 lem", len(arr8))
    print("a8 0", arr8[0])
    print("a8 1", arr8[1])
    print("a8 2", arr8[len(arr4)-1])

    with open('sorted_4.txt', 'w') as f:
        f.writelines(arr4)

    with open('sorted_8.txt', 'w') as g:
        g.writelines(arr8)


def sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = len(array[0])
        for x in array:
            if len(x) < pivot:
                less.append(x)
            elif len(x) == pivot:
                equal.append(x)
            elif len(x) > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)
    else:
        return array


def prePreProc():

    print("in prepreproc")
    #only do this once

    with open('en') as i:
        arr = i.readlines()

    print()
    new_list=sort(arr)

    print()
    print("new list lem", len(new_list))
    print("new list 0", new_list[0])
    print("new list 1", new_list[1])
    print("new list 2", new_list[len(new_list)-1])

    with open('sorted.txt', 'w') as f:
        f.writelines(new_list)

    """
    for i in range(len(new_list)):
        if len(new_list[i]) < 4:

            print(i, new_list[i])
            new_list.remove(i)
    """


    return new_list


def preProc():
    with open('sorted_8.txt') as i:
        arr = i.readlines()
    
    #remove words with 8 distinct letters

    """
    only need to do words w len > 7
    split list before

    len(8+):

    """
    print()
    print("arr[len]", len(arr))

    new_arr = []
    bad_arr = []
    n = 1
    print("arr", arr[n])
    q = set(arr[n])
    print("q", q)
    print("len q", len(q))
    

    for j in range(len(arr)):
        s = set(arr[j])

        if len(s) <= 8: # if set has less than 8 dis letters, aka valid
            new_arr.append(arr[j])
        else:
            bad_arr.append(arr[j])


    print("new arr",len(new_arr))
    #print("new arr", new_arr[:30])
    #print("new arr 0 ", new_arr[0])
    #print("bad arr", bad_arr[:30])
    #print("bad arr 0 ", bad_arr[0])

    with open('sorted_4.txt') as m:
        front = m.readlines()
    #
    full_list = front + new_arr
    #
    with open('sorted_asc.txt', 'w') as m:
        m.writelines(full_list)


def sortdesc():
    print("sortdesc")
    #"""
    with open('sorted_asc.txt') as i:
        arr = i.readlines()

    print("len arr",len(arr))
    print("arr0",arr[0])
    arr.sort(key=len, reverse=True)
    print("toret0", arr[0])
    
    #print("toret", to_ret)
    print("toret len", len(arr))

    with open('sorted_desc.txt', 'w') as m:
        m.writelines(arr)
    #"""
#############################################################
#############################################################

def trimCenterLetter(char):
    print("trimming")
    print()
    with open('sorted_asc.txt') as i:
        arr = i.readlines()

    trimmed = []
    for j in range(len(arr)):
        if char in arr[j]:
            trimmed.append(arr[j])

    print()
    print("trimmed length", len(trimmed))
    print()
    with open('trimmed.txt', 'w') as k:
        k.writelines(trimmed)
    

def solver(letters):
    print("in solver")
    """
    with open('trimmed.txt') as i:
        toarr = i.readlines()
    """
    #with open('sorted_asc.txt') as i:
    #    toarr = i.readlines()
    #"""

    word_file = open("trimmed.txt", "r")

    toarr = []
    for word in word_file:
            toarr.append(str(word).lower()[:-1])

    # 1. turn trimmed into vvvv
    #[[len=4][len=5][len=6][len=7][len=8]...]
    # or reverse order?
    # within that alphabetical
    """
    arr = [[]]
    k = len(toarr[0])
    for j in range(len(toarr)):
        if len(toarr[j]) > k:#some condition where you need to add a [] to arr [[abcd, defg], []]
            arr.append([])
            k = len(toarr[j])
        else:
            k = len(toarr[j])

        #print("n", n)
        arr[k-5].append(toarr[j])
    """
    print()
    #print("len arr", len(arr))
    #print("arr[n]", arr[len(arr)-1])

    #for k in range(len(arr)):
    #    print(k+4, arr[k][0])

    # 2. math
    #say we have an alphabetical list with same number of letters
    # arr[0] has len4, arr[1] len5, etc. 
    #for k in len(arr)
    # if arr[k][0] in letters
    #    newarr.append(arr[0][k])
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z']
    
    unacceptable_letters = [l for l in alphabet if l not in letters]
    acceptable_words = []
    
    for word in toarr:
        if letters[0] in word:
            if word not in acceptable_words:
                if len(word) > 3:
                    if any(l in unacceptable_letters for l in word) == False:
                        acceptable_words.append(word)

    #for each char/while sttill going
    #   all len 4s, then put into new arr
    #   all len 5s then put into new arr

    #for each char/while still going
    #   for each different len, checkarr then put into new arr
    

    #print("words", acceptable_words)

    return acceptable_words
    #for each char/while still going
    #   all len 4s, then put into new arr
    #   all len 5s then put into new arr


def cleanInput(letters):
    print()
    print("in procinput", letters)
    print()
    clean = []
    for i in letters:
        if i.strip():
            clean.append(i)
        
    print("clean_list", clean)
    return clean
    

def cleanOutput(wordlist):
    #list currently low to high
    wordlist.sort(key=len, reverse=True)
    print()
    print()
    for i in range(len(wordlist)):
        print(wordlist[i])



def main():

    #"""
    print("main:")
    #1. prepreprocess corpus
    #2. clean input letter list
    #3. isolate first letter as center
    #4. go through corpus again
    #5. then the tricky part

    ######################

    #1. prepreprocess corpus
    #   - already done

    # 2. clean input
    print()
    arr = list(input("input letters, center first: "))
    print()
    
    print("input: ",arr)
    print()

    cleaninput = cleanInput(arr)
    print("cleaned list: ",cleaninput)
    

    # 3/4. go through corpus again with center letter

    trimCenterLetter(cleaninput[0])
    #or#
    #centerletterlist = []
    #   preproc(cleaniinput[0])


    # 5. solve

    solvedList = solver(cleaninput)
    #solver(cleaninput)

    
    print("printMe: ", len(solvedList))


    cleanOutput(solvedList)

    #"""
    
###############################

#print("pre-preprocessingCorpus")
#corpus = prePreProc()

#splithalves()
#preProc()
#sortdesc()

###############################
if __name__ == "__main__":
    main()
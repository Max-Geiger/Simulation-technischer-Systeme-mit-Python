import numpy as np

def WordCount(TxtFile, key=False):
    '''
    WordProcess.WordCount(file, key=False)
    Returns a sorted list of a string and, optional, its sort key.
    
    Parameters
    ----------
    TxtFile : string
        Path to a text file for the word analysis
    key : Bool, optional
        Array containing the word frequency in descending order. The default is False.

    Returns
    -------
	sorted_list : ndarray
    	Array of words in their descending frequency
	key : ndarray
		Array of word frequency in descending order
    '''
    # load the stop word list from StopWords.txt
    with open('/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/Probeklausur 22/StopWords.txt', 'r',  encoding='utf-8') as file:
        stopWords = file.read().replace('\n', ' ')
    # make stopword list
    stopWords=stopWords.split(' ')
    
    # load the text 
    with open(TxtFile, 'r',  encoding='utf-8') as file:
        data = file.read()
    # change all charkter to low
    data=data.lower()
    # cleen the text for better processing
    data=data.replace('–', ' ')
    data=data.replace('{', '')
    data=data.replace('}', '')
    data=data.replace('.', ' ')
    data=data.replace('\n', ' ')
    data=data.replace(',', ' ')
    data=data.replace(';', '')
    data=data.replace(':', ' ')
    data=data.replace('-', ' ')
    data=data.replace('–', ' ')
    data=data.replace('– ', ' ')
    data=data.replace('_', ' ')
    data=data.replace('>>', ' ')   
    data=data.replace('<<', ' ')
    # make a wordlist from the cleaned text
    data=data.split(' ')
    # remove the stop words from the wordlist
    clearData = sorted([x for x in data if x not in stopWords])
    # sort and count the words in the wordlist
    Udat,count=np.unique(clearData, return_counts=True)
    #AllData=(np.append([Udat],[count],axis=0))
    # sort the word list according to its frequency
    Skey=sorted(range(len(count)), key=lambda k: count[k])[::-1]
    # return the sorted words and its frequency 
    if key:
        return Udat[np.array(Skey)], np.sort(count)[::-1]
    else:
        return Udat[np.array(Skey)]


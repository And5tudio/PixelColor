import os
def Trans_list_of_words(mot,separator=' '):
    words = mot
    listOfString=list(words)
    newList=[]
    newWord=''
    string = ''
    for i in range(len(listOfString)):
        # print(str(i))
        string=str(listOfString[i])
        if string == separator :
  #  print(str(newWord))
            newList.append(newWord)
  #  print(str(newList))
   
            newWord = ''
        else:
        #  print(str(string))
            newWord =newWord+ string
            if i+1 == len(listOfString):
    # print(str(newWord))

                newList.append(newWord)
   
    # print(str(newList))
                newWord = ''
  
    return newList

if __name__ == '__main__':

    file =  open('config','r')

    mot = file.read()

    print(str(Trans_list_of_words(mot)))

    file.close()
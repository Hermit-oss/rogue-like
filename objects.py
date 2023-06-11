import pygame
import shutil
import os
import random
import pandas as pd
from collections import Counter

def genre_objects(filename, fileCopy):
    shutil.copyfile(filename, fileCopy)  #kopiujemy mape

############################ Losujemy ile przedmiotow
    def weighted_random_amount():
        r = random.randint(1, 10)
        if r <= 1:
            return 1    
        elif 1 < r <= 3:
            return 2   
        elif 3 < r <= 6:
            return 3   
        elif 6 < r <= 9:
            return 4    
        else:
            return 5
    result_amount=0
    result_amount_counter= Counter(weighted_random_amount() for _ in range(1)).keys()
    for i in result_amount_counter:
        result_amount=i


########################## Losujemy typ przedmiotu
    def weighted_random_object():
        r = random.randint(1, 10)
        if r <= 3:
            return 1
        elif 3 < r <= 5:
            return 2
        else:
            return 3

    results_type_counter = Counter(weighted_random_object() for _ in range(result_amount))


##################### Wrzucamy typy na liste
    keys=results_type_counter.keys()
    values=results_type_counter.values()

    object_list=[]
    list_tmp=[]
    list_tmp2=[]
    for j in keys:    
        list_tmp.append(j)

    for k in values:   
        list_tmp2.append(k)

    object_list.append(list_tmp)
    object_list.append(list_tmp2)

########################## Edytowanie pliku csv 
    csv_map = pd.read_csv(fileCopy)
    column_count=len(csv_map)
    row_count = sum(1 for row in csv_map)

    value=[]
    for i in object_list[0]:
        if(i==1):
            value.append(3)
        if(i==2):
            value.append(4)
        if(i==3):
            value.append(5)

    index=0
    while (result_amount>0):


        for j in range(object_list[1][index]):
            while True:
                try:
                    row_index=(random.randint(3,row_count-3))   #losujemy w ktorym rzedzie i kolumnie chcemy cos umiescic
                    column_index=(random.randint(2,column_count-3))

                    if(((csv_map.iloc[row_index][column_index-1]==1 and csv_map.iloc[row_index-1][column_index]==1 and #czy chociaz jedno pole 
                    csv_map.iloc[row_index][column_index+1]==1) and csv_map.iloc[row_index+1][column_index]==1) #obok przedmiotu to 1 lub 2
                    and csv_map.iloc[row_index][column_index]==1):                                            #oraz czy umieszczamy na polu z wartoscia 1
        
                        csv_map.iloc[row_index][column_index]=value[index]
                        csv_map.to_csv(fileCopy, index=False)

                        break
                except:
                    pass

        result_amount=result_amount-object_list[1][index]
        index+=1

################# Usuwamy skopiowany plik ale chyba nie jest to niezbedne bo za kazdym razem
def remove_file():
    file = './assets/map/map1.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("file deleted")
    else:
        print("file not found")
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:56:13 2020

@author: SEBASTIAO NG
"""


import numpy as tableau

nb_lignes = int(input("entre le nombre de lignes = "))
nb_Colonnes = int(input("\nentre le nombre de colonnes = "))

#methode pourgenerer valeurs aléatoires
def nb_aleatoire(nb_lignes,nb_Colonnes):
    
    valeurs =tableau.random.randint(nb_lignes, size=(nb_lignes,nb_Colonnes))
    tableau.savetxt("fichierTXT.txt", valeurs,fmt='%i')
    
#methode pour creer fichier txt sans trier les valeurs
def Aff_fichierTXT():
    fichier = open("fichierTXT.txt", "r")
    lines = fichier.readlines()
    fichier.close() #fermer le fichier
    print("\n\nTABLEAU DE VALEURS À TRIER\n\n")
    for line in lines:
        print(line.strip()) # affichier le tableau sur la console python
        
  
      
#***********TRI PAR INSERTION****************************
#methode tri par insertion
def insertionSort(alist):
    
    for i in range(1,len(alist)):
        current = alist[i] #liste courant
        while i>0 and alist[i-1]>current:
            alist[i] = alist[i-1]
            i = i-1
            alist[i] = current
    return alist


def insertion_file_txt():
    data = tableau.loadtxt('fichierTXT.txt')
    for i in range(0,nb_Colonnes):
        read_data =data[:,i]             
        insertionSort(read_data)
    fichier_trié=open('tri_Insertion.txt','w')
    tableau.savetxt('tri_Insertion.txt', data, fmt='%i')
    fichier_trié.close()


#*************TRI PAR MARGESORT**********************************
def mergeSort(aliste):
    #print(aliste) # pour verifier les tri étape par étape
    if len(aliste)>1:
        mid = len(aliste)//2

        lefthalf = aliste[:mid]  #left list
        righthalf = aliste[mid:] #rigth list
        mergeSort(lefthalf) #Call mergeSort function
        mergeSort(righthalf)# Call mergeSort function
        
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            #comparer le first item of listes
            if lefthalf[i] < righthalf[j]: 
                aliste[k]=lefthalf[i]
                i +=1
            else:
                aliste[k]=righthalf[j]
                j+=1
            k=k+1
        while i < len(lefthalf):
            aliste[k]=lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            aliste[k]=righthalf[j]
            j+=1
            k+=1
            

def mergeSort_file_txt():
    data = tableau.loadtxt('fichierTXT.txt')
    for i in range(0,nb_Colonnes):
        read_data =data[:,i]             
        mergeSort(read_data)
    fichier_trié=open('tri_mergeSort.txt','w')
    tableau.savetxt('tri_mergeSort.txt', data, fmt='%i')
    fichier_trié.close()
    
    
#**********QUICKSORT************************************
def quicksort(aliste,gauche, droite):
     
     #pivot ---> calcule la mediane
     pivot = aliste[(gauche+droite)//2]
     i = gauche
     j = droite
     while True:
         while aliste[i]<pivot:
             i+=1
         while aliste[j]>pivot:
             j-=1
         if i>j:
             break
         if i<j:
             (aliste[i], aliste[j]) = (aliste[j],aliste[i])
         i+=1
         j-=1
     if gauche<j:
         quicksort(aliste,gauche,j)
     if i<droite:
         quicksort(aliste,i,droite)
         

#methode pour creer le ficheroù sont trié les données
def QuickSort_file_txt():
    data = tableau.loadtxt('fichierTXT.txt')
    for i in range(0,nb_Colonnes):
        read_data=data[:,i]      
        gauche=0
        droite=len(read_data)-1
        quicksort(read_data,gauche,droite)
    fichier_trié=open('tri_QuickSort.txt','w')
    tableau.savetxt('tri_QuickSort.txt', data, fmt='%i')
    fichier_trié.close()
    

#*************************************************
#METHODE PRINCIPALE
if __name__ == "__main__":
    nb_aleatoire(nb_lignes,nb_Colonnes)
    Aff_fichierTXT()
    insertion_file_txt()
    mergeSort_file_txt()
    QuickSort_file_txt()
# First part CSV and how to handle csv in our class 
# comma separated value  ( C S V )
# so the comma that separate each value in our csv file is caled delemiter hh ma3ndi mandir b had m3loma wlkn mouhim 

# first thing we import the csv bibl


import csv 
# to open a file we use the context manager which is 

with open('data.csv', 'r') as csv_file:
    #to read this file we use the reader method 
    csv_reader = csv.reader(csv_file)
    # to print the content of the csv file 
    #if we just writed print(csv_reader ) it will just print the object memory 
    next(csv_reader)
    #ila bghina n7ydo dik field li fiha achno anl9aw f les valeurs o nprintiw hir les valeur bi3ibara okhra awl str n7ydo tandir next 
    for line in csv_reader:
        print(line)
        #we can also print the value 3la hsab index matalan ana bghit n afficher hir les emails andir 
        print(line[2])

# how to write in a csv file 
# bghina nchdo nfs values li f had file ndirohom f file jdid wlkn blast comma andiro dashes 
        
    # 7lina l original file r y3ni read mode 
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # creena had variable csv reader o drna reader methode bach n9raw dak original file 

        # mn wraha 7lina wahd file jdid  w writer mode 
        with open('new_file.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file , delimiter= '\t')        
            # o creena wahd variable csv writer odrna writer methode bach nktbo fhad new file + bdlna delimiter kan virgule rdinah dash   also la bghina ndiro tabs blast dash andi \t


            # mn wraha wahd loop dial each line f csv reader
            for line in csv_reader :
                # ghadi nwritiw f had new file kola line mn original file 
                csv_writer.writerow(line)


# new part ga3 hadchi li drna how l common way to work with csv wlkn kayn mahsn li howa  dict reader o dict writer , hit blast manb9aw nhddo fieds taywliw homa l keys wst dictionnaire m3a values dialhom tayshal 3lina nl9aw info bzrba
                

    with open('data.csv', 'r') as csv_file:
    #to read this file we use the reader method 
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            #blast manhddo index tandiro l keys o haka hsn 
            print(line['email'])



# bnisba l dict writer taykhsna nhddo fields :
        with open('data.csv', 'r') as csv_file:
            
            csv_reader = csv.DictReader(csv_file)

            with open('new_dict.csv', 'w') as new_dict:
                fieldnames = ['first_name' , 'last_name ' , 'email']
                # hna hddna l fields 
                csv_writer = csv.DictWriter(new_dict,fieldnames=fieldnames ,delimiter='\t')
                # ila bghinahom ibano homa lwlin f header
                
                csv_writer.writeheader()


                for line in csv_reader:
                    csv_writer.writerow(line)
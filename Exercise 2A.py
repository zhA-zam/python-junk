# read the rainfall.txt then write out a new file called rainfall.txt
# the data should be grouped on the total annual rainfall field into the 
# categories: [60-70], [71-80], [81,90], [91-]
import os.path

def main():

    endofprogram = False
    try:
        InputFileName = input('Enter name of input file: ')
        infile = open(InputFileName,'r')
        OutputFileName = input('Enter name of output file: ')
        # determine wether name exists
        while True:
            if os.path.isfile(OutputFileName):
                OutputFileName = input('File Exists. Enter name again: ')
            else:
                outfile = open(OutputFileName,'w')
                break
    except IOError:
        print("Error opening file - End of program")
        endofprogram = True

        #If there is not exception, start reading the input file
        #Write the same data in formated form in new file.
    if endofprogram == False:
        cat_60 = []
        cat_71 = []
        cat_81 = []
        cat_91 = []
        for line in infile:
            city, rain = line.split(' ')
            rain = float(rain)

            if 60 <= rain < 70:            
                cat_60.append((city, rain)) # Storing a tuple in the list
            elif 70 <= rain < 80:
                cat_71.append((city, rain))  
            elif 80 <= rain < 90:
                cat_81.append((city, rain))
            elif 90 <= rain :
                cat_91.append((city, rain))

        outfile.write("[60-70]"+'\n')
        for i in range(len(cat_60)):
            city = cat_60[i][0]
            rain = cat_60[i][1]
            outfile.write('%+25s'%(city)+'%5.1f'%(rain)+'\n')

        outfile.write("[70-80]"+'\n')
        for i in range(len(cat_71)):
            city = cat_71[i][0]
            rain = cat_71[i][1]                
            outfile.write('%+25s'%(city)+'%5.1f'%(rain)+'\n')

        outfile.write("[80-90]"+'\n')
        for i in range(len(cat_81)):
            city = cat_81[i][0]
            rain = cat_81[i][1]
            outfile.write('%+25s'%(city)+'%5.1f'%(rain)+'\n')

        outfile.write("[91-]"+'\n')
        for i in range(len(cat_91)):
            city = cat_91[i][0]
            rain = cat_91[i][1]
            outfile.write('%+25s'%(city)+'%5.1f'%(rain)+'\n')
main()
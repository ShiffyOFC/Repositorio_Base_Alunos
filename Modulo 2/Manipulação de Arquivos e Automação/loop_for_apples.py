import csv

applesFile=open('apples.csv')
applesReader=csv.reader(applesFile)

for row_and_down in applesReader:
    print('Row #' + str(applesReader.line_num) + ' ' + str(row_and_down))
#                       número por linha      elemento da linha
import csv


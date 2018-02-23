def pattern(numOfRows, midPoint):
    row=0 
    element = 1
    numOfColumns = 0
    indentDec = midPoint
    indentInc = 0
    indentRow = 0

    while row < numOfRows:
        rowList = []
        if row < midPoint:
            # number of columns increases till mid point 
            numOfColumns = 2*row + 1 
            # indentation is for alignment of digits 
            indentDec -=1
            indentRow = indentDec
        else:
            # number of columns decrease after mid point
            numOfColumns = numOfColumns - 2  
            indentInc +=1
            indentRow = indentInc

        col = 0
        while col < numOfColumns:
            rowList.append(element)
            col +=1
            element += 1

        #print the row  
        def printRow(rowList):
            tempString = ''
            for i in range(0,len(rowList)):
                tempString += str(rowList[i]) + ' '
            return tempString      
          
        print(indentRow * '  ' + printRow(rowList))
        row += 1

# only odd number of rows can print this pattern. 

numOfRows = int(input("enter an ODD number as the number of rows: "))

midPoint = (numOfRows + 1)/2

pattern(numOfRows, midPoint)

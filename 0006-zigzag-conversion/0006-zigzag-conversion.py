class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rowArray = [""] * numRows
        
        rowIndex = 1
        goingDown = True
        
        for currentChar in s:
            rowArray[rowIndex-1] += currentChar
            
            if rowIndex == numRows:
                goingDown = False
            
            elif rowIndex == 1:
                goingDown = True
            
            if goingDown:
                rowIndex += 1
            else:
                rowIndex -= 1
            
        return "".join(rowArray)
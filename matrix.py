#!/usr/bin/env python3

#Filename: matrix.py
# Author - Prathamesh Pawar 
# Email  - prathameshpawar1301@gmail.com

"""Description of the Class is below"""

#############################################################################################
##  Matrix Class -  supporting meathods
##                  initialize - given row and columns
##                  insert     - insert at given index
##                  addScaler  - add given scaler value to the matrix
##                  mulScaler  - multiply given scaler value with the matrix
##                  printMtx   - print given matrix
#############################################################################################

class Matrix:
    

    def __init__(self, *args):
        """__init__(*args) --> initializes matrix object with given parameters(rows and columns)
        Parameters:
        arg0: (if  only 1 arg is given then rows and columns) number of rows
        arg1: number of columns
        """
        numargs = len(args)

        if numargs < 1:
            raise TypeError(f'Epected at least one argument, got {numargs}')
        elif numargs == 1:
            print(f'Created square matrix {numargs}x{numarags}')
            self._rows    = args[0]
            self._columns = args[0]
        elif numargs == 2:
            self._rows    = args[0]
            self._columns = args[1]
        else:
            raise TypeError(f'At most 2 arguments ara permitted, but got{numargs}')
        self.initMatrix(0)
            
    def initMatrix(self, val:int)->int:
        """initMatrix(val:int)--> initializes nxm matrix to given value
        Parameters:
        val: value to initialize matrix with 
        """
        self._matrix = [[val for x in range(self._columns)] for y in range(self._rows)]
        return self._matrix

    def changeElements(self, **kwargs):
        """changeElements(rw_chng= int, cl_chng = int, val_chng = int) --> changas single value if row and
        column are given or, Either changes entire row or entire column
        Parameters:
        rw_chng = gives row to change
        cl_chng = gives column to change
        val_chng = gives value to change to 
        """
        rw_chng  = None
        cl_chng  = None
        val_chng = None
        
        if 'row' in kwargs:
            rw_chng = kwargs['row']
            if rw_chng != None and rw_chng > self._rows: raise IndexError(f'Row number exceeded beyond matrix bounds')
        if 'col' in kwargs:
            cl_chng = kwargs['col']
            if cl_chng != None and cl_chng > self._columns: raise IndexError(f'Column number exceed beyond matrix bounds')
        if 'val' in kwargs: val_chng = kwargs['val']

        if val_chng  == None: raise TypeError(f'Missing value parameter')
        elif rw_chng == None and cl_chng == None: raise TypeError(f'At least a row or column value required')
        else: print(f'Resultant Matrix')

        if rw_chng == None:
            for i in range(self._rows):
                self._matrix[i][cl_chng-1] = val_chng
        elif cl_chng == None:
            for i in range(self._columns):
                self._matrix[rw_chng-1][i] = val_chng
        else:
            self._matrix[rw_chng-1][cl_chng-1] = val_chng

        return self._matrix


    def scalerMultiplier(self, scal_val):
        """scalerMultiplier(scal_val: int)-->multiplies each element of the matrix by given scalar value
        Paramater:
        scal_val = multiplies entire matrix(each individual value of the matrix) by this value
        """

        if scal_val != None:

            for i in range(self._rows):
                for j in range(self._columns):
                    self._matrix[i][j] *= scal_val

            return self._matrix
        else:
            raise TypeError(f'Need scaler value to multiply')

    def scalerAddition(self, scal_val):
        """scalarAddition(scal_val:int)--> adds given scalar value with each elements of the matrix
        Paramaters:
        scal_val = Adds each value of the matrix by this scalar value
        """

        if scal_val != None and scal_val != 0:

            for i in range(self._rows):
                for j in range(self._columns):
                    self._matrix[i][j] += scal_val

            return self._matrix
        elif scal_val == 0:
            return self._matrix
        else:
            raise TypeError(f'Need scaler value to Add')

    def printMatrix(self):
        """printMatrix()--> prints matrix in matrix form
        No Parameters
        """
        for row in self._matrix:
            print(row)


    def findTranspose(self):
        """findTranspose()--> gives transpose of the current matrix object 
        No Parameters
        """

        tr_matrix = [[self._matrix[j][i] for j in range(len(self._matrix))]for i in range(len(self._matrix[0]))]

        print(f'Transpose is')

        for row in tr_matrix:
            print(row)

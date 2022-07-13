from tkinter import *
import os

class Sudoku:
    def __init__(self, game):
        try:
            for i in range(9):
                for j in range(9):
                    if int(game[i][j]) >= 0 or int(game[i][j]) <= 9:
                        game[i][j] = int(game[i][j])
                    else:
                        raise ValueError("DATOS INCORRECTOS")
        except:
            print("ERROR DE INICIACION")
        self._game = game
        self._solution = []
        
        def getGame(self):
            return self._game
            print(self._game)
            
        def setSolution(self, game):
            self._solution = game
            
        def getNum(self, i, j):
            return(self._game[i][j])
        
        def setNum(self, i, j,n):
            self._game[i][j] = n
            
        def getSolution(self):
            return self._solution
        
        def check(self, line, col, n):
            line = int(line)
            col = int(col)
            if self.getNum(line, col) == n:
                return True
            if self.getNum(line, col) != 0:
                return False
                
            for c in range(0,9):
                if self._game[line][c] == n:
                    return False
            for l in range(0,9):
                if self._game[l][col] == n:
                    return False
                
            lr = int(line/3)
            cr = int(col/3)
            for l in range(lr*3, (lr + l)*3):
                for c in range(cr*3,(cr + l)*3):
                    #if l >= 9 or c >= 9:
                    #      continua
                    if self._game[l][c] == n:
                        #print('l = ','l', 'c = ','c','num = ', self.getNum(l,c), 'n = ', 'n')
                        return False
            return True
        
        def resolve(self,i,j,l):
            if i == 9:
                self.setSolution(self._juego)
                self.write_Solution(self.getSolution())
                return 0
            else:
                for n in range(1, 10):
                    if self.check(i,j,n):
                        t = self.getNum(i,j)
                        self.setNum(i,j,n)
                        if j == 8:
                            self.resolve(i+l, 0)
                        else:
                            self.resolve(i, j + l)
                            self.setNum(i,j,t)
                    
        
            
        
        def write_Solution(self, solution):
            file = open("SudokuTEMP.txt", "w")
            try:
                for i in range(0,9):
                    for j in range(0,9):
                        file.write(str(solution[i][j]))
                        file.write(' ')
                    file.write('\n')
                file.write('\n\n')
                file.close()
            except:
                print('ERROR SAVING THE FILE')
            finally:
                file.close()
                
class Screen:
    def __init__(self, toplevel):
        toplevel.resizable(width = False, height = False)
        toplevel.title("Sudoku Game")
        
        fonte = ('Arial', 18)
        
        self.fr = Frame(toplevel)
        self.fr.bind('<Motion>', self.correct)
        self.fr.pack(ipady = 0, padx = 0)
        
        self.fr1 = Frame(toplevel)
        self.fr1.bind('<Motion>', self.correct)
        self.fr1.pack(ipady = 0, padx = 0)
        
        self.fr2 = Frame(toplevel)
        self.fr2.bind('<Motion>', self.correct)
        self.fr2.pack(ipady = 0, padx = 0)
        
        self.fr3 = Frame(toplevel)
        self.fr3.bind('<Motion>', self.correct)
        self.fr3.pack(ipady = 0, padx = 0)
        
        self.fr4 = Frame(toplevel)
        self.fr4.bind('<Motion>', self.correct)
        self.fr4.pack(ipady = 0, padx = 0)
        
        self.fr5 = Frame(toplevel)
        self.fr5.bind('<Motion>', self.correct)
        self.fr5.pack(ipady = 0, padx = 0)
        
        self.fr6 = Frame(toplevel)
        self.fr6.bind('<Motion>', self.correct)
        self.fr6.pack(ipady = 0, padx = 0)
        
        self.fr7 = Frame(toplevel)
        self.fr7.bind('<Motion>', self.correct)
        self.fr7.pack(ipady = 0, padx = 0)
        
        self.fr8 = Frame(toplevel)
        self.fr8.bind('<Motion>', self.correct)
        self.fr8.pack(ipady = 0, padx = 0)
        
        self.fr9 = Frame(toplevel)
        self.fr9.bind('<Motion>', self.correct)
        self.fr9.pack(ipady = 1, padx = 1)
        
        self._juego = []
        for i in range(1, 10):
            self._juego += [[0,0,0,0,0,0,0,0,0]]
            
        variable = self.fr
        px = 0
        py = 0
        cor = 'white'
        thickness = 0
        for i in range(0,9):
            for j in range(0,9):
                
                if i == 0:
                    variable = self.fr
                if i == 1:
                    variable = self.fr1
                if i == 2:
                    variable = self.fr2
                if i == 3:
                    variable = self.fr3
                if i == 4:
                    variable = self.fr4
                if i == 5:
                    variable = self.fr5
                if i == 6:
                    variable = self.fr6
                if i == 7:
                    variable = self.fr7
                if i == 8:
                    variable = self.fr8
                
                if j%2 == 0 and i%2 == 0:
                    thickness = 1
                
                if j%2 != 0 and i%2 != 0:
                    thickness = 1
                    
                if j in [3,4,5] and i in [0,1,2,6,7,8,]:
                    cor = 'gray'
                elif j not in [3,4,5] and i not in [0,1,2,6,7,8]:
                    cor = 'gray'
                else:
                    cor = 'white'
                    
                self._game[i][j] = Entry(variable, width = 2, font = fonte, bg = cor, cursor = 'arrow', borderwidth = 0, highlightcolor = 'yellow',highlightthickness = 1, highlightbackground = 'black', textvar = jg[i][j])
                self._game[i][j].bind('<Button-1>', self.correct)
                self._game[i][j].bind('<FocusIn>', self.correct)
                self._game[i][j].bind('<Motion>', self.correct)
                self._game[i][j].pack(side = LEFT, padx = px, pady = py)
                
                thickness = 0
                
        self.btn1 = Button(self.fr9, text = 'Save', fg = 'red', font = ('Arial', 11), command = self.save)
        self.btn1.pack(side = RIGHT)
        
        self.btn2 = Button(self.fr9, text = 'Solve', fg = 'blue', font = ('Arial', 11), command = self.solve)
        self.btn2.pack(side = LEFT)
        
        self.btn3 = Button(self.fr9, text = 'Open', fg = 'blue', font = ('Arial', 11), command = self.Open)
        self.btn3.pack(side = LEFT)
        
        self.btn3 = Button(self.fr9, text = 'Reset', fg = 'red', font = ('Arial', 11), command = self.reset)
        self.btn3.pack(side = RIGHT)
        
        self._nombredelsarchivo = "Entrada.txt"
    def solve(self):
        try:
            solucion = Sudoku(self.getGame())
            solucion.resolve(0,0)
            self._nombredelarchivo = "SudokuTEMP.txt"
            self.Open()
            self._nombredelarchivo = "Entrada.txt"
            os.remove("SudokuTEMP.txt")
        except:
            print("ERROR DE LECTURA")
        finally:
            self._numbredelarchivo = "Entrada.txt"
            
    def getGame(self):
        game = []
        for i in range(9):
            game += [[0,0,0,0,0,0,0,0,0]]
        for i in range(9):
            for j in range(9):
                #self._juego[i][j]
                game[i][j] = jg[i][j].get()
                if game[i][j] == '':
                    game[i][j] = 0
        return game
    
    def reset(self):
        for i in range(9):
            for j in range(9):
                jg[i][j].set('')
                
    def save(self):
        file = open("Sudoku.txt", "a")
        try:
            for i in range(9):
                for j in range(9):
                    if self._game[i][j].get() == '':
                        file.write("0")
                    else:
                        file.write(self._game[i][j].get())
                    file.write(' ')
                file.write('\n')
            file.write('\n\n')
            file.close()
        except:
            print("ERROR WHILE WAITING FOR THE FILE")
        finally:
            file.close()
            
    def correct(self, event):
        for i in range(9):
            for j in range(9):
                if jg[i][j].get() == '':
                    continue
                if len(jg[i][j].get()) > 1 or jg[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    jg[i][j].set('')
                    
    def complete(self):
        for i in range(9):
            for j in range(9):
                jg[i][j].set(self._game[i][j])
                
    def Open(self):
        try:
            file = open(self._FileName, 'r')
            
            text = file.readline()
            text = text.split(' ')
            for i in range(0,9):
                for j in range(0,9):
                    if text[0] == '0':
                        jg[i][j].set('')
                    else:
                        jg[i][j].set(text[0])
                    text.pop(0)
                text = file.readline()
                text = text.split(' ')
            file.close()
            
        except:
            print("HAY UN ERROR")
        finally:
            file.close()
            
solution = []
root = Tk()
txt = StringVar(root)
jg = []
for i in range(1, 10):
    jg += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        jg[i][j] = StringVar(root)
        
a = Screen(root)
root.mainloop()
                    
            
                
            
        
                

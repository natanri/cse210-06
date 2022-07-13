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
                        raise ValueError("INCORRECT DATA")
        except:
            print("INITIALIZATION ERROR")
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
            self._juego[i][j] = n
            
        def getSolution(self):
            return self._solution
        
        def verificar(self, linea, col, n):
            linea = int(linea)
            col = int(col)
            if self.getNum(linea, col) == n:
                return True
            if self.getNum(linea, col) != 0:
                return False
                
            for c in range(0,9):
                if self._game[linea][c] == n:
                    return False
            for l in range(0,9):
                if self._game[l][col] == n:
                    return False
                
            lr = int(linea/3)
            cr = int(col/3)
            for l in range(lr*3, (lr + l)*3):
                for c in range(cr*3,(cr + l)*3):
                    #if l >= 9 or c >= 9:
                    #      continua
                    if self._game[l][c] == n:
                        #print('l = ','l', 'c = ','c','num = ', self.getNum(l,c), 'n = ', 'n')
                        return False
            return True
        
        def resolve(self,i,j):
            if i == 9:
                self.setSolution(self._juego)
                self.escribeSolucion(self.getSolution())
                return 0
            else:
                for n in range(1, 10):
                    if self.verificar(i,j,n):
                        t = self.getNum(i,j)
                        self.setNum(i,j,n)
                        if j == 8:
                            self.resolve(i+1, 0)
                        else:
                            self.resolve(i, j + 1)
                            self.setNum(i,j,t)
                    
        
            
        
        def escribeSolucion(self, solution):
            f = open("SudokuTEMP.txt", "w")
            try:
                for i in range(0,9):
                    for j in range(0,9):
                        f.write(str(solution[i][j]))
                        f.write(' ')
                    f.write('\n')
                f.write('\n\n')
                f.close()
            except:
                print('ERROR AL GUARDAR EL ARCHIVO')
            finally:
                f.close()
                
class Janela:
    def __init__(self, toplevel):
        toplevel.resizable(width = False, height = False)
        toplevel.title("Sudoku Game")
        
        fonte = ('Arial', 18)
        
        self.fr = Frame(toplevel)
        self.fr.bind('<Motion>', self.corrige)
        self.fr.pack(ipady = 0, padx = 0)
        
        self.fr1 = Frame(toplevel)
        self.fr1.bind('<Motion>', self.corrige)
        self.fr1.pack(ipady = 0, padx = 0)
        
        self.fr2 = Frame(toplevel)
        self.fr2.bind('<Motion>', self.corrige)
        self.fr2.pack(ipady = 0, padx = 0)
        
        self.fr3 = Frame(toplevel)
        self.fr3.bind('<Motion>', self.corrige)
        self.fr3.pack(ipady = 0, padx = 0)
        
        self.fr4 = Frame(toplevel)
        self.fr4.bind('<Motion>', self.corrige)
        self.fr4.pack(ipady = 0, padx = 0)
        
        self.fr5 = Frame(toplevel)
        self.fr5.bind('<Motion>', self.corrige)
        self.fr5.pack(ipady = 0, padx = 0)
        
        self.fr6 = Frame(toplevel)
        self.fr6.bind('<Motion>', self.corrige)
        self.fr6.pack(ipady = 0, padx = 0)
        
        self.fr7 = Frame(toplevel)
        self.fr7.bind('<Motion>', self.corrige)
        self.fr7.pack(ipady = 0, padx = 0)
        
        self.fr8 = Frame(toplevel)
        self.fr8.bind('<Motion>', self.corrige)
        self.fr8.pack(ipady = 0, padx = 0)
        
        self.fr9 = Frame(toplevel)
        self.fr9.bind('<Motion>', self.corrige)
        self.fr9.pack(ipady = 1, padx = 1)
        
        self._juego = []
        for i in range(1, 10):
            self._juego += [[0,0,0,0,0,0,0,0,0]]
            
        variable = self.fr
        px = 0
        py = 0
        cor = 'white'
        espesura = 0
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
                    espesura = 1
                
                if j%2 != 0 and i%2 != 0:
                    espesura = 1
                    
                if j in [3,4,5] and i in [0,1,2,6,7,8,]:
                    cor = 'gray'
                elif j not in [3,4,5] and i not in [0,1,2,6,7,8]:
                    cor = 'gray'
                else:
                    cor = 'white'
                    
                self._juego[i][j] = Entry(variable, width = 2, font = fonte, bg = cor, cursor = 'arrow', borderwidth = 0, highlightcolor = 'yellow',highlightthickness = 1, highlightbackground = 'black', textvar = jg[i][j])
                self._juego[i][j].bind('<Button-1>', self.corrige)
                self._juego[i][j].bind('<FocusIn>', self.corrige)
                self._juego[i][j].bind('<Motion>', self.corrige)
                self._juego[i][j].pack(side = LEFT, padx = px, pady = py)
                
                espesura = 0
                
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
            solucion = Sudoku(self.getJuego())
            solucion.resolve(0,0)
            self._nombredelarchivo = "SudokuTEMP.txt"
            self.open()
            self._nombredelarchivo = "Entrada.txt"
            os.remove("SudokuTEMP.txt")
        except:
            print("ERROR DE LECTURA")
        finally:
            self._numbredelarchivo = "Entrada.txt"
            
    def getJuego(self):
        juego = []
        for i in range(9):
            juego += [[0,0,0,0,0,0,0,0,0]]
        for i in range(9):
            for j in range(9):
                #self._juego[i][j]
                juego[i][j] = jg[i][j].get()
                if juego[i][j] == '':
                    juego[i][j] = 0
        return juego
    
    def reset(self):
        for i in range(9):
            for j in range(9):
                jg[i][j].set('')
                
    def save(self):
        f = open("Sudoku.txt", "a")
        try:
            for i in range(9):
                for j in range(9):
                    if self._juego[i][j].get() == '':
                        f.write("0")
                    else:
                        f.write(self._juego[i][j].get())
                    f.write(' ')
                f.write('\n')
            f.write('\n\n')
            f.close()
        except:
            print("ERROR AL AGUARDAR EL ARCHIVO")
        finally:
            f.close()
            
    def corrige(self, event):
        for i in range(9):
            for j in range(9):
                if jg[i][j].get() == '':
                    continue
                if len(jg[i][j].get()) > 1 or jg[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    jg[i][j].set('')
                    
    def complete(self):
        for i in range(9):
            for j in range(9):
                jg[i][j].set(self._juego[i][j])
                
    def Open(self):
        try:
            file = open(self._nombredelarchivo, 'r')
            
            texto = file.readline()
            texto = texto.split(' ')
            for i in range(0,9):
                for j in range(0,9):
                    if texto[0] == '0':
                        jg[i][j].set('')
                    else:
                        jg[i][j].set(texto[0])
                    texto.pop(0)
                texto = file.readline()
                texto = texto.split(' ')
            file.close()
            
        except:
            print("HAY UN ERROR")
        finally:
            file.close()
            
solucion = []
raiz = Tk()
txt = StringVar(raiz)
jg = []
for i in range(1, 10):
    jg += [[0,0,0,0,0,0,0,0,0]]
for i in range(0,9):
    for j in range(0,9):
        jg[i][j] = StringVar(raiz)
        
a = Janela(raiz)
raiz.mainloop()
                    
            
                
            
        
                
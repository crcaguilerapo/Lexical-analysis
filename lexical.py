import sys

class lexico:

    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B",
                "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

    reserved_word = ("var", "print", "input", "when", "if", "unless", "while", "return",
                    "until", "else", "do", "for", "next", "break", "and", "or", "num",
                    "bool", "end", "function", "true", "false")

    #empezar en 1
    flag = 0
    pointer = 0
    buffer = []
    state = 1
    line = 1
    endLine = 0
    token = {"token" : "", "lexeme" : "","line" : "", "position" : ""}
    def __init__(self, buffer):
        self.buffer = buffer

    def getNextToken(self):
        while True:
            token = ""
            if self.state == -1:
                print(f">>>Error léxico(línea:{self.line},posición:{self.flag + 1 - self.endLine})")
                break
            if self.pointer == len(self.buffer):
                break
            
            self.c = self.buffer[self.pointer]
            self.state, token = self.delta()
            self.pointer = self.pointer + 1
            if token!="":
                return token
                break


    def delta(self):
        if self.state == 1:
            if self.c == ";":
                #print(f"<tk_puntoycoma,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_puntoycoma","lexeme":"","line":self.line,"position" : (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1, self.token
            elif self.c == ",":
                self.token  = {"token" : "tk_coma", "lexeme" : "","line" : self.line, "position" : (self.flag + 1) - self.endLine}
                #print(f"<tk_coma,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1, self.token
            elif self.c == "(":
                #print(f"<tk_par_izq,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token" : "tk_par_izq", "lexeme" : "","line" : {self.line}, "position" : {(self.flag + 1) - self.endLine}}
                self.flag = self.pointer + 1
                return 1, self.token
            elif self.c == ")":
                self.token  = {"token" : "tk_par_der", "lexeme" : "","line" : self.line, "position" : (self.flag + 1) - self.endLine}
                #print(f"<tk_par_der,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1, ""
            elif self.c == "}":
                #print(f"<tk_llave_der,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token" : "tk_llave_der", "lexeme" : "","line" : {self.line}, "position" : {(self.flag + 1) - self.endLine}}
                self.flag = self.pointer + 1
                return 1, self.token
            elif self.c == "{":
                self.token  = {"token" : "tk_llave_izq", "lexeme" : "","line" : self.line, "position" : (self.flag + 1) - self.endLine}
                #print(f"<tk_llave_izq,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1, self.token
            elif self.c == "\n":
                self.line = self.line + 1
                self.flag = self.pointer + 1
                self.endLine = self.pointer + 1
                return 1, ""
            elif self.c == "\t":
                self.flag = self.pointer + 1
                return 1, ""
            elif self.c == " ":
                self.flag = self.pointer + 1
                return 1, ""
            elif self.c == "+":
                return 34, ""
            elif self.c == "-":
                return 30, ""
            elif self.c == "*":
                return 27, ""
            elif self.c == "/":
                return 24, ""
            elif self.c == "%":
                return 21, ""
            elif self.c == "<":
                return 18, ""
            elif self.c == ">":
                return 15, ""
            elif self.c == "=":
                return 12, ""
            elif self.c == "!":
                return 10, ""
            elif self.c == ":":
                return 7, ""
            elif self.c in self.alphabet:
                return 47, ""
            elif self.c in "@":
                return 44, ""
            elif self.c in self.digits:
                return 49, ""
            elif self.c in "#":
                return 42, ""
            else:
                return -1, ""
        elif self.state == 34:
            if (self.c == "+"):
                #print(f"<tk_incremento,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_incremento", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1, self.token
            elif self.c == "=":
                #print(f"<tk_sum_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_sum_asig", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1, self.token
            else:
                self.token = {"token":"tk_mas", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_mas,{self.line},{(self.flag + 1) - self.endLine}>")
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1, self.token
        elif self.state == 30:
            if self.c == "-":
                #print(f"<tk_decremento,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_decremento", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1, self.token
            elif self.c == "=":
                self.token = {"token":"tk_res_asig","lexeme" :"" ,"line" : self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_res_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                return 1, self.token
            else:
                self.token = {"token":"tk_menos", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_menos,{self.line},{(self.flag + 1) - self.endLine}>")
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1, self.token
        elif self.state == 27:
            if self.c == "=":
                self.token = {"token":"tk_mul_asig", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_mul_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                return 1, self.token
            else:
                self.token = {"token":"tk_mul", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_mul,{self.line},{(self.flag + 1) - self.endLine}>")
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1,self.token
        elif self.state == 24:
            if self.c == "=":
                self.token = {"token":"tk_div_asig", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_div_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                return 1, self.token
            else:
                #print(f"<tk_div,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_div", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1, self.token
        elif self.state == 21:
            if self.c == "=":
                #print(f"<tk_mod_asig,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_mod_asig", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                return 1, self.token
            else:
                #print(f"<tk_mod,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_mod", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1, self.token
        elif self.state == 18:
            if self.c == "=":
                #print(f"<tk_menor_igual,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_menor_igual", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                return 1, self.token
            else:
                self.token = {"token":"tk_menor", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_menor,{self.line},{(self.flag + 1) - self.endLine}>")
                self.pointer = self.pointer - 1
                self.flag = self.pointer
                return 1,self.token
        elif self.state == 15:
            if self.c == "=":
                self.token = {"token":"tk_mayor_igual", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_mayor_igual,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1, self.token
            else:
                #print(f"<tk_mayor,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_mayor", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1, self.token
        elif self.state == 12:
            if self.c == "=":
                #print(f"<tk_igualdad,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_igualdad", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1, self.token
            else:
                return -1, ""
        elif self.state == 10:
            if self.c == "=":
                #print(f"<tk_diferente,{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_diferente", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer + 1
                return 1, self.token
            else:
                return -1, ""
        elif self.state == 7:
            if self.c == "=":
                self.token = {"token":"tk_asignacion", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_asignacion,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer + 1
                return 1, self.token
            else:
                self.token = {"token":"tk_dospuntos", "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_dospuntos,{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1, self.token
        elif self.state == 47:
            if self.c in self.alphabet:
                return 47, ""
            elif self.c in self.digits:
                return 47, ""
            else:
                lexeme = ''.join(buffer[self.flag:self.pointer])
                if lexeme in self.reserved_word:
                    #print(f"<{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                    self.token = {"token":lexeme, "lexeme":"", "line": self.line, "position": (self.flag + 1) - self.endLine}
                else:
                    #print(f"<id,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                    self.token = {"token":"id", "lexeme":lexeme, "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1, self.token
        elif self.state == 44:
            if self.c in self.alphabet:
                return 45, ""
            else:
                return -1, ""
        elif self.state == 45:
            if self.c in self.alphabet:
                return 45, ""
            elif self.c in self.digits:
                return 45, ""
            else:
                lexeme = ''.join(buffer[self.flag:self.pointer])
                #print(f"<fid,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1, ""
        elif self.state == 49:
            if self.c in self.digits:
                return 49, ""
            elif self.c in ".":
                return 50, ""
            else:
                lexeme = ''.join(buffer[self.flag:self.pointer])
                self.token = {"token":"tk_num", "lexeme":lexeme, "line": self.line, "position": (self.flag + 1) - self.endLine}
                #print(f"<tk_num,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1, self.token
        elif self.state == 50:
            if self.c in self.digits:
                return 52, ""
            else:
                self.pointer = self.pointer - 1
                lexeme = ''.join(buffer[self.flag:self.pointer])
                #print(f"<tk_num,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_num", "lexeme":lexeme, "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 1
                return 1, self.token
        elif self.state == 52:
            if self.c in self.digits:
                return 52, ""
            else:
                lexeme = ''.join(buffer[self.flag:self.pointer])
                #print(f"<tk_num,{lexeme},{self.line},{(self.flag + 1) - self.endLine}>")
                self.token = {"token":"tk_num", "lexeme": lexeme, "line": self.line, "position": (self.flag + 1) - self.endLine}
                self.flag = self.pointer
                self.pointer = self.pointer - 2
                return 1, self.token
        elif self.state == 42:
            if self.c != "\n":
                return 42, ""
            else:
                self.line = self.line + 1
                self.flag = self.pointer + 1
                self.endLine = self.pointer + 1
                return 1, ""


st = sys.stdin.readlines()
buffer = "".join(st)

lex = lexico(buffer)
while (True):
    i = lex.getNextToken()
    if i == None:
        break
    print(i)

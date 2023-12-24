
DIGITS = '0123456789'
 
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

#ERRORS
class Error: 
    def __init__(self, error_name, details) -> None:
        self.error_name = error_name
        self.details = details
        
    def as_string(self):
        results = f'{self.error_name} : {self.details}'
        
        return results
    
    
class IllegalCharError(Error):
    def __init__(self, details) -> None:
        super().__init__('Ilgegal characters', details)

#POSITION



#




class Token:
    def __init__(self, type_, value=None) -> None:
        self.type = type_
        self.value = value
        
        
    def __repr__(self):
        if self.value: 
            return f'{self.type}:{self.value}'
        return f'{self.type}' 
        
        
        
        
        
class Lexer:
    def __init__(self, text) -> None:
        self.text = text 
        self.pos = -1
        self.current_char = None
        self.advanced()
        
    def advanced(self):
        self.pos +=1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
        
        
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advanced()
                
                
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
                
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advanced()
                
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advanced()
                
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advanced()
                
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advanced()
                
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advanced()
                
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advanced()
                
            else:
                char = self.current_char
                self.advanced()
                
                return [], IllegalCharError("'" + char + "'")
                
                
                        
        
        
        return tokens, None
        
        
    def make_number(self):
        num_str = ''
        dot_count = 0
        
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advanced()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))
        
        
        
        
        
###RUN

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    
    return tokens, error
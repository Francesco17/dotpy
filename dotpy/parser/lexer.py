import ply.lex as lex

class MyLexer(object):

    reserved = {
        'digraph':  'DIGRAPH',
        'node':     'NODE',
        'edge':     'EDGE',
        'rankdir':  'RANKDIR',
        'center':   'CENTER',
        'size':     'SIZE',
        'init':     'INIT',
        'label':    'LABEL'
    }
    # List of token names.   This is always required
    tokens = (
        'TERM',
        'NUMBER',
        'COMMA',
        'QUOTE',
        'ARROW',
        'SLPAR',
        'SRPAR',
        'COLON',
        'EQUALS',
        'CLPAR',
        'CRPAR',
        'LPAR',
        'RPAR'
    ) + tuple(reserved.values())

    # Regular expression rules for simple tokens
    t_COMMA = r','
    t_QUOTE = r'"'
    t_ARROW = r'\->'
    t_SLPAR = r'\['
    t_SRPAR = r'\]'
    t_CLPAR = r'\{'
    t_CRPAR = r'\}'
    t_LPAR = r'\('
    t_RPAR = r'\)'
    t_COLON = r';'
    t_EQUALS = r'='

    t_ignore = r' '+'\n'

    def t_TERM(self, t):
        r'[a-zA-Z\_]+'
        t.type = MyLexer.reserved.get(t.value, 'TERM')
        return t  # Check for reserved words

    def t_NUMBER(self, t):
        r'[0-9\.]+'
        t.type = MyLexer.reserved.get(t.value, 'NUMBER')
        return t  # Check for reserved words

    def t_error(self, t):
        print("Illegal character '%s' in the input formula" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

# Build the lexer and try it out
m = MyLexer()
m.build()           # Build the lexer
m.test('''digraph MONA_DFA {
 rankdir = LR;
 center = true;
 size = "7.5,10.5";
 edge [fontname = Courier];
 node [height = .5, width = .5];
 node [shape = doublecircle]; 4;
 node [shape = circle]; 0; 1; 2; 3;
 node [shape = box];
 init [shape = plaintext, label = ""];
 init -> 0;
 0 -> 1 [label="X"];
 1 -> 2 [label="X"];
 2 -> 3 [label="0"];
 2 -> 4 [label="1"];
 3 -> 3 [label="X"];
 4 -> 4 [label="X"];
}''')     # Test it
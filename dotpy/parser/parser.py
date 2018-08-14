import ply.yacc as yacc

class MyParser(object):

    def __init__(self):
        self.lexer = MyLexer()
        self.lexer.build()
        self.tokens = self.lexer.tokens
        self.symbols = self.lexer.reserved
        self.parser = yacc.yacc(module=self)

    def __call__(self, s, **kwargs):
        return self.parser.parse(s, lexer=self.lexer.lexer)

    def p_graph(self, p):
        '''graph : DIGRAPH TERM CLPAR stmt_list CRPAR
                 | DIGRAPH CLPAR stmt_list CRPAR'''
        pass

    def p_stmt_list(self, p):
        '''stmt_list : stmt COMMA stmt_list
                     | stmt SEMICOLON
                     | stmt'''
        if len(p) == 2 or len(p) == 3:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_stmt(self, p):
        '''stmt : node_stmt
                | edge_stmt
                | attr_stmt
                | TERM EQUALS TERM'''
        pass

    def p_node_stmt(self, p):
        '''node_stmt : NODE SEMICOLON
                     | NODE attr_list'''
        pass

    def p_edge_stmt(self, p):
        '''edge_stmt : EDGE SEMICOLON
                     | EDGE attr_list'''
        pass

    def p_attr_stmt(self, p):
        '''attr_stmt : NODE attr_list
                     | EDGE attr_list'''
        pass

    def p_attr_list(self, p):
        '''attr_list : SLPAR a_list SRPAR attr_list
                     | SLPAR SRPAR attr_list
                     | SLPAR a_list SRPAR
                     | SLPAR SRPAR'''
        pass

    def p_a_list(self, p):
        '''a_list : TERM EQUALS TERM SEMICOLON a_list
                  | TERM EQUALS TERM COMMA a_list
                  | TERM EQUALS TERM SEMICOLON
                  | TERM EQUALS TERM COMMA
                  | TERM EQUALS TERM a_list
                  | TERM EQUALS TERM'''
        pass

    def p_error(self, p):
        print("Error: syntax error when parsing '{}'".format(p))


if __name__ == '__main__':
    par = MyParser()
    with open('PDDLparser/prob.pddl', 'r') as f:
        domain = f.read()
        f.close()

    result = par(domain)
    print(result)
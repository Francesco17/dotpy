from dotpy.parser.lexer import MyLexer
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
        '''graph : DIGRAPH ID CLPAR stmt_list CRPAR
                 | DIGRAPH CLPAR stmt_list CRPAR'''
        pass

    def p_stmt_list(self, p):
        '''stmt_list : stmt stmt_list
                     | stmt SEMICOLON
                     | stmt SEMICOLON stmt_list
                     | stmt'''
        if len(p) == 2 or len(p) == 3:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_stmt(self, p):
        '''stmt : node_stmt
                | edge_stmt
                | attr_stmt
                | ID EQUALS ID'''
        pass

    def p_node_stmt(self, p):
        '''node_stmt : node_id attr_list
                     | node_id'''
        pass

    def p_edge_stmt(self, p):
        '''edge_stmt : node_id edge_rhs attr_list
                     | node_id edge_rhs'''
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

    def p_edge_rhs(self, p):
        '''edge_rhs : ARROW node_id edge_rhs
                    | ARROW node_id'''

    def p_node_id(self, p):
        '''node_id : ID'''
        pass

    def p_a_list(self, p):
        '''a_list : ID EQUALS ID SEMICOLON a_list
                  | ID EQUALS ID COMMA a_list
                  | ID EQUALS ID a_list
                  | ID EQUALS ID SEMICOLON
                  | ID EQUALS ID COMMA
                  | ID EQUALS ID'''
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
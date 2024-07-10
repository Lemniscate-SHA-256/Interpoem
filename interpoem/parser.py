import ply.yacc as yacc
from interpoem.lexer import tokens
from interpoem.parser import parser
from interpoem.interpreter import interpret_poem

def p_poem(p):
    '''poem : TITLE QUOTED_STRING AUTHOR QUOTED_STRING variables stanza_list'''
    p[0] = {'title': p[2], 'author': p[4], 'variables': p[5], 'stanzas': p[6]}

def p_variables(p):
    '''variables : VARIABLES '{' variable_list '}'
                 | empty'''
    p[0] = p[3] if len(p) == 5 else []

def p_variable_list(p):
    '''variable_list : variable_list variable
                     | empty'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else []

def p_variable(p):
    '''variable : IDENTIFIER ':' BOOLEAN ';' '''
    p[0] = {'name': p[1], 'value': p[3]}

def p_stanza_list(p):
    '''stanza_list : stanza_list stanza
                   | empty'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else []

def p_stanza(p):
    '''stanza : STANZA '{' line_list '}' '''
    p[0] = p[3]

def p_line_list(p):
    '''line_list : line_list line
                 | empty'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else []

def p_line(p):
    '''line : LINE '{' QUOTED_STRING ';' event_list '}' '''
    p[0] = {'text': p[3], 'events': p[5]}

def p_event_list(p):
    '''event_list : event_list event
                  | empty'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else []

def p_event(p):
    '''event : ON event_type '{' event_action_list '}' '''
    p[0] = {'type': p[2], 'actions': p[4]}

def p_event_type(p):
    '''event_type : HOVER
                  | CLICK
                  | TIME '(' INTEGER ')' '''
    p[0] = p[1] if len(p) == 2 else f'time({p[3]})'

def p_event_action_list(p):
    '''event_action_list : event_action_list event_action
                         | empty'''
    p[0] = p[1] + [p[2]] if len(p) == 3 else []

def p_event_action(p):
    '''event_action : CHANGE_TEXT QUOTED_STRING ';'
                    | PLAY_AUDIO QUOTED_STRING ';'
                    | DISPLAY_IMAGE QUOTED_STRING ';'
                    | SET_VARIABLE variable_action ';'
                    | conditional_event'''
    p[0] = {p[1]: p[2]} if len(p) == 4 else p[1]

def p_variable_action(p):
    '''variable_action : IDENTIFIER ':' BOOLEAN'''
    p[0] = {p[1]: p[3]}

def p_conditional_event(p):
    '''conditional_event : IF '{' condition '}' THEN '{' event_action_list '}' ELSE '{' event_action_list '}' '''
    p[0] = {'if': p[3], 'then': p[6], 'else': p[10]}

def p_condition(p):
    '''condition : CONDITION IDENTIFIER ';' '''
    p[0] = p[2]

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

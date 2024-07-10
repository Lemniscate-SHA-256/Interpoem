import ply.lex as lex

tokens = (
    'TITLE', 'AUTHOR', 'VARIABLES', 'STANZA', 'LINE', 'ON', 'IF', 'THEN', 'ELSE',
    'HOVER', 'CLICK', 'TIME', 'CHANGE_TEXT', 'PLAY_AUDIO', 'DISPLAY_IMAGE',
    'SET_VARIABLE', 'CONDITION', 'QUOTED_STRING', 'IDENTIFIER', 'BOOLEAN', 'INTEGER'
)

t_ignore = ' \t\n'
t_TITLE = r'title:'
t_AUTHOR = r'author:'
t_VARIABLES = r'variables'
t_STANZA = r'stanza'
t_LINE = r'line'
t_ON = r'on:'
t_IF = r'if:'
t_THEN = r'then:'
t_ELSE = r'else:'
t_HOVER = r'hover'
t_CLICK = r'click'
t_TIME = r'time\(\d+\)'
t_CHANGE_TEXT = r'change_text:'
t_PLAY_AUDIO = r'play_audio:'
t_DISPLAY_IMAGE = r'display_image:'
t_SET_VARIABLE = r'set_variable:'
t_CONDITION = r'condition:'
t_QUOTED_STRING = r'"[^"]*"'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_BOOLEAN = r'true|false'
t_INTEGER = r'\d+'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

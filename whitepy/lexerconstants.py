# Ref: http://compsoc.dur.ac.uk/whitespace/tutorial.html

CHAR_MAP = {'space': chr(32), 'tab': chr(9), 'lf': chr(10)}

IMP_CONST = [
    (CHAR_MAP['space'], 'STACK_MANIPULATION'),
    (CHAR_MAP['tab'] + CHAR_MAP['space'], 'ARITHMETIC'),
    (CHAR_MAP['tab'] * 2, 'HEAP_ACCESS'),
    (CHAR_MAP['lf'], 'FLOW_CONTROL'),
    (CHAR_MAP['tab'] + CHAR_MAP['lf'], 'IO')]

STACK_MANIPULATION_CONST = [
    (CHAR_MAP['space'], 'PUSH'),
    (CHAR_MAP['lf'] + CHAR_MAP['space'], 'DUP'),
    (CHAR_MAP['lf'] + CHAR_MAP['tab'], 'SWAP'),
    (CHAR_MAP['lf'] + CHAR_MAP['lf'], 'POP')]

ARITHMETIC_CONST = [
    (CHAR_MAP['space'] * 2, '+'),
    (CHAR_MAP['space'] + CHAR_MAP['tab'], '-'),
    (CHAR_MAP['space'] + CHAR_MAP['lf'], '*'),
    (CHAR_MAP['tab'] + CHAR_MAP['space'], '/'),
    (CHAR_MAP['tab'] * 2, '%')]

HEAP_ACCESS_CONST = [
    (CHAR_MAP['space'], 'STORE'),
    (CHAR_MAP['tab'], 'RETR')]

FLOW_CONTROL_CONST = [
    (CHAR_MAP['space'] * 2, 'MARK'),
    (CHAR_MAP['space'] + CHAR_MAP['tab'], 'CALL'),
    (CHAR_MAP['space'] + CHAR_MAP['lf'], 'JUMP'),
    (CHAR_MAP['tab'] + CHAR_MAP['space'], 'JUMP_IF_ZERO'),
    (CHAR_MAP['tab'] * 2, 'JUMP_IF_NEG'),
    (CHAR_MAP['tab'] + CHAR_MAP['lf'], 'END_SUB'),
    (CHAR_MAP['lf'] * 2, 'END')]

IO_CONST = [
    (CHAR_MAP['space'] * 2, 'OUTPUT_CHAR'),
    (CHAR_MAP['space'] + CHAR_MAP['tab'], 'OUTPUT_NUM'),
    (CHAR_MAP['tab'] + CHAR_MAP['space'], 'READ_CHAR'),
    (CHAR_MAP['tab'] * 2, 'READ_NUM')]

NUM_CONST = {CHAR_MAP['space']: "0", CHAR_MAP['tab']: "1"}

NUM_SIGN_CONST = {CHAR_MAP['space']: 'POSITIVE', CHAR_MAP['tab']: 'NEGATIVE'}

HAS_ARGS = ['PUSH', 'MARK', 'CALL', 'JUMP', 'JUMP_IF_ZERO', 'JUMP_IF_NEG']

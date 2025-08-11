import time
import pydoc

colors = (
    '\033[m',        # 0 - no color
    '\033[0;30;41m', # 1 - red
    '\033[0;30;42m', # 2 - green
    '\033[0;30;43m', # 3 - yellow
    '\033[0;30;44m', # 4 - blue
    '\033[0;30;45m', # 5 - purple
    '\033[7;30m'     # 6 - inverted white
)

def title(msg, color=0):
    length = len(msg) + 4
    print(colors[color], end='')
    print('~' * length)
    print(f'  {msg}')
    print('~' * length)
    print(colors[0], end='')

while True:
    title('PyHelp Help System', 2)
    command = input('Function or Library > ').strip()
    if command.upper() == 'END':
        break
    title(f"Accessing the manual for '{command}'", 4)
    time.sleep(1)
    try:
        obj = eval(command)
        doc = pydoc.render_doc(obj, "Help on %s")
        print(colors[6] + doc + colors[0])
    except NameError:
        print(colors[1] + f"Command '{command}' not found." + colors[0])

title('GOODBYE!', 1)
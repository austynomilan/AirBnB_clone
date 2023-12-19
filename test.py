#!/usr/bin/python3
import console
import inspect
import cmd
import io
import sys

import console

"""
 Create console
"""
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False

"""
 Exec command
"""
def exec_command(my_console, the_command, last_lines = 1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    the_command = my_console.precmd(the_command)
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])

"""
 Tests
"""
model_id = "not_found"

result = exec_command(my_console, "show Place {}".format(model_id))
if result is None or result == "":
    print("FAIL: no output")
    
search_str = "** no instance found **"
if result != search_str:
    print("FAIL: wrong output \"{}\" instead of \"{}\"".format(result, search_str))
    
print("OK")

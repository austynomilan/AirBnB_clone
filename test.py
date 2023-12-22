#!/usr/bin/python3
import inspect
import io
import sys
import cmd
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
    my_console.preloop()
    the_command = my_console.precmd(the_command)
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1*(last_lines+1)):-1])

model_class = "BaseModel"
model_id = "Nop"
attribute_name = "attribute_name"
attribute_value = "string_value"

result = exec_command(my_console, "{}.update(\"{}\", \"{}\", \"{}\")".format(model_class, model_id, attribute_name, attribute_value))
is_error = False
if result is None or result == "":
    pass  
elif result == "** no instance found *":
    is_error = True

if not is_error:
    result = exec_command(my_console, "{}.update({}, \"{}\", \"{}\")".format(model_class, model_id, attribute_name, attribute_value))
    if result is None or result == "":
        pass  
    elif result == "** no instance found *":
        is_error = True

if not is_error:
    result = exec_command(my_console, "{}.update(\"{}.{}\", \"{}\", \"{}\")".format(model_class, model_class, model_id, attribute_name, attribute_value))
    if result is None or result == "":
        pass  
    elif result == "** no instance found **":
        is_error = True

if not is_error:
    result = exec_command(my_console, "{}.update({}.{}, \"{}\", \"{}\")".format(model_class, model_class, model_id, attribute_name, attribute_value))
    if result is None or result == "":
        pass  
    elif result == "** no instance found **":
        is_error = True

if not is_error:
    print("FAIL: not found")

print("OK")

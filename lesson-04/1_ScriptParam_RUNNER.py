import runpy, subprocess, sys, os


# Модуль видит, что его запускают из модуля:
runpy.run_module(mod_name='1_ScriptParam')

# модуль запускается как бы из командной строки
subprocess.call(["py", os.path.dirname(sys.argv[0]) + "/1_ScriptParam.py", "100", "200", "300"])

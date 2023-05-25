from stagehand.sandbox import Sandbox, SandboxExtension
import subprocess
import sys

if sys.platform == 'win32':
    class CmdExtension(SandboxExtension):
        name = 'cmd'

        def eval(self, string):
            completed = subprocess.run(["cmd", "/C", string], capture_output=True)
            if completed.returncode == 0:
                result = completed.stdout.decode()
            else:
                result = completed.stderr.decode()
            Sandbox().tools.print(result)


    class PowershellExtension(SandboxExtension):
        name = ['powershell', 'ps']

        def eval(self, string):
            completed = subprocess.run(["powershell", "-Command", string], capture_output=True)
            if completed.returncode == 0:
                result = completed.stdout.decode()
            else:
                result = completed.stderr.decode()
            Sandbox().tools.print(result)

else:
    class ShellExtension(SandboxExtension):
        name = ['bash', 'sh']

        def eval(self, string):
            completed = subprocess.run(["bash", "-c", string], capture_output=True)
            if completed.returncode == 0:
                result = completed.stdout.decode()
            else:
                result = completed.stderr.decode()
            Sandbox().tools.print(result)
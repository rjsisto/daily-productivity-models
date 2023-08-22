# maybe switch this over to invoke or something like that
import argparse
import os

# TODO come up with a name for this run.py
parser = argparse.ArgumentParser(
    prog="makefile", description="The main way to access the project")

parser.add_argument(
    "-j", "--jup", help="Run the Jupyter Lab Server", action="store_true")
parser.add_argument(
    "-d", "--dash", help="Run the dashboard", action="store_true")
parser.add_argument("-c", "--create_env",
                    help="Create the virtual environment", action="store_true")
parser.add_argument(
    "-w", "--win", help="Manually tell the program to use windows syntax", action="store_true")
parser.add_argument(
    "-m", "--models", help="Create the models needed for the dashboard", action="store_true")

args = parser.parse_args()

# code to determine if os is windows or max/linux
win = None
# if(os.name == "posix"):
#   win = False
# elif(os.name == "nt" or args.win):
#   win = True

if (args.win):
    win = True

# TODO change this for windows
if (args.create_env):
    if (win):
        # os.system("call setup_env.bat")
        os.system("python -m venv .venv")
        os.system(".venv\Scripts\\activate && python.exe -m pip install --upgrade pip && pip install -r requirements.txt && deactivate")
        os.system(".venv\Scripts\\activate")
        os.system("python.exe -m pip install --upgrade pip")
        os.system("pip install -r requirements.txt")
        os.system("deactivate")
        print("Python environment setup complete")
    else:
        os.system("bash setup_env.sh")

# TODO create a windows script that emulates the setup_env.sh one
activate = None
if (win):
    activate = ".venv\Scripts\\activate &&"
else:
    activate = ". .venv/bin/activate;"


if (args.jup):
    os.system(activate + "jupyter-lab")
if (args.dash):
    os.system(activate + "python3 data_app/model_page.py")

if (args.models):
    os.system(activate + "python3 notebooks/create_models.py")

parser.print_help()

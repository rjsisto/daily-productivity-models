#maybe switch this over to invoke or something like that
import argparse
import os

#TODO create a windows script that emulates the setup_env.sh one
#code to determine if os is windows or max/linux
activate = None
if(os.name == "posix"):
    activate = "source .venv/bin/activate;"
elif(os.name == "nt"):
    activate = "activate windows python environment"

#TODO come up with a name for this run.py
parser = argparse.ArgumentParser(prog="makefile", description="The main way to access the project")

parser.add_argument("-j", "--jup", help="Run the Jupyter Lab Server", action="store_true")
parser.add_argument("-d", "--dash", help="Run the dashboard", action="store_true")
parser.add_argument("-c", "--create_env", help="Create the virtual environment", action="store_true")

args = parser.parse_args()
if(args.jup):
    os.system(activate + "jupyter lab")
if(args.dash):
    os.system(activate + "python data_app/model_page.py")

#TODO change this for windows
if(args.create_env):
    os.system("bash setup_env.sh")

parser.print_help()

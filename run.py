#TODO add a cli arguemnt (or automatically detect) if the script is being run in windows or linux/mac
import argparse
import os

#code to determine if os is windows or max/linux
activate = None
if(os.name == "posix"):
    activate = "source .venv/bin/activate;"
elif(os.name == "nt"):
    activate = "activate windows python environment"

#TODO come up with a name for this run.py
parser = argparse.ArgumentParser(prog="run.py", description="Run the various notebooks and the dashboard from here")

parser.add_argument("-j", "--jup", help="Run the Jupyter Lab Server", action="store_true")
parser.add_argument("-d", "--dash", help="Run the dashboard", action="store_true")

args = parser.parse_args()
if(args.jup):
    os.system(activate + "jupyter lab")
if(args.dash):
    os.system(activate + "python data_app/model_page.py")





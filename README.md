# process_term_optimus_dgpu
Automates terminating processes that blocks switching from iGPU to dGPU through Optimus

Requirements:
- Python3
- psutil (pip install psutil)

Once you have the requirements installed, put the Python script where you want and create a shortcut with any name with path to:
> cmd.exe /k python "path\to\python\process_term.py"


Go into the process_term.py and modify the list of programs in **process_names** to names of the programs that is blocking the iGPU/dGPU switch with exe

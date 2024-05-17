from time import sleep
from subprocess import run
from .job import Job


def run_slurm_string(command:str, fname:str, jobname:str, wait:bool=True):
    """Runs Slurm command by saving it first to a file and then running it.

    Parameters
    ----------
    connection : fabric.Connection
        
    command : str
        command to be executed
    jobname : str
        jobname of Slurm job
    wait : bool, optional
        if true, python waits until the Slurm job has finished, by default True
    Returns
    -------
    int
        returns the job ID
    """
    with open(fname, "w") as f:
        f.write(command)
    return run_slurm_file(fname, jobname, wait=wait)

    

def run_slurm_file(fname:str, jobname:str, wait:bool=True):
    """Runs Slurm script.

    Parameters
    ----------
    connection : fabric.Connection
        
    fname : str
        remote filename of Slurm script 
    jobname : str
        jobname of Slurm job
    wait : bool, optional
        if true, python waits until the Slurm job has finished, by default True
    Returns
    -------
    int
        returns the job ID
    """

    run(f"sbatch {fname}", shell=True)

    # wait for job to be created
    sleep(1)
    job = Job.from_name(jobname)

    if wait:
        while job.is_completed == False:
            sleep(0.1)

    return job.id
"""Functions to handle SLURM jobs on a remote cluster via SSH/Fabric."""

from subprocess import run
import numpy as np
import re
from quantiphy import Quantity
from .time import time_to_seconds, seconds_to_time
from rich.table import Table 
from rich.console import Console

class Job(object):

    def __init__(self, id):
        self.id = id

    @classmethod
    def from_name(cls, name):
        id = cls._get_job_id(name)
        return cls(id)

    def print(self):
        table = Table(title=f"Job: {self.id}")
        table.add_column("Property", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")
        table.add_row("Name", self.name)
        table.add_row("Status", self.status)
        table.add_row("User", self.user)
        table.add_row("Elapsed Time", seconds_to_time(self.elapsed_time))
        table.add_row("CPU Time", seconds_to_time(self.cpu_time))
        table.add_row("Allocated Memory", str(self.allocated_memory))
        table.add_row("Allocated CPUs", str(self.allocated_cpus))
        table.add_row("Allocated Nodes", str(self.allocated_nodes))
        table.add_row("Partition", self.partition)
        table.add_row("Nodes", str(self.nodes))
        console = Console()
        console.print(table)

    def __repr__(self):
        return f"Job {self.id} ({self.name})"
    
        
    @property
    def name(self, length_name=500):
        res = run(
            f"sacct -j {self.id} --format='JobName%{length_name}'",
            shell=True,
            text=True,
            capture_output=True,
        )

        return res.stdout.split()[2]

    @property
    def status(self):
        """Returns the status of the job.

        Returns
        -------
        str
            status of the job ("PENDING", "RUNNING", "COMPLETED", "FAILED", "UNKNOWN","CANCELLED")
        """
        res = run(
            f"sacct -j {self.id} --format='JobID%50,State%50' | grep {self.id}",
            shell=True,
            text=True,
            capture_output=True,
        )

        try:
            status = res.stdout.split()[1]
        except:
            status = "UNKNOWN"

        return status

    @property 
    def user(self):
        res = run(
            f"sacct -j {self.id} --format='User'",
            shell=True,
            text=True,
            capture_output=True,
        )

        return res.stdout.split()[2]
    
    @property 
    def elapsed_time(self):
        res = run(
            f"sacct -j {self.id} --format='Elapsed'",
            shell=True,
            text=True,
            capture_output=True,
        )

        time_str= res.stdout.split()[2]

        return time_to_seconds(time_str)
    
    @property 
    def cpu_time(self):
        res = run(
            f"sacct -j {self.id} --format='CPUTime'",
            shell=True,
            text=True,
            capture_output=True,
        )

        time_str= res.stdout.split()[2]

        return time_to_seconds(time_str)


    @property
    def is_completed(self) -> bool:
        try:
            res = run(
                f'squeue -o"%.50i" -j {self.id} | grep {self.id}',
                shell=True,
                text=True,
                capture_output=True,
            )
            res = res.stdout.split()
        except Exception as e:
            res = ""
        return not res

    @property
    def allocated_memory(self):
        return self._alloc_resources()[1]

    @property
    def allocated_cpus(self):
        return self._alloc_resources()[0]

    @property
    def allocated_nodes(self):
        return self._alloc_resources()[2]

    def kill(self, raise_exception=False):
        res = run(f"scancel {self.id} --verbose", shell=True, text=True, capture_output=True)
        if res.stderr != "" and raise_exception:
            raise Exception(res.stderr)

    @staticmethod
    def _get_job_id(name: str) -> int:
        """
        Get id of job with **unique** name.
        """
        s = run(
            f"squeue -o'%.50i %.128j' | grep {name}",
            shell=True,
            text=True,
            capture_output=True,
        )
        s = int(s.stdout.split()[0])
        return s

    @property
    def partition(self):
        res = run(
            f"sacct -j {self.id} --format='Partition'",
            shell=True,
            text=True,
            capture_output=True,
        )

        return res.stdout.split()[2]

    @property
    def nodes(self):
        res = run(
            f"sacct -j {self.id} --format='NodeList'",
            shell=True,
            text=True,
            capture_output=True,
        )
        out = res.stdout.split()[2]

        # with regex find all numbers in out
        nodes = re.findall(r"\d+", out)
        nodes = [int(node) for node in nodes]

        return nodes

    def _alloc_resources(self):

        cmd = f"sacct -j {self.id} --format='AllocTRES%100C'"

        res = run(
            cmd,
            shell=True,
            text=True,
            capture_output=True,
        )

        out = res.stdout.split()[2]
        out = out.split(",")

        cpus = out[1]
        mem = out[2]
        n_nodes = out[3]

        mem = re.findall(r"\d+", mem)[0] + mem[-1]
        mem = Quantity(mem)

        cpus = int(re.findall(r"\d+", cpus)[0])
        n_nodes = int(re.findall(r"\d+", n_nodes)[0])

        return cpus, mem, n_nodes


# %%

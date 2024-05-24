from subprocess import run
from rich.table import Table 
from rich.console import Console
from quantiphy import Quantity
from .cluster import Cluster
from .partition import Partition
from .settings import *

class Node(object):

    def __init__(self, id, leading_zeros=2):
        self.id = id

        self.name = f"{PREFIX_NODE}{str(id).zfill(leading_zeros)}"


    def _cpus(self):
        """Returns the number of allocated/idle/other CPUs on the specified node"""

        output = run(
            f'sinfo -o "%20C" -n {self.name} --noheader',
            text=True,
            capture_output=True,
            shell=True,
        )

        try:
            out = output.stdout.split("/")

            n_cpus_alloc = out[0]
            n_cpus_idle = out[1]
            n_cpus_other = out[2]

            return int(n_cpus_alloc), int(n_cpus_idle), int(n_cpus_other)
        except Exception as e:
            print(e)
            return None
    
    def print(self):
        table = Table(title="Node: " + self.name)
        table.add_column("Property")
        table.add_column("Value")
        table.add_row("Allocated CPUs", str(self.n_cpus_alloc))
        table.add_row("Idle CPUs", str(self.n_cpus_idle))
        table.add_row("Other CPUs", str(self.n_cpus_other))
        table.add_row("Memory", str(self.memory))
        table.add_row("Allocated Memory", str(self.memory_alloc))
        table.add_row("Partition", str(self.partition))

        console = Console()
        console.print(table)

    @property
    def dict(self):
        return {
            "name": self.name,
            "n_cpus_alloc": self.n_cpus_alloc,
            "n_cpus_idle": self.n_cpus_idle,
            "n_cpus_other": self.n_cpus_other,
            "memory": str(self.memory),
            "memory_alloc": str(self.memory_alloc),
            "partition": str(self.partition),
        }


    @property
    def n_cpus_alloc(self):
        """Returns the number of allocated CPUs on the specified node."""
        return self._cpus()[0]

    @property
    def n_cpus_idle(self):
        """Returns the number of idle CPUs on the specified node."""
        return self._cpus()[1]

    @property
    def n_cpus_other(self):
        """Returns the number of other CPUs on the specified node."""
        return self._cpus()[2]

    @property
    def n_cpus_total(self):
        """Returns the total number of CPUs on the specified node."""
        return self.n_cpus_alloc + self.n_cpus_idle + self.n_cpus_other

    @property 
    def memory(self):
        """Returns the available memory on the node."""
        output = run(
            f'sinfo -o "%20m" -n {self.name} --noheader',
            text=True,
            capture_output=True,
            shell=True,
        )
        try:
            return Quantity(float(output.stdout.strip())*1e6, "B")
        except Exception as e:
            print(e)
            return None
    
    @property 
    def memory_alloc(self):
        """Returns the amount of allocated memory on the node."""
        output = run(
            f'sinfo -O "AllocMem" -n {self.name} --noheader',
            text=True,
            capture_output=True,
            shell=True,
        )
        try:
            return Quantity(float(output.stdout.strip())*1e6, "B")
        except Exception as e:
            print(e)
            return None
    

    @property 
    def partition(self):
        """Returns the partition of the node."""
        cluster = Cluster()
        partitions = cluster.partitions
        for partition in partitions:
            nodes = Partition(partition).nodes
            if self.id in nodes:
                return partition
        
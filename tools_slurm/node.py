from subprocess import run
from rich.table import Table 
from rich.console import Console

class Node(object):

    def __init__(self, id, prefix="node", leading_zeros=2):
        self.id = id
        self.name = f"{prefix}{str(id).zfill(leading_zeros)}"


    def _cpus(self):
        """Returns the number of allocated/idle/other CPUs on the specified node"""

        output = run(
            f'sinfo -o "%20C" -n {self.name} --noheader',
            text=True,
            capture_output=True,
            shell=True,
        )
        out = output.stdout.split("/")

        n_cpus_alloc = out[0]
        n_cpus_idle = out[1]
        n_cpus_other = out[2]

        return n_cpus_alloc, n_cpus_idle, n_cpus_other
    
    def print(self):
        table = Table(title="Node: " + self.name)
        table.add_column("Property")
        table.add_column("Value")
        table.add_row("Allocated CPUs", str(self.n_cpus_alloc))
        table.add_row("Idle CPUs", str(self.n_cpus_idle))
        table.add_row("Other CPUs", str(self.n_cpus_other))

        console = Console()
        console.print(table)


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

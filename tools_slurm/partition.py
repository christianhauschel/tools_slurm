from subprocess import run
import re
from rich.table import Table 
from rich.console import Console

class Partition(object):

    def __init__(self, name):
        self.name = name

    def _cpus(self):
        """Returns the number of allocated/idle/other CPUs on the specified partition"""

        output = run(
            f'sinfo -o "%20C" -p {self.name} --noheader',
            text=True,
            capture_output=True,
            shell=True,
        )
        out = output.stdout.split("/")

        n_cpus_alloc = int(out[0])
        n_cpus_idle = int(out[1])
        n_cpus_other = int(out[2])

        return n_cpus_alloc, n_cpus_idle, n_cpus_other
    
    def print(self):
        table = Table(title="Partition: " + self.name)
        table.add_column("Property")
        table.add_column("Value")
        table.add_row("Nodes", str(self.nodes))
        table.add_row("Allocated CPUs", str(self.n_cpus_alloc))
        table.add_row("Idle CPUs", str(self.n_cpus_idle))
        table.add_row("Other CPUs", str(self.n_cpus_other))

        console = Console()
        console.print(table)


    @property
    def n_cpus_alloc(self):
        """Returns the number of allocated CPUs on the specified partition."""
        return self._cpus()[0]

    @property
    def n_cpus_idle(self):
        """Returns the number of idle CPUs on the specified partition."""
        return self._cpus()[1]

    @property
    def n_cpus_other(self):
        """Returns the number of other CPUs on the specified partition."""
        return self._cpus()[2]

    @property
    def nodes(self):
        """Returns the node names of a specified partition."""
        output = run(
            f'sinfo --partition {self.name} -o "%20n"',
            text=True,
            capture_output=True,
            shell=True,
        )
        output = output.stdout.split("\n")[1:-1]
        output = [out.strip() for out in output]
        return [int(re.findall(r"\d+", o)[0]) for o in output]

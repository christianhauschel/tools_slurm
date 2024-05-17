from subprocess import run
from rich.table import Table 
from rich.console import Console
class Cluster(object):
    def __init__(self):
        pass 

    @property
    def partitions(self):
        """Returns the available partitions on the cluster."""
        output = run(
            "sinfo --noheader -o '%20P'",
            text=True,
            capture_output=True,
            shell=True,
        )

        partitions = output.stdout.split()

        # remove "*" from partitions if present
        partitions = [p.replace("*", "") for p in partitions]

        return partitions
    

    def print(self):
        partitions = self.partitions
        table = Table(title="Cluster")
        table.add_column("Property")
        table.add_column("Value")
        table.add_row("Partitions", ", ".join(partitions))
        console = Console()
        console.print(table)

    def dict(self):
        return {
            "partitions": self.partitions,
        }
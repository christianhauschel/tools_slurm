from subprocess import run
from rich.table import Table 
from rich.console import Console
import re
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
        try:
            partitions = output.stdout.split()
            # remove "*" from partitions if present
            partitions = [p.replace("*", "") for p in partitions]
            return partitions
        except Exception as e:
            print(e)
            return None
    
    @property
    def nodes(self):
        """Returns the available nodes on the cluster."""
        output = run(
            f'sinfo -o "%20n"',
            text=True,
            capture_output=True,
            shell=True,
        )
        try:
            output = output.stdout.split("\n")[1:-1]
            output = [out.strip() for out in output]
            nodes = [int(re.findall(r"\d+", o)[0]) for o in output]
            return nodes
        except Exception as e:
            print(e)
            return None

    def print(self):
        partitions = self.partitions
        table = Table(title="Cluster")
        table.add_column("Property")
        table.add_column("Value")
        table.add_row("Partitions", ", ".join(partitions))
        table.add_row("Nodes", str(self.nodes))
        console = Console()
        console.print(table)

    @property
    def dict(self):
        return {
            "partitions": self.partitions,
            "nodes": self.nodes,
        }
    
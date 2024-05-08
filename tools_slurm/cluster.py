from subprocess import run

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
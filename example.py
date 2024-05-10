# %%

from pysection import *
from tools_slurm import Job, Node, Partition, Cluster, seconds_to_time

# Job
job = Job("91295") # finished job
# job = Job("91293") # cancelled job
job.print()
# job.kill()

# Cluster
cluster = Cluster()
cluster.print()

# Partition
name_partition = job.partition
partition = Partition(name_partition)
partition.print()


# Node
node = Node(partition.nodes[0])
node.print()

# %%

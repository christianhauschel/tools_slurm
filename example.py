# %%

from pysection import *
from tools_slurm import Job, Node, Partition, Cluster, seconds_to_time, optimal_job_singlenode
from quantiphy import Quantity

# Job
job = Job("96121") # finished job
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

# Optimal Single-Node Job
partition, n_cpus, memory = optimal_job_singlenode(
    partitions_included=["bravo", "charlie"],
    mem_min=Quantity("50", "GB"),
    mem_max=Quantity("100", "GB"),
    n_cpu_min=10,
    n_cpu_max=40,
)
print("Optimal Single-Node Job Settings")
print(" Partition: ", partition)
print(" #CPUs:     ", n_cpus)
print(" Memory:    ", memory)


# %%


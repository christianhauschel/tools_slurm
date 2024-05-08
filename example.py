# %%

from pysection import *
from tools_slurm import Job, Node, Partition, Cluster

# Job
section("Job")
job = Job("91085")
print("ID: ", job.id)
print("Name: ", job.name)
print("Status: ", job.status)
print("Finished? ", job.is_completed)
print("Memory: ", job.memory)
print("Partition: ", job.partition)
print("Nodes: ", job.nodes)

# Cluster
section("Cluster")
cluster = Cluster()
partitions = cluster.partitions
print("Partitions: ", partitions)

# Partition
name_partition = partitions[0]
section(f"Partition: {name_partition}")
partition = Partition(name_partition)
print("Nodes: ", partition.nodes)

print("CPU Status:")
print("\tAlloc: ", partition.n_cpus_alloc)
print("\tIdle: ", partition.n_cpus_idle)
print("\tOther: ", partition.n_cpus_other)

# Node
node = Node(partition.nodes[0])
section(f"Node: {node.name}")
print("CPU Status:")
print("\tAlloc: ", node.n_cpus_alloc)
print("\tIdle: ", node.n_cpus_idle)
print("\tOther: ", node.n_cpus_other)

# %%

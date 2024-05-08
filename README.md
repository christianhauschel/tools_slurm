# tools_slurm

```python
from pysection import *
from tools_slurm import Job, Node, Partition

# Job
section("Job")
job = Job("91085")
print(job.id)
print(job.name)
print(job.status)
print(job.is_completed)
print(job.memory)
print(job.partition)
print(job.nodes)

# Partition
name_partition = "alpha"
section(f"Partition: {name_partition}")
partition = Partition(name_partition)
print(partition.nodes)
print(partition.n_cpus_alloc)
print(partition.n_cpus_idle)
print(partition.n_cpus_other)

# Node
node = Node(partition.nodes[0])
section(f"Node: {node.name}")
print(node.n_cpus_alloc)
print(node.n_cpus_idle)
print(node.n_cpus_other)
```
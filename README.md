# tools_slurm

```python
from pysection import *
from tools_slurm import Job, Node, Partition, Cluster

# Job
section("Job")
job = Job("80000")
print("ID: ", job.id)
print("Name: ", job.name)
print("Status: ", job.status)
print("Finished? ", job.is_completed)
print("Alloc. Memory: ", job.allocated_memory)
print("Alloc. CPUs: ", job.allocated_cpus)
print("Alloc. Nodes: ", job.allocated_nodes)
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
```

Output:
```bash
╔══════════════════════════════════════════════════════════════════════════════╗
║   JOB                                                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
ID:  80000
Name:  SomeJobName
Status:  COMPLETED
Finished?  True
Alloc. Memory:  5G
Alloc. CPUs:  10
Alloc. Nodes:  1
Partition:  alpha
Nodes:  [5]

╔══════════════════════════════════════════════════════════════════════════════╗
║   CLUSTER                                                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
Partitions:  ['alpha', 'bravo', 'charlie']

╔══════════════════════════════════════════════════════════════════════════════╗
║   PARTITION: ALPHA                                                           ║
╚══════════════════════════════════════════════════════════════════════════════╝
Nodes:  [5, 6, 7, 8]
CPU Status:
        Alloc:  0
        Idle:  48
        Other:  0

╔══════════════════════════════════════════════════════════════════════════════╗
║   NODE: NODE05                                                               ║
╚══════════════════════════════════════════════════════════════════════════════╝
CPU Status:
        Alloc:  0
        Idle:  12
        Other:  0
```
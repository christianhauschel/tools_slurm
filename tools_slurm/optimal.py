from numpy import argmax
from quantiphy import Quantity

from .cluster import Cluster
from .node import Node
from .partition import Partition


def optimal_job_singlenode(
    partitions_included=["bravo", "charlie"],
    mem_min=Quantity("50GB"),
    mem_max=Quantity("100GB"),
    n_cpu_min=10,
    n_cpu_max=40,
):

    nodes = Cluster().nodes

    nodes_n_cpus_max = []
    nodes_mem_max = []
    nodes_allowed = []

    for n in nodes:
        node = Node(n)

        mem_free = Quantity(node.memory - node.memory_alloc, "B")

        if (
            node.n_cpus_idle >= n_cpu_min
            and node.partition in partitions_included
            and mem_free >= mem_min
        ):
            nodes_allowed.append(n)
            nodes_n_cpus_max.append(node.n_cpus_idle)
            nodes_mem_max.append(mem_free)

    if len(nodes_n_cpus_max) == 0:
        return None, None, None
    
    id_node = argmax(nodes_n_cpus_max)


    node = Node(nodes_allowed[id_node])

    # node.print()

    n_cpu =  max(n_cpu_min, min(n_cpu_max, node.n_cpus_idle))
    mem = max(mem_min, min(mem_max, Quantity(node.memory - node.memory_alloc, "B")))    

    return node.partition, n_cpu, mem

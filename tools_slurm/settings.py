import os 

if "SLURM_PREFIX_NODE" in os.environ:
    PREFIX_NODE = os.environ["SLURM_PREFIX_NODE"]
else:
    PREFIX_NODE = "node"

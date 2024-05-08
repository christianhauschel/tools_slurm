import unittest 
from tools_slurm import run_slurm_string, Job, Cluster
import os
import glob

class TestToolsSlurm(unittest.TestCase):

    def test_run_slurm(self):    

        # delete all local *.out files 
        files = glob.glob('test/*.out')
        for f in files:
            os.remove(f)

        cluster = Cluster()
        partitions = cluster.partitions
        partition = partitions[0]

        # create random name for job
        import random
        import string
        jobname = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        cmd = \
f"""#!/bin/sh
#SBATCH --job-name={jobname}
#SBATCH --time=00:10:00
#SBATCH --mem=100M
#SBATCH --partition={partition}
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --chdir=test

echo "Hello, World!"

# wait for 10 seconds
sleep 10

echo "Goodbye, World!"
"""
        fname = "test/test.sh"
        job_id = run_slurm_string(cmd, fname, jobname, wait=True)

        job = Job(job_id)

        print(job.id)

        self.assertTrue(job.is_completed)

if __name__ == "__main__":
    unittest.main()
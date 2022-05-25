To change the max jobs a user can submit, use `MaxSubmitJobs` in `/etc/slurm/slurm.conf`.

https://slurm.schedmd.com/slurm.conf.html


From an email from George. 

*
The OnDemand instance provides template scripts for Single Core, Single Node, and MPI jobs.  The slurm queueing system is configured with three "partitions" which are what SGE called queues.  The partitions are call short (which is the default), normal, and high. 

The normal partition is the lowest priority partition, is available on all nodes, and has an unlimited wall-clock time limit.  The short partition has a medium priority, is available on all nodes, and has a 3 hour wall-clock time limit.  The high partition is available on 4 nodes, has an unlimited wall-clock time limit, and has the highest priority.

If a job is running on a lower priority partition, it can be suspended by a higher priority job, but will then continue when the high priority job has been completed.  This is similar to how sos.q and all.q behaved previously. 
*

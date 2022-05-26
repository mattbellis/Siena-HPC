# Check `slurm` config

```
scontrol show config
```
Output will be something like
```
Configuration data as of 2022-05-26T10:41:42
AccountingStorageBackupHost = (null)
AccountingStorageEnforce = none
AccountingStorageHost   = localhost
AccountingStorageExternalHost = (null)
AccountingStorageParameters = (null)
AccountingStoragePort   = 0
AccountingStorageTRES   = cpu,mem,energy,node,billing,fs/disk,vmem,pages
AccountingStorageType   = accounting_storage/none
AccountingStorageUser   = root
AccountingStoreJobComment = Yes
AcctGatherEnergyType    = acct_gather_energy/none
AcctGatherFilesystemType = acct_gather_filesystem/none
AcctGatherInterconnectType = acct_gather_interconnect/none
AcctGatherNodeFreq      = 0 sec
AcctGatherProfileType   = acct_gather_profile/none
AllowSpecResourcesUsage = No
AuthAltTypes            = (null)
AuthAltParameters       = (null)
AuthInfo                = (null)
AuthType                = auth/munge
BatchStartTimeout       = 10 sec
BOOT_TIME               = 2022-05-24T20:41:21
```

# `sinfo` is good

Output looks something like this

```
mbellis@grawp:~/JOBS_skim_gaia> sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
short*       up    4:00:00      6  down* node[4-7,9,17]
short*       up    4:00:00      6    mix node[1-2,13-16]
short*       up    4:00:00      5  alloc node[3,20-22,24]
short*       up    4:00:00      6   idle node[8,10-11,18-19,23]
short*       up    4:00:00      1   down node12
normal       up   infinite      6  down* node[4-7,9,17]
normal       up   infinite      6    mix node[1-2,13-16]
normal       up   infinite      5  alloc node[3,20-22,24]
normal       up   infinite      6   idle node[8,10-11,18-19,23]
normal       up   infinite      1   down node12
high         up   infinite      3  alloc node[21-22,24]
high         up   infinite      1   idle node23
```

# Check the status of the partitions (queues: short, normal, high)

```
mbellis@grawp:~/JOBS_skim_gaia> scontrol show partition
PartitionName=short
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=YES QoS=N/A
   DefaultTime=NONE DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=04:00:00 MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED
   Nodes=node[1-24]
   PriorityJobFactor=1 PriorityTier=20 RootOnly=NO ReqResv=NO OverSubscribe=FORCE:4
   OverTimeLimit=NONE PreemptMode=GANG,SUSPEND
   State=UP TotalCPUs=288 TotalNodes=24 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerNode=UNLIMITED MaxMemPerNode=UNLIMITED

PartitionName=normal
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=N/A
   DefaultTime=NONE DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=UNLIMITED MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED
   Nodes=node[1-24]
   PriorityJobFactor=1 PriorityTier=10 RootOnly=NO ReqResv=NO OverSubscribe=FORCE:4
   OverTimeLimit=NONE PreemptMode=SUSPEND
   State=UP TotalCPUs=288 TotalNodes=24 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerNode=UNLIMITED MaxMemPerNode=UNLIMITED

PartitionName=high
   AllowGroups=ALL AllowAccounts=ALL AllowQos=ALL
   AllocNodes=ALL Default=NO QoS=N/A
   DefaultTime=NONE DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=UNLIMITED MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED
   Nodes=node[21-24]
   PriorityJobFactor=1 PriorityTier=30 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=GANG,SUSPEND
   State=UP TotalCPUs=48 TotalNodes=4 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerNode=UNLIMITED MaxMemPerNode=UNLIMITED
```

# Check status of nodes

```
sinfo
```
or
```
sinfo -R
```

# Bringing down a node for maintenance

https://www.advancedclustering.com/act_kb/tech-tip-taking-compute-nodes-down-for-maintenance/



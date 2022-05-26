# Check `slurm` config

```
scontrol show config
```
Output will be something like
```
onfiguration data as of 2022-05-26T10:41:42
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

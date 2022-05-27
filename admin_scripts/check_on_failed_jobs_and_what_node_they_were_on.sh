jobids=$(sudo grep "WEXITSTATUS 1" /var/log/slurmctld.log  | awk -F"=" '{print $2'} | awk '{print $1}' | tail -500)

echo $jobids

for jobid in $jobids
do
	echo $jobid
	sudo grep $jobid /var/log/slurmctld.log
done


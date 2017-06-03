This directory contains all scripts that need to be deployed on the grid

All data collection scripts are here

for i in $( ls ); 
do qsub -o $PWD/logs -e $PWD/logs $i 
done

qsub -o $PWD/logs -e $PWD/logs 

===========================================
sync commands:
rsync -av location/to/sync/from <user>@system:/where/to/sync/to
rsync -av <user>@system:/where/to/sync/from location/to/sync/to



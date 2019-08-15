#using Anaconda on Win 10 Pro, check my working environment in conda
ls .\Anaconda3\envs\
conda create -n bids

#to activate newly created environ
conda activate bids

#install dicom to bids python package
pip install dcm2bids
pip install --force dcm2bids

#can NOT run dcm2bids as it opens a new window asking "How do you want to open this file"
#so try using Ubuntu virtual machine on Win 10 Pro

import os
import sys
import csv
import glob

# open file, add samples to sample list or exit if file not found
# if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
#     with open(sys.argv[1], 'r') as infile:
#
# else:
#     print('Please enter valid file name')
#     exit()

infile = 'revert.samples.txt'
with open(infile, 'r') as infiletxt:
    sample_dict = dict()
    for line in csv.reader(infiletxt, delimiter='\t'):
         sample_dict[line[0]] = line[1]


#make qc_revert dir if doesn't exist
def make_revert_dir(woid):
    if not os.path.isdir('qc_revert'):
        print('qc_revert dir not found, creating qc_revert dir')
        os.mkdir('qc_revert')
    else:
        print('qc_revert exists')


def get_status_file(sample,woid):
    qc_status_file = woid + '.qcstatus.tsv'
    qc_status_dict = {}
    if os.path.exists(qc_status_file):

        with open(qc_status_file, 'r') as statustsv:
            status_reader = csv.DictReader(statustsv, delimiter='\t')
            for line in status_reader:
                qc_status_dict[line['DNA']] = line
                if sample in line['DNA'] and line['QC Directory']:
                    qc_dir = line['QC Directory']
    else:
        print(qc_status_file, 'not found, exiting')

    return qc_status_dict, qc_dir

#open status file
#get sample qc dir
#make new qc dir minus one if sample is found
#make revert dir if not present
#make sample.date revert dir
#make new files minus sample for new qc dir
#make sample only file for revert dir
#revert status in qc status file topup if specified


def main():
    for sample in sample_dict:
        woid = sample_dict[sample]

        if not os.path.exists(woid):
            print(woid, 'does not exist, exiting')
            exit()

        os.chdir(woid)
        print('Working directory is', woid)

        # get status file and qc.dir
        qc_status, qc_dir = get_status_file(sample=sample, woid=woid)
        print(qc_dir)










if __name__ == '__main__':
    main()
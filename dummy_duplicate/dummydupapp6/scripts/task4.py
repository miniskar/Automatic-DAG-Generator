import os
import time
import shutil
import math
import random
import filecmp
from collections import defaultdict

def task(filename,pathin,pathout):
	input_list = [pathin+'/'+ file for file in filename]
	count = defaultdict(lambda:0)
	if isinstance(filename, list):
		input_files = [pathin+'/'+file for file in filename]
		for i in range(0,len(input_files)-1):
			for j in range(i+1,len(input_files)):
				if filecmp.cmp(input_files[i],input_files[j], shallow=False):
					count[input_files[i]]=count[input_files[i]]+1
					count[input_files[j]]=count[input_files[j]]+1
		candidate=max(count, key=count.get)
		if count[candidate] < math.ceil(1.5):
			print('The validator can not come to aggreement')
			return -1

	execution_time = 1.4
	timeout = time.time() + execution_time
	while time.time() < timeout:
		1+1
	task_name = os.path.basename(__file__).split('.')[0]
	print('-------------------------')
	print(task_name)
	print(filename)
	print(pathin)
	print(pathout)
	print('-------------------------')
	if isinstance(filename, list):
		output1_list = [file.split('.')[0] +'_'+task_name+'.txt' for file in filename]
		input_file = filename[0].split('_')[0]
	elif not isinstance(filename, list):
		output1_list=[filename.split('.')[0] +'_'+task_name+'.txt']
		input_file = filename.split('_')[0]
	print(output1_list)
	output1=set(output1_list)
	print(output1)
	print(input_file)
	output_fname=[f.split('.')[0].split('_')[-1] for f in output1]
	output_name='_'.join(output_fname)
	output_name=input_file+'_'+output_name
	print(output_name)
	print('-------------------------@@@')
	print(os.path.realpath('communication.txt'))
	f = open('/centralized_scheduler/communication.txt', 'r')
	total_info = f.read().splitlines()
	f.close()
	comm = dict()
	multicast = dict()
	for line in total_info:
		src = line.strip().split(' ')[0]
		multicast[src] = line.strip().split(' ')[1]
		dest_info = line.split(' ')[2:-1]
		if len(dest_info)>0:
			comm[src] = dest_info
	print('-------------------------##')
	print(multicast)
	print(comm)
	print(comm.keys())
	print(task_name)
	if not os.path.isdir(pathout):
		os.makedirs(pathout, exist_ok=True)
	output_path=[]
	if task_name in comm.keys():
		print(comm[task_name])
		dest=[x.split('-')[0] for x in comm[task_name]]
		print(dest)
		comm_data=[str(math.ceil(float(x.split('-')[1]))) for x in comm[task_name]]
		print(comm_data)
		output_list=[]
		file_size=[]
		multicast[task_name]
		if multicast[task_name]=='false':
			print('Multicast is false')
			for idx,neighbor in enumerate(dest):
				print(neighbor)
				print(idx)
				new_file=output_name+'_'+neighbor
				output_list.append(new_file)
				file_size.append(comm_data[idx])
				new_path=os.path.join(pathout,new_file) 
				output_path.append(new_path)
				print(new_path)
				bash_script='/centralized_scheduler/generate_random_files.sh'+' '+new_path+' '+comm_data[idx]
				print(bash_script)
				os.system(bash_script)
		else:
			print('Multicast is true')
			print(dest[0])
			new_file=output_name
			print(comm_data)
			print(comm_data[0])
			new_path=os.path.join(pathout,new_file)
			bash_script='/centralized_scheduler/generate_random_files.sh'+' '+new_path+' '+comm_data[0]
			print(bash_script)
			os.system(bash_script)
	elif task_name not in comm.keys():
		new_file=output_name+'_'+task_name
		new_path=os.path.join(pathout,new_file) 
		print(new_path)
		output_path.append(new_path)
		file_size=str(random.randint(1,20))
		bash_script='/centralized_scheduler/generate_random_files.sh'+' '+new_path+' '+file_size
		print(bash_script)
		os.system(bash_script)

	return output_path

def main():
	filelist = '1botnet.ipsum'
	outpath = os.path.join(os.path.dirname(__file__), 'sample_input/')
	outfile = task(filelist, outpath, outpath)
	return outfile

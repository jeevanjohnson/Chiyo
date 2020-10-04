from subprocess import run, PIPE
from json import loads
from config import oppai_dir, map_dir
import os

os.chdir(oppai_dir)

acc = [100, 99, 98, 97, 96]

def oppai(beatmap_id):
	
	command = []
	ending_acc = []
	command.append(f'./oppai {map_dir}/{beatmap_id}.osu')
	for accuracy in acc:

		command.append(f'{accuracy}%')
		command.append('-ojson')

		process = run(
		' '.join(command),
		shell = True, stdout = PIPE, stderr = PIPE)
		
		output = loads(process.stdout.decode('utf-8', errors='ignore'))
		ending_acc.append('{Acc}%: {PP}PP'.format(PP=round(output["pp"], 2), Acc=accuracy))
		command.remove(f'{accuracy}%')
	return ending_acc
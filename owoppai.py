from subprocess import run, PIPE
from json import loads
from config import oppai_dir, map_dir
import os
import requests

acc = [100, 99, 98, 97, 96]

def oppai(beatmap_id, mods = None, accc = None):
	
	os.chdir(oppai_dir)

	if not os.path.exists('{mapdir}/{mapid}.osu'.format(mapdir = map_dir, mapid = beatmap_id)):
		with open('{mapdir}/{mapid}.osu'.format(mapdir = map_dir, mapid = beatmap_id), 'w') as b:
			d = requests.get("http://osu.ppy.sh/osu/{}".format(beatmap_id))
			b.write(d.content.decode("utf-8"))

	accc = '{}'.format(accc)
	command = []
	ending_acc = []
	command.append(f'oppai {map_dir}/{beatmap_id}.osu')
	if accc != 'None':
		command.append(f'{accc}%' if not '%' in accc else f'{accc}')
		
		if mods:
			command.append(f'+{mods}')
		
		command.append('-ojson')

		process = run(
		' '.join(command),
		shell = True, stdout = PIPE, stderr = PIPE)
		output = loads(process.stdout.decode('utf-8', errors='ignore'))
		ending_acc.append('{PP}PP for {Acc} FC'.format(PP=round(output["pp"], 2), Acc=accc))
	else:
		for accuracy in acc:

			if mods:
				command.append(f'+{mods}')

			command.append(f'{accuracy}%')
			
			command.append('-ojson')

			process = run(
			' '.join(command),
			shell = True, stdout = PIPE, stderr = PIPE)
			
			output = loads(process.stdout.decode('utf-8', errors='ignore'))
			ending_acc.append('{PP}PP for {Acc} FC'.format(PP=round(output["pp"], 2), Acc=accuracy))
			command.remove(f'{accuracy}%')
	return ending_acc
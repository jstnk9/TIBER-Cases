#############
## Author: Jose Luis Sanchez Martinez - @Joseliyo_Jstnk
## Date: 2022-02-08
## Version: 1.0
#############
import os, json, yaml, argparse

def parseYaml(inputPath, yamlFile):
	### Method to parse yml to JSON
	fullPath = os.path.join(inputPath,yamlFile)
	with open(fullPath, encoding='utf-8') as f:
		jsonData = yaml.load(f, Loader=yaml.FullLoader)
	return jsonData

def main(inputPath, recursively):
	# machinetag structure. More info https://www.circl.lu/doc/misp/taxonomy/
	machinetag = {
		"namespace": "Sigma",
		"expanded": "Sigma Rules Taxonomy",
		"description": "Sigma rules Taxonomy",
		"version": 1,
		"predicates": []
	}
	if recursively == True:
		for dirpath, dirs, files in os.walk(inputPath):

			if os.name == 'nt': # check if is Windows to set the path
				path = dirpath.split('/')[0]
			else:
				path = dirpath

			for f in files:
				if f.endswith(".yml"):
					jsonData = parseYaml(path, f)
					machinetag["predicates"].append({"value": "%s"%(f), "expanded": "%s"%(jsonData["description"])})
	else:
		# recursive deactivated
		for f in os.listdir(inputPath):
			if f.endswith(".yml"):
				jsonData = parseYaml(inputPath, f)
				machinetag["predicates"].append({"value": "%s"%(f), "expanded": "%s"%(jsonData["description"])})

	writeMachinetag(machinetag)

def writeMachinetag(machinetag):
	with open("machinetag.json", "w") as f:
		json.dump(machinetag, f)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Script to convert Sigma rules to machinetag.json taxonomy for MISP and TheHive")
	parser.add_argument("-p", "--path", dest="inputPath", required=True, default="None", help="Path where are the sigma rules")
	parser.add_argument("-r", "--recursive", dest="recursive", action="store_true", help="If you want convert all the sigma rules recursive from the path established")
	args = parser.parse_args()
	main(args.inputPath, args.recursive)
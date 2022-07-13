# Usage

Python3 is needed.

```
usage: sigma-taxonomy-generator.py [-h] -p INPUTPATH [-r]

Script to convert Sigma rules to machinetag.json taxonomy for MISP and TheHive

optional arguments:
  -h, --help            show this help message and exit
  -p INPUTPATH, --path INPUTPATH
                        Path where are the sigma rules
  -r, --recursive       If you want convert all the sigma rules recursive from the path established

```

## Example 1
```
python sigma-taxonomy-generator.py -r -p "/opt/sigmarules/sigma/rules"
```
Creates the file machinetag.json with all the sigma rules under `/opt/sigmarules/sigma/rules` path and subpaths.



## Example 2
```
python sigma-taxonomy-generator.py -p "/opt/sigmarules/sigma/rules/windows/process_creation"
```
Creates the file machinetag.json with all the sigma rules only under `/opt/sigmarules/sigma/rules/windows/process_creation` path **and not** subpaths.


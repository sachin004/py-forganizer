##################################################################################################################
# @author: Sachin Irukula <sachin.irukula@gmail.com>
# @file: forganizer.py
# @date: 13th July 2012
#
# This script creates a custom project with the specified directories subdirectories and files form an input file.
# If input file is not given and in place given any argument creates a project based on the arguments.
# Options:
# -dp: default project type 'f' for flex etc
# -p: Project title
# -ip: input file for creating custom project
# --version: prints the version the script
#################################################################################################################### 
import os, argparse

def create_project(project_name, file_name):
	f = open(file_name, 'r')
	if not os.path.exists(project_name):
		os.makedirs(project_name)
	else:
	    print "Project already exists"
	    exit()
	project = os.getcwd() + '/'+ project_name
	os.chdir(project)
	direct = {-1:project}
	for line in f:
	    if line != '\n':
			line = line.rstrip('\n')
			count = 0
			for i in range(len(line)):
				if line[i] == "-":
					count = count+1
				else:
					break
			line = line.lstrip('-')
			if count  == 0:
				filename, fileext = os.path.splitext(line)
				if direct[-1] != os.getcwd():
					os.chdir(direct[count - 1])
					direct = {-1:project}		
				if fileext == '':
					if not os.path.exists(line):
						os.makedirs(line)
						os.chdir(project + '/' + line)
						direct[0] = project + '/' + line
				else:
					f1 = open(line, 'w')
					f1.write('')
					f1.close()
			else:
				if count-1 in direct and direct[count - 1] != os.getcwd():
					os.chdir(direct[count - 1])
				filename, fileext = os.path.splitext(line)
				if fileext == '':
					if not os.path.exists(line):
						os.makedirs(line)
						os.chdir(direct[count - 1] + '/' + line)
						direct[count] = direct[count - 1] + '/' + line
				else:
					f1 = open(line, 'w')
					f1.write('')
					f1.close()
	
	f.close()
	return 0

def decision_project(args):
    if args['dp'] == "flex":
        if not os.path.exists(args['project_name']):
            os.makedirs(args['project_name'])
            project = os.getcwd() + '/'+ args['project_name']
            os.chdir(project)
            default_flex(project)
        else:
            print "Project already exists"
            exit()
    else:
        create_project(args['project_name'], args['input_file'])
    return 0

def default_flex(project):
    

def parse_arguments():
    parser = argparse.ArgumentParser(description='''Creates a project with 
    the specified directories subdirectories and files form an input file.
    **NOTE**: If input file is not given and in place given any argument 
    creates a project based on the arguments.''', 
    epilog="To report any bugs email <sachin.irukula@gmail.com>", 
    formatter_class=argparse.RawDescriptionHelpFormatter, conflict_handler='resolve')
    parser.add_argument('-p', dest = "project_name", help="project name")
    parser.add_argument('-ip', dest = "input_file", help="input file for project creation")
    parser.add_argument('-dp', dest = "dp", help="creates a default flex project/php project based on input")
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    args = vars(parser.parse_args())
    decision_project(args)
    exit()
    


if __name__ == "__main__":
	parse_arguments()

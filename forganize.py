######################################################################
# @author: Sachin Irukula <sachin.irukula@gmail.com>
# @file: forganizer.py
# @date: 29th April 2012
#
# This script creates a custom project with the specified 
#directories subdirectories and files form an input file.
# If input file is not given and in place given any argument
# creates a project based on the arguments.
# Options:
# -v: verbose - Show verbose mode
# -dp: default project type 'f' for flex etc
# -p: Project title
# -ip: input file for creating custom project
# --version: prints the version the script
######################################################################
import os, argparse

def create_project(args, project_name, file_name):
	f = open(file_name, 'r')
	if not os.path.exists(project_name):
		os.makedirs(project_name)
		print_verbose(args, project_name)
	else:
	    print "Project already exists"
	    exit()
	project = os.getcwd() + '/'+ project_name
	os.chdir(project)
	creation(args, project, f)	
	f.close()
	return 0

def decision_project(args):
    if args['dp'] == "flex":
        if not os.path.exists(args['project_name']):
            os.makedirs(args['project_name'])
            print_verbose(args, args['project_name'])
            project = os.getcwd() + '/'+ args['project_name']
            os.chdir(project)
            default_flex(args, project, args['project_name'])
        else:
            print "Project already exists"
            exit()
    else:
        create_project(args, args['project_name'], args['input_file'])
    return 0

def default_flex(args, project, a):
    f = ["src", "-assets", "--images", "--videos", "--skins", 
    "--style", "--lang", "---en_US", "---fr_FR", "-com", "--knolskape"
    , "---util", "---orgchart", "--adobe", "-events", "-php", 
    "-services", "-models", "-views", "--renders", "---common", 
    "--components", "-controllers", "-util", "--enum", "-Main.mxml", 
    "-README.txt"]
    creation(args, project, f)
    f1 = open(a + '.sql', 'w')
    f1.write('')
    f1.close()
    return 0    

def creation(args, project, f):
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
						print_verbose(args, line)
						os.chdir(project + '/' + line)
						direct[0] = project + '/' + line
				else:
					f1 = open(line, 'w')
					print_verbose(args, line)
					f1.write('')
					f1.close()
			else:
				if count-1 in direct and direct[count - 1] != os.getcwd():
					os.chdir(direct[count - 1])
				filename, fileext = os.path.splitext(line)
				if fileext == '':
					if not os.path.exists(line):
						os.makedirs(line)
						print_verbose(args, line)
						os.chdir(direct[count - 1] + '/' + line)
						direct[count] = direct[count - 1] + '/' + line
				else:
					f1 = open(line, 'w')
					f1.write('')
					print_verbose(args, line)
					f1.close()
    return 0

def print_verbose(args, single_file):
    if (args['VERBOSE'] == True):
        print "Created " + single_file    

def parse_arguments():
    parser = argparse.ArgumentParser(description='''Creates a project 
    with the specified directories subdirectories and files form an 
    input file.**NOTE**: If input file is not given and in place 
    given any argument creates a project based on the arguments.''', 
    epilog="To report any bugs email <sachin.irukula@gmail.com>", 
    formatter_class=argparse.RawDescriptionHelpFormatter, 
    conflict_handler='resolve')
    parser.add_argument('-p', dest = "project_name", 
                       help="project name")
    parser.add_argument('-ip', dest = "input_file", 
                       help="input file for project creation")
    parser.add_argument('-dp', dest = "dp", help="creates a default" 
                        "flex project/php project based on input")
    parser.add_argument('-v', '--verbose', dest='VERBOSE', 
                       default=False, action='store_true', 
                       help='Verbose mode')
    parser.add_argument('--version', action='version', 
                       version='%(prog)s 1.0')
    args = vars(parser.parse_args())
    decision_project(args)
    exit()

if __name__ == "__main__":
	parse_arguments()

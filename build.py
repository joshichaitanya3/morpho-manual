
# This is a script to generate the figures in the Examples chapter
# and build the reference section of the manual.

# To generate the figures, we run the morpho files provided in this repository.
# To build the reference section, we copy the help files from the libmorpho repository and add javascript syntax highlighting to the code blocks.

libmorphofolder = '/Users/chaitanya/Documents/GitHub/morpho-libmorpho' # Set this to your local libmorpho path. To-do: Download this from the Morpho GitHub repository instead.

docsfolder = libmorphofolder + '/help/' # This is the folder where the help files are located
reffolder = 'src/reference/nested/' # This is the folder where the reference files will be written to. Don't change this as it is hardcoded in the SUMMARY.md file

import os, glob, shutil
import urllib.request

executable = "morpho6" # This is the current CLI program name of Morpho. Making this a variable since it might change in the future.

createFigures = True # Set this to False once you have created the figures as they take quite a bit of time
buildReference = True

if createFigures:

    # The figures are created by running the program on the .morpho files in all the subfolders.
    print('--Creating figures-------------------------------')

    files=glob.glob('**/**.morpho', recursive=True)

    for f in files:
        print(f)
        # Run the program
        os.system(executable + ' ' + f)

if buildReference:
    print('--Building reference section---------------------')

    files=glob.glob(docsfolder+'**.md', recursive=True)

    # Since our help files are already Markdown, we could just copy them over in our reffolder and it would work.
    # Here, we do something a little extra by adding javascript syntax highlighting to the code blocks.

    # To do this, we identify code lines as the ones starting with 4 spaces or a tab, and then add '```javascript' before the code block and '```' after.
    def isCode(line):
        return line.startswith('    ') or line.startswith('    ')

    for f in files:
        filename=reffolder + f.split('/')[-1]
        print(filename) # This is the file we are writing to
        prevCode = False # This is to keep track of whether the previous line was a code line
        with open(f) as fin, open(filename, 'w') as fout: # Open the input and output files
            for line in fin:
                # Check if the line is a code line
                if isCode(line):
                    # If this line is a code but the previous line wasn't, this is the start of the code block. Add '```javascript' before the code block.
                    if not prevCode:
                        fout.write('```javascript\n')
                    # Set prevCode to True since this line is a code line
                    prevCode = True
                    fout.write(line[4:]) # Write the line without the 4 spaces
                else:
                    # If the current line is not a code line, we write the line.
                    # However, if the previous line was a code line, this indicates the end of the code block. Add '```' after the code block.
                    if prevCode:
                        fout.write('```\n')
                    fout.write(line)
                    # Since this is not a code line, set prevCode to False
                    prevCode = False

    print('-------------------------------------------------')

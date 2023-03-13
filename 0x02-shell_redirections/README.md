0-hello_world prints Hello, World
1-confused_smiley prints a confused smiley
2-hellofile displays the content of passwd file
3-twofiles displays the content of two files
4-lastlines displays the last 10 lines of a file
5-firstlines displays the first 10 lines of a file
6-third_line displays the third line of a file
8-cwd_state writes the output of ls -la to a file
9-duplicate_last_line duplicates the last line of the file iacta
10-no_more_js deletes all files with a .js extension
11-directories counts the number of directories and sub-directories in the current directory
12-newest_files displays the 10 newest files in the current directory.
13-unique  takes a list of words as input and prints only words that appear exactly once.
14-findthatword uses the grep utility to search for the pattern "root" in the file /etc/passwd. grep will print all lines that contain the pattern, which in this case will be all lines containing information about the "root" user 
15-countthatword Display the number of lines that contain the pattern “bin” in the file /etc/passwd
16-whatsnext uses the grep utility with the -A option to display the 3 lines that come after each line containing the pattern "root" in the file /etc/passwd. grep will search the file for the pattern and print the matching lines along with the specified number of lines after them.
17-hidethisword Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

The -v option invert the match and display all lines that do not contain the pattern "bin" in the file /etc/passwd. grep will search the file for lines that do not match the pattern and print them
18-letteronly displays all lines of the file /etc/ssh/sshd_config starting with a letter
19-AZ replaces  all characters A and c from input to Z and e respectively using the tr command
20-hiago removes all letters c and C from input using tr -d
21-reverse reverses the input using the rev command
22-users_and_homes displays all users and their home directories, sorted by users
100-empty_casks finds all empty files and directories in the current directory and all sub-directories
101-gifs  lists all the files with a .gif extension in the current directory and all its sub-directories

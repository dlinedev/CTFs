Fun with NASL
100
This script knows it has issues, and knowing is half the battle.
Find and fix the errors in this NASL script and then pass the fixed line numbers to the script to generate the flag.
The script contains bugs which generate the following errors and warnings: 
#1 - error P1000: syntax error, unexpected VAR, expecting ';'
#2 - warning C1097: defining global variable
#3 - Error: function '()' has no argument ''
#4 - add : bad types 31:3 for instruction

The script can be run using the following syntax to see the errors: 
$ nasl -W flag.nasl

Find and fix each error, making note of the line where the error was fixed.
Note that some errors/warnings will not appear until other bugs are fixed.
Review the script code to determine the preference name and preference value format that the script expects.
Then, pass the line numbers to the script as a preference value so it can use them to generate the flag: 
$ nasl -W -P 'my_pref_name=value' flag.nasl

The nasl command line executable is included with Nessus installations.If it isn't available in the path, the default locations are: 
*nix - /opt/nessus/bin/nasl
Windows - "C:\Program Files\Tenable\Nessus\nasl.exe"
OSX - /Library/Nessus/run/bin/nasl
See FAQ for more info on Nessus Essentials.

file: flag.nasl
# How To Use Bash Like a Hacker

## To Err Is Human

 Use `^old^new` to replace the wrong part of your previous command or improve your typo:
```bash
$ cat myflie
$ ^li^il
$ cat myfile
```
```bash
$ cond env list
$ ^d^da
$ conda env list
```

## To Forget History Is to Repeat It

Save commands to history without executing it
```bash
history -s <you-command>
```

Use `Ctrl + r` to reverse search history commands
```bash
bck-i-search: _
```
Use `!!` to execute the previous command, by adding `sudo` at the beginning you run the previous command as root
```bash

$ apt-get install conda
$ sudo !!
$ sudo apt-get install conda
```
Use `!?foo` to execute a command containing foo
```bash
$ !?Chrome
$ /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --app=http://127.0.0.1\?token\=
```
Use `!n` to execute the nth command
```bash
$ !20
$ less /var/log/system.log
```

Display your 10 common bash commands
```bash
history | awk '{CMD[$2]++;count++;}END { for (a in CMD)print CMD[a] " " CMD[a]/count*100 "% " a;}' | grep -v "./" | column -c3 -s " " -t | sort -nr | nl | head -n10
```
     1  94  18.8%  vim
     2  83  16.6%  g++
     3  77  15.4%  ls
     4  69  13.8%  cd
     5  11  2.2%   ps
     6  10  2%     man
     7  8   1.6%   git 
     8  6   1.2%   conda 
     9  5   1%     cp
    10  4   0.8%   ssh

Use `!:n` to get the nth parameter from a previous command
```bash
$ touch foo.py bar.py main.py
$ atom !:3
$ atom main.py
```
### macOSX

Get your external IP address:  
```bash
$ curl ifconfig.me
```
Get network IP:
```bash
ipconfig getifaddr en0
```
Open finder at place from terminal:
```bash
open .
```
Make your mac os read(verbally) a text file
```bash
say -f /path/to/file.txt
```


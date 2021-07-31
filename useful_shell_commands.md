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

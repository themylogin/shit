shit
====

This is a tool for easy sharing of your configs and scripts directories, containing passwords (such as [themylog_collectors](https://github.com/themylogin/themylog_collectors)) via git:

Installation
------------

```
python setup.py develop
alias shit='python -m shit'
```

Write your .shitignore file:

```
[server] ~/www/apps/themylog_collectors> cat .shitignore 
qwerty | <password>
713 | <bank card CVC2>
```

And use it like regular git repository

```
[server] ~/www/apps/themylog_collectors> shit init
Initialized empty Git repository in /home/themylogin/www/apps/themylog_collectors/.shit/.git/
[server] ~/www/apps/themylog_collectors> shit add vtb24.py
[server] ~/www/apps/themylog_collectors> shit commit -a -m 'VTB24'
[server] ~/www/apps/themylog_collectors> shit push
```

As you can see, it creates `.shit` directory where files with replaced passwords and git repository are stored.

Title: Setting Up a dedicated local development environment for PHP development.
Tags: PHP, Apache, MySQL, Ubuntu, XDebug
Summary: In this article I'll show how to set up a LAMP stack which is acronim for Linux, Apache, MySQL and PHP
Date: 2022/06/05
image: LAMP_stack

If you are making the first steps with PHP then you definetely will need some
sort of local development environment to run code on your own machine without
the need to push it to the remote server. While it is absolutely possible to
work with remote server, it'll seriously slows down development process. In
this article I'm going to show how to set up a **LAMP** stack which is
acronim for **Linux**, **Apache**, **MySQl** and **PHP**. In addition we'll
install **XDebug** and make it work nicely with VSCode and web browser, to debug code that receives HTTP request. Although this
configuration has some downsides such as the lack of isolation of dev sites
but if you are just starting up and not going to work on multiple projects at
once it may be a good alternative to the resource hungry and more complex
tools as [Vagrant](https://www.vagrantup.com/) or
[Docker](https://www.docker.com/). There is no doubt that for a serious
development those tools are preferable and we'll get there in the forthcoming
articles, but for now we are going to start with LAMP stack which nonetheless
will give us a good starting point. 


So let's get started.

## Step one - Installing Apache Web Server

Open up a terminal with ctrl+alt+t shortcut and run the command:

    $ sudo apt update

Then, install **Apache** with:

    $ sudo apt install apache2

When the prompt arise hit <mark>Y</mark> to confirm installation.
Now to verify that everything is installed properly enter to the browser
local address of your newly installed server:

    http://127.0.0.1/

Or just:

    localhost

The output will contain all information to test correct operation of **Apache2** server:

![Apache2 Welcome Page](/images/apache2_default_page.jpg)

## Step two - Installing MySQL

Now install database server MySQL:

    $ sudo apt install mysql-server

By default MySQL and Apache will start automatically on every boot. If this
is not what you want you could change that behavior. To check if the MySQL
and Apache are up and running issue next commands:

    $ sudo systemctl status mysql
    $ sudo systemctl status apache2

I'm going to remove those processes from autostart:

    $ sudo systemctl disable mysql
    $ sudo systemctl disable apache2

Then on every boot if I want to work with those servises I'll need to start
them like this:

    $ sudo systemctl start mysql
    $ sudo systemctl start apache2

It's up to you to leave it as is, and not bother yourself starting these
processes manually, but for the sake of saving resources I prefer to not
having them in autostart script, because single MySQL app takes around 300MB
of RAM.

Log in to **MySQL** as root:

    $ sudo mysql

List all users that present by default.

    mysql> SELECT user, host FROM mysql.user;

It'll show us a bunch of default system user accounts:
``` text
Output:
+------------------+-----------+
| user             | host      |
+------------------+-----------+
| debian-sys-maint | localhost |
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
+------------------+-----------+
```
Now we are able to create new users and give them only those **PRIVILEGES**
that needed.

To exit from mysql type:
```text
mysql> exit
```
## Step 3 - Installing PHP

For installing **PHP** all we basically need is to install just **PHP**
package. But to integrate our interpreter with Apache2 and MySQL we need two
additional packages **libapache2-mod-php** and **php-mysql**. 

These packages can be installed with:

    $ sudo apt install php libapache2-mod-php php-mysql

As the installation is finished run the following command to verify your PHP
version:

    $ php -v

```text
Output:
PHP 8.1.2 (cli) (built: Jun 13 2022 13:52:54) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.2, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.2, Copyright (c), by Zend Technologies
```
Now go to the default **virtual host** folder and create test **PHP** script:

```text
$ cd /var/www/html
```

Create new folder:

```text
$ sudo mkdir test
```

Open it and create test script:
```text
$ cd test
$ sudo vim phpinfo.php
```
In VIM press <mark>i</mark> to activate **INSERT** mode and type the following:

    <?php
    phpinfo();

To exit from VIM first press <mark>ESC</mark> to exit from 
<mark>INSERT</mark> mode then <mark>:wq</mark>. This will save your file and
exit from editor.
    
Now go to the address bar and enter: ``http://localhost/test/phpinfo.php``.

You should see something like this:

![PHP Info Page](/images/php_info.jpg)

## Step 4 - Installing XDebug

To install XDebug type in the next command and press ENTER:

    $ sudo apt install php-xdebug

To verify installation enter:

    $ php -v

If XDebug was installed the output should look like this:

``` text
PHP 8.1.2 (cli) (built: Jun 13 2022 13:52:54) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.1.2, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.2, Copyright (c), by Zend Technologies
    with Xdebug v3.1.2, Copyright (c) 2002-2021, by Derick Rethans
```

Now we need restart <mark>APACHE</mark> to apply new configuration.

    $ sudo systemctl restart apache2

Now run again test script by entering ``http://localhost/test/phpinfo.php``
in an address bar.

This time output shows us presence of XDebug itself and its ini config file.

![php-info-xdebug](/images/phpinfo_xdebug.jpg)

XDebug also have its own information page which we could reach by calling 
**xdebug_info()** function. To run it create another file inside
**test** directory and name it **xdebug_info.php**.

    $ sudo vim /var/www/html/test/xdebug_info.php 

Open it and add a call to the **xdebug_info()** function.

    <?php
    xdebug_info();

Now open newly created file in a browser again.

Here it is.

![XDebug info page](/images/xdebug_info.jpg)

At the top of the page we'll see the list of activated features.
In the **Settings** section below we can see all configuration files.
To active **Step Debugger** we need to add a couple of lines to the file called **20-xdebug.ini**.

Open the file in file editor.

    $ sudo vim /etc/php/8.1/apache2/conf.d/20-xdebug.ini

You'll see something like this:

    zend_extension=xdebug.so

Add these lines below:

    xdebug.mode=develop,debug
    xdebug.start_with_request=yes 

Now save file and exit with <mark>:wq</mark>. Those changes will activate 
step debugging feature and make xdebug start on request. To apply changes 
restart **Apache** again.

    $ sudo systemctl restart apache2

Now refresh the **XDebug** info page.

![XDebug info page with activated step debugger](/images/xdebug_info_update.jpg)

As we can see the **Step Debugger** is activated but **Diagnostic Log** shows us some weird errors. That's because we did not connected **XDebug** with **IDE** yet. So lets do this.

## Step 5 - Install VSCode

You can install VSCode by downloading deb package from official website and 
then install it with your package installer, or 
using your software center. Depending on your system it might be Ubuntu 
Software, Discover or something different. 

Now as you've installed VSCode install PHP Debug extension.

![PHP Debug extension](/images/PHP Debug.jpg)

To open a folder with our files we need to change permissions first.
So open a terminal in **VSCode** with <mark>Ctrl+`</mark> and type in the
command:

    $ sudo chown -R www-data /var/www/html/test

Now click **file>open folder**, navigate to the **/var/www/html** and open 
**test** folder. Next create a new file **upload.php** and paste into it
next code:

``` php
<?php // upload.php
echo <<<_END
<html><head><title>PHP Form Upload</title></head><body>
<form method='post' action='upload.php' enctype='multipart/form-data'>
Select File: <input type='file' name='filename' size='10'>
<input type='submit' value='Upload'>
</form>
_END;
if ($_FILES) {
    $name = $_FILES['filename']['name'];
    move_uploaded_file($_FILES['filename']['tmp_name'], $name);
    echo "Uploaded image '$name'<br><img src='$name'>";
}
echo "</body></html>";
```

Next press the **Run and Debug** button on the left sidebar and pick 
**create a launch.json file**. It will open a new tab already filled with 
configuration. Save it as is and click **Run and Debug** button then stop
debugging process by pressing on the red square and pick up from dropdown
menu near the green triangle **Listen for Xdebug** option.

![XDebug control panel](/images/debugging_control_panel.jpg)

Now set the breakpoint on line 9, open in the browser **upload.php** file,
choose some image and press **Upload**. Go through debugging steps..

![Bulletpoint stop](/images/bulletpoint_stop.jpg) 

Open browser again..

![It works!](/images/it_works.jpg)

Thats it! Now we are able to write, execute, debug code and 
connect databases. Happy coding!


# Wox.Plugin.Qrcode
A qrcode generator plugin for [wox][1]

## Features
* Support preview and save qrcode image
* Generater custom size/path/filename qrcode

## Usage
* Install [wox][1] on windows, and launch it（press `Alt+Space`）: 
* Input command `wpm install qrcode` to install this plugin
* Input `qr` key to active it

## Syntax
`qr content [-s size] [-p path] [-f filename] <size [path] [filename]>`

**【size】** qrcode'size, default 100px. Plugin will change size automatically to fit content'length.  
**【path】** qrcode'path, default Users Desktop. If path is not absolute, qrcode will also be saved in Users Desktop.  
**【filename】** qrcode'filename, default `qrcode.png`

 - `qr test ` 
 - `qr test 100 desktop-path` 
 - `qr test 100 C:\Users filename`
 - `qr test -s 100 -p C:\Users -f filename.png`

If a parameter contains any spaces, you should use quote, like this:   
`qr "this is my content" -p "D:\Program Files\qrcode" ...`

## Screenshot
![image](Images/screenshot.png)

[1]: http://www.getwox.com/

```
██       █████  ██    ██ ███████ ██████       ██████  ███    ██ ███████ 
██      ██   ██  ██  ██  ██      ██   ██     ██    ██ ████   ██ ██      
██      ███████   ████   █████   ██████      ██    ██ ██ ██  ██ █████   
██      ██   ██    ██    ██      ██   ██     ██    ██ ██  ██ ██ ██      
███████ ██   ██    ██    ███████ ██   ██      ██████  ██   ████ ███████ 
```

![Capture d’écran 2022-11-04 104119](https://user-images.githubusercontent.com/92639080/199942076-513e5e92-0e92-4d68-992f-be0827ec2b80.jpg)


```
___  ____ ____ ____ ____ _ ___  ___ _ ____ _  _ 
|  \ |___ [__  |    |__/ | |__]  |  | |  | |\ | 
|__/ |___ ___] |___ |  \ | |     |  | |__| | \| 
                                                
```

Set an **image top level** **front of all windows** and its the **opacity** / dimension + **clic trough**, in a Python script.

This little tool create a window to load a picture who will overlay everything, drived by its command's board.
Useful for **3D artists** who have to modelize with **layers** on software who are not giving this possibility, like **metahuman** from **unreal engine**, or else.
Also for pc gamers who would like to reproduce people in game, but also for science, for improving other projects.

Need some rework but it's working now, btw I will NOT make a .exe soon for this one.
The cause is every anti-malware will considere it like a virus because it could be, but let me explain ;

The probleme come from the possibility of put the layer front of all windows, that also mean it could avoid you to use your desktop blocking the mouse or whatever.

To avoid this problem I have 2 possibility ; pay for a certificate or hack your computer to say it's ok.
For those reasons I will not make an exe ; it's boring.
But don't worry you still can launch the program by following the next tutorial (fow windows users);

```
___ _  _ ___ ____ ____ _ ____ _    
 |  |  |  |  |  | |__/ | |__| |    
 |  |__|  |  |__| |  \ | |  | |___ 
                                   
```

I will improve the code when I will have time, for the moment it has some little issue but it's stable so I don't really care.
The most boring issue you may encounter will be the problem of resize / re catch the window.


**You can catch back the window if you resize by clicking on the border top** 



# TO LAUNCH THE FILE ;

You have 3 possibilities ; 


## 1. Launch by click on Layer1.exe

The first .exe file is a portable version made for windows 10, you can only download this and launch by click on it .


## 2. Launch by Python

"Python script" is directory with the original python script for python 3.10 / 3.11. 
In case you have a lower version you may have to download pillow/ pywin32 or other module imported not included with your version

If you want to launch it with python **YOU WILL NEED THE IMAGE SAD.png TO BE IN THE SAME DIRECTORY OF THE SCRIPT**.

Also I made 2 versions, all is described in the name but here's a remember ;
There is one prepared to be compiled with auto-py-to-exe who can't run, and another "layer1.pyw" you can launch whenever you want.
The w in pyw is for launch the python script without the CMD but it's still a common python file.


## 3. Compile yourself the python script (for windows 10) ;

For this part you will need auto-py-to-exe, here is the link 
 https://pypi.org/project/auto-py-to-exe/#description


- [ ] 0. Download the files (at least layer1.py and sad.png)

- [ ] 1.a Download and install python here ; https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe

DON'T FORGET TO TICK THE BOX " ADD PYTHON TO PATH "

- [ ] 1.b You can finalize this tutorial by right-clicking on layer1.py and select open with => python, but you can also ; 

- [ ] 2. Create a new text file on your desktop

- [ ] 3.In the text file type and write (and change/ complete the path, first is for python, 2nd is for layer1.py);

"C:\Users\ **YOUR USER NAME** \AppData\Local\Programs\Python\Python310\python.exe" "C:\Users\ **YOUR USER NAME** \Desktop\layer1.py"

- [ ]  4. Rename the file text by layer one.bat then just left-click in and it will run the program.
Btw you just probably create and run your first batch program.


If these steps are not working, before smashing your screen with your keyboard, you maybe wants to take a look to the noobugs cat.

```
_  _ ____ ____ ___  _  _ ____ ____ 
|\ | |  | |  | |__] |  | | __ [__  
| \| |__| |__| |__] |__| |__] ___] 
 ``` 
 
1. To be able to rename in .bat, you have to verify if you can;
You just have to open any file you want (Document or whatever) then go to display upside of the searchbar then tick the box asking you if you want to see the filename extextension

![tuto](https://user-images.githubusercontent.com/92639080/199935818-8d4f9bcf-5eb0-4a0d-9cd5-1eeb11182880.png)

Or you can check other possibilities to get it here ; https://www.wikihow.com/Change-a-File-Extension


2. Make sur you replaced the python path I wrote for example by the path where you have installed python without forget the Python.exe at end.

"C:\Users\ **YOUR USER NAME** \AppData\Local\Programs\Python\Python310\python.exe"

Again for the path of layer one, by default I wrote it's on the desktop, but you can put it where you want just change the path.

"C:\Users\ **YOUR USER NAME** \Desktop\layer1.py"

3.If it's still not running in .bat, it's possibly because you don't have installed libraries to run the script, here is a tutorial for Pillow (it's furnished with Python but I already saw this bug so ...
https://www.youtube.com/watch?v=KdLyS_tAvjY

4.You must put the sad.png in the  same file with layer1.py or you will not be able to put your images in the 2nd window. You can also simply erase the icon part of the script because it's where the error will be generated (the programm dosen't find the icon).

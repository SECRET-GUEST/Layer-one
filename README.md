Python version : 3.11
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

! THE SCRIPT IS MADE FOR WINDOWS 10 USERS !
I'm using pywin32 for clicthrough so if you're a **Linux** or **Mac** user you will need to adjust the code for your system 🏋️‍♂️ gl hf 🏋️‍♂️

```
___ _  _ ___ ____ ____ _ ____ _    
 |  |  |  |  |  | |__/ | |__| |    
 |  |__|  |  |__| |  \ | |  | |___ 
                                   
```

I will improve the code when I will have time, for the moment it has some little issue but it's stable so I don't really care.
The most boring issue you may encounter will be the problem of resize / re catch the window.


**You can catch back the window if you resize by clicking on the border top** 



# TO LAUNCH THE FILE ;

Because this script has no official signature it could be detected as a malware so I made 3 versions who show you it's safu.

I listed 5 possibilities to launch the program; 


## 1. Launch by click on Layer1.exe with confidence

The first .exe file is a portable version made for windows 10 with auto-py-to-exe, you can download only this file and nothing else.

There is another one .exe in the folder named "Layer 1 exe".
=> You can download the entire folder and click on the Layer1.exe you will find inside.
It's same version of the portable but you can check what's inside the file for more transparency.

## 2. Launch with Python

"Python script" is directory with the original python script for python 3.10 / 3.11. 
In case you have a lower version you may have to download module imported not included with your version ( pywin32 or maybe PIL ).

If you want to launch it with python **YOU WILL NEED THE IMAGE SAD.png TO BE IN THE SAME DIRECTORY OF THE SCRIPT**.

Also I made 2 versions, all is described in the name but here's a remember ;

- One prepared to be compiled with auto-py-to-exe who can't run solo (all is explained in the script)
- "layer1.pyw" ready to launch (if sad.png is in the same directory).

The w in pyw is added to launch the python script without the CMD but it's still a common python file.


## 3. Compile yourself the python script ;

**THIS IS A TUTORIAL FOR ABSOLUTE BEGINNER**

- [ ] 0. Download the files from "python script" (at least "sad.png" & "AUTOPY layer1.py", that you can rename without spaces to avoid futur errors )

- [ ] 1.a Download and install python here ; https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe

DON'T FORGET TO TICK THE BOX " ADD PYTHON TO PATH "

- [ ] 1.b You can finalize this tutorial by right-clicking on layer1.py and select open with => python, but you can also ; 

- [ ] 2. Compile the file yourself

Now you will need auto-py-to-exe, here is the link https://pypi.org/project/auto-py-to-exe/#description

You just have to click on the autopytoexe.py after the download and follow instructions, don't forget to add sad.png by tick additionnal files or it will not work.

Also you can obviously compile it from another way but I suppose auto-py-to-exe is the fastest and easiest way.

In case you're a **MAC** or **Linux** user or just not prefere to not compile in an .exe file

- [ ] 3. Create a new text file on your desktop

- [ ] 4.a. [WINDOWS] In the text file type and write (and change/ complete the path, first is for python, 2nd is for layer1.py);

"C:\Users\ **YOUR USER NAME** \AppData\Local\Programs\Python\Python310\python.exe" "C:\Users\ **YOUR USER NAME** \Desktop\layer1.py"

- [ ] 5. Rename the file text by layer one.bat then just left-click in and it will run the program.




If these steps are not working, before smashing your screen with your keyboard, you maybe wants to take a look to the noobugs.




```
_  _ ____ ____ ___  _  _ ____ ____ 
|\ | |  | |  | |__] |  | | __ [__  
| \| |__| |__| |__] |__| |__] ___] 
 ``` 
 
 
1. To rename in .bat, you have to verify if you can;
You just have to open any file you want (Document or whatever) then go to display upside of the searchbar then tick the box asking you if you want to see the filename extension

![tuto](https://user-images.githubusercontent.com/92639080/199935818-8d4f9bcf-5eb0-4a0d-9cd5-1eeb11182880.png)

Or you can check other possibilities to get it here ; https://www.wikihow.com/Change-a-File-Extension


2. Make sur you replaced the python path I wrote for example by the path where you have installed python without forget the Python.exe at end.

"C:\Users\ **YOUR USER NAME** \AppData\Local\Programs\Python\Python310\python.exe"

Again for the path of layer one, by default I wrote it's on the desktop, but you can put it where you want just change the path.

"C:\Users\ **YOUR USER NAME** \Desktop\layer1.py"

3.If it's still not running in .bat, it's possibly because you don't have installed libraries to run the script, here is a tutorial for Pillow (it's furnished with Python but I already saw this bug so ...
https://www.youtube.com/watch?v=KdLyS_tAvjY

4.You must put the sad.png in the  same file with layer1.py or you will not be able to put your images in the 2nd window. You can also simply erase the icon part of the script because it's where the error will be generated (the programm dosen't find the icon).

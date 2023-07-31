Module Installation Guide for MG-DOS Project
MG-DOS is an operating system project developed in the Python programming language. The project uses several third-party modules that must be installed before using MG-DOS.

Installing Modules Manually
Follow these steps to install modules manually:

Open a command prompt (on Windows) or a terminal (on macOS and Linux).

To install modules, use the pip install <module_name> command. Replace <module_name> with the name of the module you want to install.

For example, to install the colorama module, run the following command:

```
pip install colorama
```
Repeat this command for each module in the list of modules that you want to install.

Installing modules using a .bat file
To simplify the module installation process, you can create a .bat file (on Windows) or .sh file (on macOS and Linux) that will automatically install all required modules.

Setting up the .bat file
Create a new text file in the same folder as your MG-DOS project.

Open the file in a text editor and paste the following code:
```
@echo off
pip install colorama
pip install configparser
pip install alive-progress
pip install pillow
pip install playsound
pip install keyboard
pip install psutil
pip install deep_translator
REM Add any other modules you need for your MG-DOS project
```
Save the file and name it, for example, install_modules.bat.
Running the .bat file
Double click the install_modules.bat file in File Explorer.

The command prompt will open and the installation of the modules will start automatically.

Wait until all modules are installed.

After completing these steps, all required modules will be installed and you can use the MG-DOS project without having to install modules manually.

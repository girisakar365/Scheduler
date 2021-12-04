<p align = 'center'>![logo_dark](https://raw.githubusercontent.com/girisakar365/Scheduler/main/FrontEnd/Image/logo_l.png#gh-dark-mode-only)</p> <br>
<p align = 'center'>![logo_dark](https://raw.githubusercontent.com/girisakar365/Scheduler/main/FrontEnd/Image/logo.png#gh-light-mode-only) </p><br>
A School Routine Managing software!<br><br>

### File Management

Following are the main folder and files with their descriptions:

<br><b>Folders</b><br>

1. [`FrontEnd`](https://github.com/girisakar365/Scheduler/tree/main/FrontEnd)
2. [`BackEnd`](https://github.com/girisakar365/Scheduler/tree/main/BackEnd)

<br><b>FrontEnd</b>

|S.N | Files (.py) | Discription |
|----| ---- | ----------- |
|1.|[`__init__`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/__init__.py)|Initializes parent and child windows along with widget classes.|
|2.|[`Box`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/Box.py)|Initializes input boxes (i.e. Entry, Combo, Radio etc.)|
|3.|[`Button`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/Button.py)|Initializes buttons.|
|4.|[`Dialog`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/Dialogue.py)|Contains child/sub windows.|
|5.|[`Lable`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/Lable.py)|Initializes text elements.|
|6.|[`Photo_Lib`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/Photo_Lib.py)|Contains all the images and icons|
|7.|[`raw`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/raw.py)|FrontEnd database|
|8.|[`src`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/src.py)|Holds the main framework and common functions|
|9.|[`StyleSheet`](https://github.com/girisakar365/Scheduler/blob/main/FrontEnd/StyleSheet.py)|Contains all the style classes|

<br><b>BackEnd</b>

|S.N | Files (.py) | Discription | 
|----| ---- | ----------- |
|1.|[`__init__`](https://github.com/girisakar365/Scheduler/blob/main/BackEnd/__init__.py)|Handels backend modules.|
|2.|[`Allocation`](https://github.com/girisakar365/Scheduler/blob/main/BackEnd/Allocation.py)|Handles data sorting.|
|3.|[`Coordinates`](https://github.com/girisakar365/Scheduler/blob/main/BackEnd/Coordinates.py)|Generates table coordinates.|
|4.|[`Crypto`](https://github.com/girisakar365/Scheduler/blob/main/BackEnd/Crypto.py)|Cryptography handler.|
|5.|[`database`](https://github.com/girisakar365/Scheduler/blob/main/BackEnd/database.py)|Handles main database.|
|6.|[`domy`](https://github.com/girisakar365/Scheduler/blob/main/BackEnd/domy.py)|Generates random data for testing.|
|7.|[`Generator`](https://github.com/girisakar365/Scheduler/blob/main/BackEnd/Generator.py)|Data refinery.|

<br><b>API</b>
|S.N | Files (.py) | Discription | 
|----| ---- | ----------- |
|1.|[`Function`](https://github.com/girisakar365/Scheduler/blob/main/Function.py)|Connects frontend with backend.|
|2.|[`main`](https://github.com/girisakar365/Scheduler/blob/main/main.py)|Integrates the entire code base.|

<br><br>
### How are classes tranfered from one file to another ?

Each class contains a variable called __widget__ : __dict__ and a method called __collect__.<br>
- __widget__: Collects the specific variable using the widget class and store in a dict format.
- __collect__: Method that takes name of the widget class (as key) and variable of widget class (as value) as its parameters.<br><br>

The files that initializes the class can use these features to take the methods or variables containg widget class and use it.

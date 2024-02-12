What is this?
=============

Tower Of Hanoi is a puzzle game for the Sugar desktop.

![alt text](https://github.com/vaibhav-sangwan/tower-of-hanoi/blob/main/screenshots/instructions.png?raw=true)

How to use?
===========

Tower Of Hanoi can be run on the Sugar desktop.  Please refer to;

* [How to Get Sugar on sugarlabs.org](https://sugarlabs.org/),
* [How to use Sugar](https://help.sugarlabs.org/)

How to run?
=================

Dependencies:- 
- Python >= 3.10
- PyGObject >= 3.42
- PyGame >= 2.5
  
These dependencies need to be manually installed on Debian, Ubuntu and Fedora distributions.


**Running outside Sugar**


- Install the dependencies

- Clone the repo and run -
```
git clone https://github.com/vaibhav-sangwan/tower-of-hanoi.git
cd tower-of-hanoi
python main.py
```

**Running inside Sugar**

- Open Terminal activity and change to the Tower Of Hanoi activity directory
```
cd activities\TowerOfHanoi.activity
```
- To run
```
sugar-activity3 .
```
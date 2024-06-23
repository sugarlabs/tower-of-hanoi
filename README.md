What is this?
=============

Tower Of Hanoi is a puzzle game for the Sugar desktop. The goal of the game is to move the stack of disks to any one of the initially empty rods.

### Rules
1. Only one disk can be moved at a time.
2. Larger disks cannot be put on top of smaller ones.

![Screenshot of Tower Of Hanoi](https://github.com/vaibhav-sangwan/tower-of-hanoi/assets/94783049/1ac1387f-6105-4775-b8a0-79dab212c2e2)

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

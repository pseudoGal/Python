#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu aug  07 22:40:10 2021

@author: pratiksha

"""



import schedule
import time


def reminder():
	print("Maths Revision today...")
	
def good_luck():
	print("Good luck for revision!!")
		
def reminder1():
	print("Chapter 1 : Basics of calculas!")
	
def reminder2():
	print("Chapter 2,3 & 4 : Linear Algebra ")
	
	
def reminder3():
	print("Chapter 6,7 & 8:Vector")	
	
			
#schedule.every(250).seconds.do(reminder)
schedule.every(20).minutes.do(reminder)

schedule.every(3).hours.do(reminder1)
schedule.every().hour.do(good_luck)
#schedule.every().monday.do(good_luck)
schedule.every().monday.at("14:00").do(good_luck)
schedule.every(4).hours.do(reminder2)
schedule.every(6).hours.do(reminder3)

#schedule.every().hour.do()


while True:
    schedule.run_pending()
    time.sleep(1)
	

import tkinter as t
from tkinter import Tk
from tkinter import Label
from tkinter import Frame
from tkinter import Button
from tkinter import messagebox
from tkinter import Text

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

global driver

# Path of the firefox driver
# If error of permission or path occurs, you will get solution soon on the internet
driver = webdriver.Firefox(executable_path=r".\\geckodriver")
driver.get("https://studio.youtube.com/channel/UC1uOIfL2hiW4wEBexs8hCTQ")

def start():
    global driver
    try:
        driver.get("https://studio.youtube.com/channel/UC1uOIfL2hiW4wEBexs8hCTQ")
    except:
        driver = webdriver.Firefox(executable_path=r"C:\Users\HP\MachineLearningProjects\Fiverr\driver\geckodriver")
        driver.get("https://studio.youtube.com/channel/UC1uOIfL2hiW4wEBexs8hCTQ")

def addBulk():
    functionCall = rValue.get()
    if functionCall == 1:
        addBulkInHour()
    elif functionCall == 2:
        addBulkOutHour()
    else:
        messagebox.showwarning("Error : Select Video Type", "Please select the video type, either < hour(total time less than an hour) or >= hour(total time more than an hour).")

def addBulkInHour():
    global driver
    try:
        totalTime = int(textbox1.get('1.0', '1.4'))
        if totalTime >= 60:
            raise Exception()
    except:
        messagebox.showwarning("Error : Total Time box EMPTY/contain Decimal/not less than 60",
                               "Please enter total minutes in the Video in minutes, ofcourse < 60 minutes!")
        raise Exception()
    try:
        gapTime = int(textbox2.get('1.0', '1.4'))
        if gapTime <= 0:
            raise Exception()
    except:
        messagebox.showwarning("Error : Gap Time box EMPTY/contain Decimal", "Please enter Gap in ads in minutes!")
        raise Exception()
    try:
        startTime = int(textbox3.get('1.0', '1.4'))
        if startTime <= 0:
            raise Exception()
    except:
        messagebox.showwarning("Error : Time box EMPTY/contain Decimal",
                               "Please enter total minutes in the Video in minutes!")
        raise Exception()

    flagOne = True
    flagTwo = True
    flagThree = True
    flagFour = True
    flagFive = True
    for minute in range(startTime, totalTime, gapTime):
        sleep(1)
        # ad button
        driver.find_element_by_xpath('//*[@id="add-ad-break"]').click()
        sleep(.5)
        # click
        driver.find_element_by_xpath(
            '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input').click()
        sleep(.3)
        # leftArrowClick
        driver.find_element_by_xpath(
            '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
            Keys.ARROW_LEFT)
        sleep(.3)
        if minute < 10:
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                minute)
        elif minute < 20:
            if flagOne:
                counter = minute - 10
                flagOne = False
            #             if counter <= 9:
            #                 numOfBack = 1
            #             else:
            #                 numOfBack = 2
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                counter)
            counter += gapTime
        elif minute < 30:
            if flagTwo:
                counter = minute - 20
                flagTwo = False
            #             if counter <= 9:
            #                 numOfBack = 1
            #             else:
            #                 numOfBack = 2
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                counter)
            counter += gapTime

        elif minute < 40:
            if flagThree:
                counter = minute - 30
                flagThree = False
            #             if counter <= 9:
            #                 numOfBack = 1
            #             else:
            #                 numOfBack = 2
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                counter)
            counter += gapTime

        elif minute < 50:
            if flagFour:
                counter = minute - 40
                flagFour = False
            #             if counter <= 9:
            #                 numOfBack = 1
            #             else:
            #                 numOfBack = 2
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                counter)
            counter += gapTime

        elif minute < 60:
            if flagFive:
                counter = minute - 50
                flagFive = False
            #             if counter <= 9:
            #                 numOfBack = 1
            #             else:
            #                 numOfBack = 2
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                960)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                counter)
            counter += gapTime
        sleep(.5)
        # enterClick
        driver.find_element_by_xpath(
            "/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input").send_keys(
            Keys.RETURN)
        sleep(.5)
    messagebox.showinfo("Ads added", "Bot successfully added ads till {} minutes :)".format(minute))

def addBulkOutHour():
    global driver
    try:
        totalTime = int(textbox1.get('1.0', '1.4'))
        if totalTime < 60:
            raise Exception()
    except:
        messagebox.showwarning("Error : Total Time box EMPTY/contain Decimal/less than 60", "Please enter total minutes in the Video in minutes, ofcourse not less than 60 minutes!")
        raise Exception()
    try:
        gapTime = int(textbox2.get('1.0', '1.4'))
        if gapTime <= 0:
            raise Exception()
    except:
        messagebox.showwarning("Error : Gap Time box EMPTY/contain Decimal", "Please enter Gap in ads in minutes!")
        raise Exception()
    try:
        startTime = int(textbox3.get('1.0', '1.4'))
        if startTime <= 0:
            raise Exception()
    except:
        messagebox.showwarning("Error : Time box EMPTY/contain Decimal", "Please enter total minutes in the Video in minutes!")
        raise Exception()
    flagOne = True
    flagTwo = True
    flagThree = True
    for minute in range(startTime, totalTime, gapTime):
        # ad button
        driver.find_element_by_xpath('//*[@id="add-ad-break"]').click()
        sleep(.5)
        # click
        driver.find_element_by_xpath(
            '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input').click()
        sleep(.3)
        if minute > 9:
            # leftArrowClick
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                Keys.ARROW_LEFT)
        sleep(.2)
        if minute <= 60:
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                minute)
        elif minute <= 120:
            if flagOne:
                counter = minute - 60
                flagOne = False
            if counter <= 9:
                numOfBack = 1
            else:
                numOfBack = 2
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                61)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                numOfBack * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                counter)
            counter += gapTime
        elif minute <= 180:
            if flagTwo:
                counter = minute - 120
                flagTwo = False
            if counter <= 9:
                numOfBack = 1
            else:
                numOfBack = 2
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                61)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                61)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                numOfBack * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                counter)
            counter += gapTime
        elif minute <= 240:
            if flagThree:
                counter = minute - 180
                flagThree = False
            if counter <= 9:
                numOfBack = 1
            else:
                numOfBack = 2
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                61)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                61)
            sleep(.2)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                2 * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                61)
            # 2backSpaces
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                numOfBack * Keys.BACK_SPACE)
            sleep(.2)
            # entry
            driver.find_element_by_xpath(
                '/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input').send_keys(
                counter)
            counter += gapTime
        sleep(.5)
        # enterClick
        driver.find_element_by_xpath(
            "/html/body/ytve-ad-breaks-modal/ytve-modal-host/ytcp-dialog/paper-dialog/div[2]/div/ytve-editor/div[1]/div/ytve-ad-breaks-editor-options-panel/div[2]/div[1]/div/ytve-framestamp-input/div/ytve-formatted-input/input").send_keys(
            Keys.RETURN)
        sleep(.5)
    messagebox.showinfo("Ads added", "Bot successfully added ads till {} minutes :)".format(minute))

root = Tk()
root.title("Youtube")
root.iconbitmap(r"youtube.ico")
root.minsize(232, 0)
root.maxsize(232, 290)

fm = Frame(root, bg = "black", borderwidth=5)
fm.pack(pady=2, padx=2, fill="x")
# Left Frame in Middle Frame
fmm1 = Frame(fm, bg="black", borderwidth=2)
fmm1.pack(side="left")
f1 = Frame(fmm1, bg = "white", borderwidth=2)
f1.pack(padx=25, pady=2) # , anchor="center"

f1Label = Label(f1, text="Welcome Faculty", bg = "aqua", padx=3)
f1Label.grid(row=0, column=0, columnspan=2, pady=2, padx=1, sticky="ew")
f1Label = Label(f1, text="Video Total Time", bg = "aqua", padx=3)
f1Label.grid(row=1, column=0, columnspan=2, pady=2, padx=1, sticky="ew")
rValue = t.IntVar()
rA1 = t.Radiobutton(f1, text = "< 1 hr", variable = rValue, value = 1)
rA1.grid(row=2, column=0, pady=3, sticky="ew")
rA2 = t.Radiobutton(f1, text = ">= 1 hr", variable = rValue, value = 2)
rA2.grid(row=2, column=1, pady=3, sticky="ew")
f1Label = Label(f1, text="Enter Total Video Time", bg = "aqua", padx=3)
f1Label.grid(row=3, column=0, columnspan=2, pady=2, padx=1, sticky="ew")
textbox1 = Text(f1, width=10, height=1)
textbox1.grid(row=4, column=0, columnspan=2, pady=3, sticky="we")
f1Label = Label(f1, text="Enter Gap in ad-breaks", bg = "aqua", padx=3)
f1Label.grid(row=5, column=0, columnspan=2, pady=2, padx=1, sticky="ew")
textbox2 = Text(f1, width=10, height=1)
textbox2.grid(row=6, column=0, columnspan=2, pady=3, sticky="we")
f1Label = Label(f1, text="Enter 1st ad-break Time", bg = "aqua", padx=3)
f1Label.grid(row=7, column=0, columnspan=2, pady=2, padx=1, sticky="ew")
textbox3 = Text(f1, width=10, height=1)
textbox3.grid(row=8, column=0, columnspan=2, pady=3, sticky="we")
button1 = t.Button(f1, text="Login", bg = "aqua", command= lambda : start())
button1.grid(row=9, column=0, pady=3, padx=1, sticky="we")
button2 = Button(f1, text = "Start Adding Ads", bg = "aqua", command= lambda : addBulk())

# used for generating keys for particular computer use(additional library also used)
# if macAdress == "":
button2.grid(row=9, column=1, pady=3, padx=1, sticky='we')
# else:
    # messagebox.showwarning("Anauthorised Access", "You are not a authorised user of this software. Please mail : psgrewal211@gmail.com")
    # driver.quit()
    # exit()

root.mainloop()

import easygui as egui
import sys
import webbrowser
import os

from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def firt():
        #imgp = ".\cover.png"
        button_list = []
        button1 = "โค้ดสี"
        button2 = "สร้าง"
        button3 = "แจ้งปัญหา"
        button4 = "ออกจากโปรแกรม"
        button_list.append(button1)
        button_list.append(button2)
        button_list.append(button3)
        button_list.append(button4)
        fbtn = egui.buttonbox(title='โปรแกรมสร้างไฟล์ภาพนาฬิกานับถอยหลัง',msg='โปรแกรมสร้างตัวนับเวลาถอยหลังเป็นรูปภาพ (GIF)',choices = button_list)
        if fbtn=="โค้ดสี":
            #webbrowser.open("https://htmlcolorcodes.com/")
            os.startfile(".\colorpicker\Colora.exe")
            firt()
        elif fbtn=="สร้าง":
            clr()
        elif fbtn=="แจ้งปัญหา":
            if egui.ccbox(title='แจ้งพบปัญหาการใช้งานโปรแกรม',msg='พบปัญหาการใช้งานโปรแกรม ติดต่อ ไลน์ไอดี kaewdevil ขอบคุณครับ'):
                firt()
            else:firt()
        else:sys.exit()

def star():
        button_list = []
        button1 = "เปลี่ยนสี"
        button2 = "สร้างเพิ่ม"
        button3 = "ออกจากโปรแกรม"
        button_list.append(button1)
        button_list.append(button2)
        button_list.append(button3)
        ctn = egui.buttonbox(title='สร้างไฟล์สำเร็จ ... !!!',image=filename,msg='สร้างไฟล์สำเร็จ ต้องการสร้างเพิ่มหรือไม่ .. ?',choices = button_list)
        if ctn=="เปลี่ยนสี":
            clr()
        elif ctn=="สร้างเพิ่ม":
            crt()
        elif ctn==filename:
            star()
        else:sys.exit()

input_list = ["สีตัวเลข", "สีพื้นหลัง"]

default_list = ["#DE3163", "#FFFFFF"]

def clr():
    global output
    output = egui.multenterbox("หน้าต่างปรับแต่งสี", "ใส่โค้ดสีเพื่อระบุสีที่ต้องการ ... !" , input_list, default_list)
    if output:
        pass
    else:firt()
    global textc
    textc = output[0]
    global bg_color
    bg_color = output[1]
    crt()

def crt():
    input_list2 = ["นาที","วินาที"]
    default_list2 = ["00","00"]
    output2 = egui.multenterbox("หน้าต่างระบุเวลานับถอยหลัง", "ระบุเวลาที่จะทำตัวนับถอยหลังภายในช่อง" , input_list2, default_list2)
    if output2:
        mn = int(output2[0])*60
        sn = int(output2[1])*1
        rsms = mn+sn
        global seconds
        seconds = 1 * rsms
        pass
    else:firt()

    ln = "/Desktop/"+str(output2[0])+'.'+str(output2[1])+' Min.gif'

    global filename
    filename = egui.filesavebox(msg='Save file',title='บันทึกไฟล์ ระบุนามสกุล .gif',default=ln,filetypes='.gif')
    if filename:
        pass
    else:sys.exit()

    def nice_time(seconds):
            m, s = divmod(seconds, 60)
            return("{0:02d}:{1:02d}".format(m, s))

    labels = list(map(nice_time, reversed(range(seconds + 1))))

    with Image() as gif:
        for label in labels:
            with Drawing() as draw:
            #draw.font = "SourceSansPro-Light.otf"
                draw.font = ".\Roboto-Regular.ttf"
                draw.font_size = 140
                draw.fill_color = textc
                draw.text_alignment = "center"
                draw.text_antialias = True

                with Image(width=350, height=130, background=Color(bg_color)) as img:
                    x = int(img.width / 2)
                    y = int(img.height / 1.15)
                    draw.text(x, y, label)
                    draw.draw(img)
                    gif.sequence.append(img)
                    gif.loop = 1

            for frame in gif.sequence:
                with frame:
                    frame.delay = 100 
                    gif.save(filename=filename)
            print('กำลังสร้างนาฬิกานับถอยหลัง โปรดรอ PLEASE WAIT DO NOT CLOSE ...!!!')
        egui.msgbox(msg="สร้างไฟล์ GIF ของ "+output2[0]+" นาที "+output2[1]+" วินาที สำเร็จแล้ว..!!!",title="GIF Create Complete..!!!")

firt()

while 1==1:
   star()

    
   
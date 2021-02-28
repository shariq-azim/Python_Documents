import cv2
import requests
import numpy as np
import time
import math

def fun1():

    cap = cv2.VideoCapture('http://192.168.0.2:5757/video?x.mjpeg')
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


def fun2():

    #stream = cv2.VideoCapture('http://192.168.0.2:8080/video?x.mjpeg')
    stream = cv2.VideoCapture('http://192.168.0.2:8080/video/mjpeg')
    while True:
        r, f = stream.read()
        cv2.imshow('IP Camera stream',f)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

def usb_cam():

    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
def num_eg():
    #https://www.youtube.com/watch?v=-mJXEzSD1Ic
    url= 'http://192.168.0.2:8080/video/jpeg'#"http://192.168.0.2:5757/shot.jpg";
    i=0
    while i<3:
        img_resp= requests.get(url)
        img_arr= np.array(bytearray(img_resp.content),dtype= np.uint8)
        img= cv2.imdecode(img_arr,-1)
        cv2.imwrite('dash'+str(i)+'.jpeg',img)
        print('dash'+str(i)+'.jpeg')
        i=i+1
        '''
>0 Return a 3-channel color image.
Note In the current implementation the alpha channel, if any, is stripped from the output image. Use negative value if you need the alpha channel.
=0 Return a grayscale image.
<0 Return the loaded image as is (with alpha channel).'''

        cv2.imshow('IP Camera stream',img)
        time.sleep(1)

        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #cv2.destroyAllWindows()
        #break
 
def fun3():
    #stream = cv2.VideoCapture('https://www.w3schools.com/html/mov_bbb.mp4')
    i=4
    while i<6:
        inp=input(': ')
        print('run ',i)

        stream = cv2.VideoCapture('http://192.168.0.2:8080/video/jpeg')
        r, f = stream.read()
        #cv2.imshow('IP Camera stream',f)
        #cv2.waitKey(200)
        cv2.imwrite('image'+str(i)+'.jpg',f)
        print('image'+str(i)+'.jpg')
        cv2.imshow('IP Camera stream',f)
        i=i+1
        time.sleep(1)
        cv2.destroyAllWindows()

    #cv2.release()


def  img_load():
    im = cv2.imread("image5.jpg")
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) # grayscale
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    #cv2.GaussianBlur(
    #edged = cv2.Canny(gray, 50, 100)
    #edged = cv2.dilate(edged, None, iterations=1)
    #edged = cv2.erode(edged, None, iterations=1)
    #contours, hierarchy  = cv2.findContours(edged.copy,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    retval, thresh = cv2.threshold(gray, 127, 255, 0)
    img_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    '''
    for c in contours:
        [x,y,w,h] = cv2.boundingRect(c)
        if h<40 or w<40:
            continue
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,255),2)
        center = (x,y)
        print (center)
    while True:
        cv2.imshow('test',im)
        if cv2.waitKey(20) & 0xFF == 27:
            break
            '''
    cv2.drawContours(gray, img_contours, -1, (0, 255, 0),2)
    cv2.imwrite("image5GR.jpg",gray)
    #cv2.imshow('Image Contours 2x2', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def im2():
    image = cv2.imread("image1.jpeg")
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
    _,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) #threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
    contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # get contours
    # for  contour found, draw a rectangle around it on original iimage
    for contour in contours:
        
        # get rectangle bounding contour
        [x,y,w,h] = cv2.boundingRect(contour)
        '''# discard areas that are too large
        if h>200 and w>200:
            continue
        # discard are as that are too small
        if h<50 or w<40:
            continue''' 
        # draw rectangle around contour on original image
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
        # write original image with added contours to disk
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        #cv2.destroyAllWindows()
        print( cv2.contourArea(contour))
        #x,y,w,h = cv2.boundingRect(contour)
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255,0), 2)
        center = (x,y)
        print (center)
        cv2.destroyAllWindows()
        #for i in range(len(contours)):
    #cv2.imshow('test',image)
    #if cv2.waitKey(20) & 0xFF == 27:

    
def hou():
    import math
    ''':param path ????????:returns lines_data ?????????resize_pic ??????
    '''
    img2= cv2.imread("image4.jpg")
    img = cv2.imread("image4GR.jpg")
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # grayscale
    #gray = cv2.GaussianBlur(gray, (5,5), 0)
    
    #resize_pic=img
    #resize_pic=cv2.resize(img,(640,480),interpolation=cv2.INTER_CUBIC)
    edges = cv2.Canny(img, 75, 150)
	
    #lines_data = cv2.HoughLines(edges,1,math.pi/180,100)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 1, maxLineGap=5 )
    c=0
    for rho,theta,alph,beta in lines[0]:
        print(lines[0])
        a = math.cos(theta)
        b = math.sin(theta)
        if(c<11):
            print(a,b,c)
            c=c+1
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
    '''for line in lines:
        x1, y1, x2, y2 = line[0]
        
        zer=int(0)
        cv2.line(edges, (x1, y1), (x2, y2), (0, 255, 0), 1)
        #print((int(x2)- int(x1)) )
        if ( (int(x2)- int(x1)) != zer ) and ((int(y2)-int(y1)) != zer) :
            slope=((int(y2)-int(y1)) / (int(x2)- int(x1)))
            if abs(slope)< 1 :
                
                cv2.line(edges, (x1, y1), (x2, y2), (0, 255, 0), 3)
                
    '''
    
    while True:
        cv2.imshow('original',img2)
        cv2.imshow('houghlines',edges)
        if cv2.waitKey(1)& 0xFF == 27:
            break
    cv2.destroyAllWindows() 


def hi2():
    #import numpy as np
    
    img =  cv2.imread('image4.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    im2 = cv2.GaussianBlur(gray, (3,3), 0)
    dimen=im2.shape

    #edges = cv2.Canny(im2, 75, 150)

    ret,thresh = cv2.threshold(im2,45 ,255,0)
    
    try:
        
       
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0,len(contours)):
            cnt = contours[i]
            
            M = cv2.moments(cnt)
            
            if(M["m00"] != 0 and cv2.contourArea(cnt)<18000 and cv2.contourArea(cnt)>150):
                
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                perimeter = cv2.arcLength(cnt,True)
                #epsilon = 0.1*perimeter
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)#
                #print(list(a)[0],list(b)[0],list(c)[0],list(d)[0])
                
                listy = []
                for row in range(4):
                    inner_list = []
                    for col in range(2):
                        inner_list.append(box[row][col])

                    #print(inner_list[col][row])
                    print(inner_list[0])
                    print(inner_list[1])

                    cv2.putText(im2,str(int(inner_list[0]))+'.'+str(int(inner_list[1])),(inner_list[0], inner_list[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)

                    listy.append(inner_list)
                print("tjos/n",listy)    
                #box = np.int0([a][b][c][d])
                #box=[[k for row in list(a)] for column in range(4)]
                #print([box])
                
                #im = cv2.drawContours(im2,list_of_lists,0,(0,255,0),2)#[[a][b][c][d]]
                
                for i in range(4):
                    im=cv2.line(im2, tuple(listy[i]), tuple(listy[(i + 1) % 4]), (0,255,0), 2, cv2.LINE_AA, 0);

                #im =cv2.line(im2,(listy),(x2,y2),(0,0,255),2)


                

                print( (cX  , cY),"area: ",cv2.contourArea(cnt),"perimeter:",perimeter)
                cv2.circle(im, (cX, cY), 4, (0, 0, 255), -1)
                '''
                cv2.putText(im,str(cv2.contourArea(cnt)),(cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
                '''
                fromCenter = False
                #ROIs = cv2.selectROIs('Select ROIs', im, showCrosshair=False,fromCenter)
                #im=im[int(dimen[0])-125:int(dimen[0])-25, int(dimen[1])-450:int(dimen[1])-50]

                #approx = cv2.approxPolyDP(cnt,epsilon,True)
                #print(approx,i)
                #cv2.drawContours(im, [cnt],-2,(0,255,0))

        im_ROI1=im[int(dimen[0])-125:int(dimen[0])-25, int(dimen[1])-680:int(dimen[1])-50]
        im_ROI2=im[int(dimen[0])-300:int(dimen[0])-100, int(dimen[1])-640:int(dimen[1])-80]

        print("1",int(dimen[0])-125,int(dimen[0])-25, int(dimen[1])-680,int(dimen[1])-50)
        print("2",int(dimen[0])-300,int(dimen[0])-100, int(dimen[1])-640,int(dimen[1])-80)



        while True:
            cv2.imshow('Features',im )
            cv2.imshow('Features0',im_ROI1 )
            cv2.imshow('Features1',im_ROI2 )
            if cv2.waitKey(1)& 0xFF == 27:
                break
        cv2.destroyAllWindows()
    except (KeyboardInterrupt, SystemExit):
        return 'exiting'

#############################################################################
#############################################################################
#############################################################################

def hi():
    
    #import numpy as np
    img =  cv2.imread('image5.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray1=gray
    gray2=gray1
    
    dimen=gray.shape
    img_arr=[]
    #edges = cv2.Canny(im2, 75, 150)
    for roi in range(0,2):
        if(roi<1):
            gdy1=int(dimen[0])-125
            gdy2=int(dimen[0])-25
            gdx1=int(dimen[1])-680
            gdx2=int(dimen[1])-40
            
            xn=int((gdx2-gdx1)/2)
            yn=int((gdy2-gdy1)/2)
            
            #im2 = cv2.GaussianBlur(gray, (1,1), 0)
            im_ROI1=gray1[gdy1:gdy2, gdx1:gdx2]
            #im2=im_ROI1
            
            print(">>>>>>>>>>>>>>>>>",gdx1,gdx2,gdy1,gdy2,xn,(2*yn))

            
            #cv2.circle(im_ROI1, (xn,(2*yn)), 6, (0, 0, 255), -1)
            #print("1st loop")
            
            
            img_fun=opt(im_ROI1,30,(xn,yn))
            img_arr.append(img_fun)
             
            if(isinstance(img_fun, str) and img_fun=='STOP'):
                print ("stopping")
                break
            
        else:
            gdy1=int(dimen[0])-300
            gdy2=int(dimen[0])-100
            gdx1=int(dimen[1])-640
            gdx2=int(dimen[1])-80
            
            xn=int((gdx2-gdx1)/2)
            yn=int((gdy2-gdy1)/2)
            im3 = cv2.GaussianBlur(gray2, (3,3), 0)          
            im_ROI2=im3[gdy1:gdy2,gdx1:gdx2]
            print("###################",gdx1,gdx2,gdy1,gdy2,xn,(2*yn))
            #im2=im_ROI2
            #cv2.circle(im_ROI2, (xn , (2*yn) ), 4, (0, 0, 255), -1)
            

            
            img_fun=opt(im_ROI2,45,(xn,yn)  )
            
            img_arr.append(img_fun)
            
    if (isinstance(img_arr[0], str) and img_arr[0] =='STOP'):
        print("object detected ,check ranger to decide now")

        return "Ranger"

    #cv2.cvtColor(im2,cv2.COLOR_GRAY2RGB)
    while True and (isinstance(img_arr[0], str)==False):
            cv2.imshow('Features',gray )
            cv2.imshow('Features0',img_arr[0] )
            cv2.imshow('Features1',img_arr[1] )
            if cv2.waitKey(1)& 0xFF == ord('q'):
                break

    cv2.destroyAllWindows()
    


def opt(im2,max_lin,(xc,yc)):
    try:
        
        img=im2
        img=cv2.circle(img, (xc , (2*yc) ), 4, (0, 0, 255), -1)
        dimen=img.shape
        print(dimen)
        print('$$$$$$',xc,yc )
        
        ret,thresh = cv2.threshold(img,max_lin ,255,0)
        contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0,len(contours)):
            cnt = contours[i]
            M = cv2.moments(cnt)
            if(M["m00"] != 0 and cv2.contourArea(cnt)<18000 and cv2.contourArea(cnt)>250):
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                perimeter = cv2.arcLength(cnt,True)
                #epsilon = 0.1*perimeter
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)#
                #print(list(a)[0],list(b)[0],list(c)[0],list(d)[0])

                listy = []
                for row in range(4):
                    
                    if(xc==320 and yc==50 and row>0):
                        return "STOP"

                    inner_list = []
                    for col in range(2):
                        inner_list.append(box[row][col])
                        #print(inner_list[col][row])\

                    print(inner_list[0])
                    print(inner_list[1])
                    #cv2.putText(img,str(int(inner_list[0]))+'.'+str(int(inner_list[1])),(inner_list[0], inner_list[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
                    listy.append(inner_list)

                print("tjos/n",listy)
                #box = np.int0([a][b][c][d])
                #box=[[k for row in list(a)] for column in range(4)]
                #print([box])
                
                #im = cv2.drawContours(im2,list_of_lists,0,(0,255,0),2)#[[a][b][c][d]]
                for i in range(4):
                    #pnt_arr=[]
                    '''
                    THIS IS IMPORTANT
                    im=cv2.line(img, tuple(listy[i]), tuple(listy[(i + 1) % 4]), (0,255,0), 2, cv2.LINE_AA, 0)
                    '''
                    if(i==0 or i==3):
                        s,slope= dist(xc,(2*yc),listy[i])
                        
                    im=cv2.line(img, tuple((xc,(2*yc))), tuple(listy[i]), (0,255,0), 2, cv2.LINE_AA, 0)
                    #im=cv2.putText(img,str(s),(inner_list[0], inner_list[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
                    while True:
                        cv2.imshow('slope',img )
                        if cv2.waitKey(1)& 0xFF == ord('q'):
                            break
                    cv2.destroyAllWindows()
                    
                    #im =cv2.line(im2,(listy),(x2,y2),(0,0,255),2)

                im=cv2.circle(img, (xc , (2*yc) ), 4, (0, 0, 255), -1)
                print( (cX  , cY),"area: ",cv2.contourArea(cnt),"perimeter:",perimeter)
                
                
                #cv2.circle(im, (cX, cY), 4, (0, 0, 255), -1)
                '''
                cv2.putText(im,str(cv2.contourArea(cnt)),(cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,255), 2, cv2.LINE_AA)
                '''
                #fromCenter = False
                #ROIs = cv2.selectROIs('Select ROIs', im, showCrosshair=False,fromCenter)
                #im=im[int(dimen[0])-125:int(dimen[0])-25, int(dimen[1])-450:int(dimen[1])-50]
                #approx = cv2.approxPolyDP(cnt,epsilon,True)
                #print(approx,i)
                #cv2.drawContours(im, [cnt],-2,(0,255,0))
                '''


                print("0:shape",img.shape,"shape(b):",dimen,int(dimen[0])-125,int(dimen[0])-25, int(dimen[1])-680,int(dimen[1])-50)

                print("1:shape",im.shape,int(dimen[0])-125,int(dimen[0])-25, int(dimen[1])-680,int(dimen[1])-50)
                #print("2:shape",im3.shape,int(dimen[0])-300,int(dimen[0])-100, int(dimen[1])-640,int(dimen[1])-80)
                '''
         

        return  img
 
    except (KeyboardInterrupt, SystemExit):
        return 'exiting'
    
def dist(xc,yc,lin_arr):
    
    distance =math.sqrt( ((xc -lin_arr[0])**2)+((yc -lin_arr[1])**2) )
    
    #m=0
    #m=int((yc-lin_arr[0])/(xc-lin_arr[1]) )
    #slope=math.degrees(math.atan(m))+45
    slope=''
    if (int(yc-lin_arr[1]) <40):
        print("distance",distance,xc,yc,lin_arr,"movement:","STOP")
        return distance,("STOP")
    if lin_arr[0]>xc:
        slope='LEFT'        
        print("go LEFT")
    if lin_arr[0]<xc:
        slope='RIGHT'
        print("go RIGHT")
    print("distance",distance,xc,yc,lin_arr,"movement:",(slope))

    return distance,(slope)

def ranging():
    print("ranging function starts")
  
'''
image=hi()
if( image=="Ranger"):
    ranger= ranging()'''
#https://docs.opencv.org/3.4/opencv.js
num_eg()

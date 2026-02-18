import cv2

photo=input("Enter the filename: ")
img=cv2.imread(photo)
if img is not None:
    
    while(1):
        choice=int(input("1. Draw a line\n2. Draw a rectangle\n3. Draw a circle\n4. Add text\n5. Exit\nEnter your choice:    "))
        if choice == 1:
            pt1x=int(input("Enter the x coordinate of the first point: "))
            pt1y=int(input("Enter the y coordinate of the first point: "))
            pt1=(pt1x,pt1y)
            pt2x=int(input("Enter the x coordinate of the second point: "))
            pt2y=int(input("Enter the y coordinate of the second point: "))
            pt2=(pt2x,pt2y)
            thick=int(input("Enter the thickness of the line: "))
            cv2.line(img,pt1,pt2,(125,125,3),thick)
            c=input("Type 'SEE' to see the edited photo\nType'SAVE' to save the pic\nType'SS' to see and save the pic\nType:   ")
            if c.lower() =='see':
                cv2.imshow("PHOTO",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif c.lower() =='save':
                cv2.imwrite("Linephoto.jpg",img)
            
            elif c.lower() =='ss':
                cv2.imshow("PHUTU",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite("Linephoto.jpg",img)
            img=cv2.imread(photo)
        elif choice == 2:
            pt1x=int(input("Enter the x coordinate of the first corner: "))
            pt1y=int(input("Enter the y coordinate of the first corner: "))
            pt1=(pt1x,pt1y)
            pt2x=int(input("Enter the x coordinate of the second corner: "))
            pt2y=int(input("Enter the y coordinate of the second corner: "))
            pt2=(pt2x,pt2y)
            thick=int(input("Enter the thickness of the line: "))
            
            cv2.rectangle(img,pt1,pt2,(125,125,3),thick)
            c=input("Type 'SEE' to see the edited photo\nType'SAVE' to save the pic\nType'SS' to see and save the pic\nType:   ")
            if c.lower() =='see':
                cv2.imshow("PHoto",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif c.lower() =='save':
                cv2.imwrite("Rectanglephoto.jpg",img)
            
            elif c.lower() =='ss':
                cv2.imshow("PHUTU",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite("Rectanglephoto.jpg",img)
            img=cv2.imread(photo)
           
        elif choice == 3:
            pt1x=int(input("Enter the x coordinate of the center: "))
            pt1y=int(input("Enter the y coordinate of the center: "))
            pt1=(pt1x,pt1y)
            thick=int(input("Enter the thickness of the line: "))
            
            cv2.circle(img,pt1,50,(125,125,3),thick)
            c=input("Type 'SEE' to see the edited photo\nType'SAVE' to save the pic\nType'SS' to see and save the pic\nType:   ")
            if c.lower() =='see':
                cv2.imshow("PHOTO",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif c.lower() =='save':
                cv2.imwrite("Circlephoto.jpg",img)
            
            elif c.lower() =='ss':
                cv2.imshow("PHUTU",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite("Circlephoto.jpg",img)
            img=cv2.imread(photo)
           
        elif choice==4:
            pt1x=int(input("Enter the x coordinate of the center: "))
            pt1y=int(input("Enter the y coordinate of the center: "))
            pt1=(pt1x,pt1y)
            text=input("What's in your mind?")
            cv2.putText(img,text,pt1,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2.0,(125,125,3),1)
            c=input("Type 'SEE' to see the edited photo\nType'SAVE' to save the pic\nType'SS' to see and save the pic\nType:   ")
            if c.lower() =='see':
                cv2.imshow("PHOTO",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif c.lower() =='save':
                cv2.imwrite("textphoto.jpg",img)
            
            elif c.lower() =='ss':
                cv2.imshow("PHUTU",img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                cv2.imwrite("Textphoto.jpg",img)
            img=cv2.imread(photo)
        elif choice==5:
            print("Thanks")
            break


else:
    print("Image not loaded succesfully")
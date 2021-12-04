def getfiles(newpath):
    #push button up again
    #newpath=path+"/"+dir
    print ("selected path",newpath)
    #filelist=[]
    if not os.listdir(newpath):
        print(f'Try another - that folder {dir} is empty')#messagebox should pop up to display this
        return
    else:
        files=os.listdir(newpath)
        for file in files:
            #print(file,'in files')
            filetype(newpath,file)
            #filelist.append(file)
    cv.destroyAllWindows()
    return

def diff(image1,image2):
    difference= cv2.subtract(image1,image2)
    #print("Difference equals ",np.sum(difference))
    result=not np.any(difference) # differewnce is all zeros it will return false
    w,h,c=difference.shape
    total_pixel_value_count=w*h*c*255  # Find the silimarity between this images %
    percentage_match=(total_pixel_value_count -np.sum(difference))/total_pixel_value_count*100
    #print(percentage_match)
    if result is True:
        print (f"the images ("+image1+" and "_image2+") are {percentage_match} the same")
    else:
        res="result"+str(i)+".jpg"
        #cv2.imwrite(res, difference)
        print (f"The images ("+image1+" and "_image2") are {percentage_match} different")
        i=i+1
    return
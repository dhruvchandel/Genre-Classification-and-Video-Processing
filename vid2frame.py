# Program To Read video 
# and Extract Frames 
import cv2
  
# Function to extract frames 
def ExtractFrames(path) :
      
    # Assigning an object to the video for it's processing
    vidObj = cv2.VideoCapture(path) 
    
    # Used as counter variable to name extracted Images 
    count = 0
      
    # Loop terminating variable(checks whether frames were extracted) 
    success = 1
      
    while success: 
      
        # The func. below is used to seek frame ot a particular time frame
        vidObj.set(cv2.CAP_PROP_POS_MSEC,count*1000)
        '''
        For setting Frame rate :
            count*1000 represents the default frame rate for the program which is 1 FPS
            For changing the frame rate to 'n' FPS ;
            count*1000 can be replaced by count*1000/n according to your needs
        '''
        
        # vidObj object calls read , it returns image to store it in the variable
        # image and also return True/False , so when video end loop terminates   
        success, image = vidObj.read() 
        
        # Saves the frames at the address with frame-count 
        cv2.imwrite("/Users/dhruvchandel/Desktop/trailer/ExtractedFrames/frame%d.jpg" % count, image) 
        '''
            Inside imwrite you can replace "/Users/dhruvchandel/Desktop/trailer/ExtractedFrames"
            by the address where you want to store your extracted frames from the video
        '''
      
        count += 1

ExtractFrames('/Users/dhruvchandel/Desktop/trailer/trailer1.mp4')

'''
    Above Function contains Source Video whose frames are to be extracted
'''
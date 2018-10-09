# Logo Detection

**Instructions for use**

Run the logo_detection.py script with the name of the imput image to classify it into one of the six bank options
```
   ['Bank Of America', 'Wells Fargo', 'JPMorgan Chase', 'Citigroup Inc', 'Capital One', 'Other']
   ```

The path to the image can be passed in as a command line argument. Either the complete path can be given or the filename of the image can be given (this will check in the images folder).

Example
   ```
   python3 logo_detection.py bank_of_america.jpg
   # OR
   python3 logo_detection.py bank_of_america_statement_page_1.jpg
   ```

I have experimented with various algorithms:
1. OCR -- This was a total bust. The text read was random gibberish. I tried this using pytesseract in combination with OpenCV.
2. Neural Nets -- There are a lot of problems with this approach. 
 -- First and for most the data is too less to be trained with a neural network.
 -- Second the dimensions of the images need to be consistent. If only the "headers" (documents) are considered then it could be done by resizing all the images to a predefined size, but that still leaves the problem of training the network which needs more data.
3. Template Matching -- This seemed like the best possible option given the circumstances. This was a much quicker apprach that training models since we had only 6 banks to classify. The basic idea is to see if a given template matches in the image or not. 

**Approach**
1. The algorithm first create a matrix of the image and converts it to Gray Scale. Conversion to Gray Scale is done so that the templates do not get confused because of the colors. I have tried using colored images but that creates a lot of false matches. Captiol One is matching with Bank of America since there is a red band in both the logos. 
2. Same procedure is followed for the template. It will do this for all the templates in the template folder. This folder has images with templates to match. I have created these templates from various images obtained from Google Images, the official websites etc. After a lot of trial and error I realized that these images had to be much smaller than the images so I had to spend a lot of time cropping and resizing the templates to get a good match.
3. The cv2.matchTemplate is the main crux of this algorithm. It creates a block of the template and slides it over the gray image to figure out if there is a match or not. Most of the templates have a match in all the images, this is where the threshold come into picture. It sets a minimum threshold for the matches. Majority of my time has been spent fine tuning these thresholds so that they work well with the header files. The ```parameter_tuning``` function is where the fine tuning happens.
4. Finally if it finds a point above the threshold then it will classify the image for that bank.

**Pros** 
1. This approach is fast since there is no training involved. 
2. No need for resizing every image. Only needed when the template image bigger than the image to be tested.

**Cons** 
1. A lot of preprocessing is required for creating the templates.
2. The templates need to be in the approximately the same size as the logo in the image for a good match.

**Improvements**

I would love to try a neural network approach since it would be definetly a better approach than template matching, given more data. 
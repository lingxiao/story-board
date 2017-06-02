This is a simple script that exploits the Tinder API to allow a person to build a facial dataset. 
 
## Inspiration 
 
Having worked with facial datasets in the past, I have often been disappointed.  The datasets tend to be extremely strict in their structure, and are usually too small.  Tinder gives you access to thousands of people within miles of you.  Why not leverage Tinder to build a better, larger facial dataset? 
 
## Running The Script 
 
To run the script tinderGetPhotos.py, one must first do the following: 
 
1.  Download the Tinder app, create a profile, and get it up and running. 
2.  Create a folder to which the scraped photos will be saved.  Then fill in the imagePath variable in the script. 
3.  Get your FaceBook ID from https://findmyfbid.in/.  Then fill in the facebook_id variable in the script. 
4.  Get your FaceBook token by clicking [here](https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd). Click Ok, and then look in the response to the POST request https://www.facebook.com/v2.6/dialog/oauth/confirm?dpr=1.  One way to see the response to the POST request is to open Developer Tools in Google Chrome prior to clicking Ok, and navigating to the Network tab.  In the response, one's token will be the string sandwiched between `&access_token=` and `&expires_in=`.  Fill in the facebook_token variable in the script. 
 
## The Dataset 
 
I have used this script to create a dataset of 20,000 male and female individuals.  ~~This dataset can be found [here](https://www.kaggle.com/scolianni/people-of-tinder) on Kaggle.~~

**UPDATE:**  I have spoken with representatives at Kaggle, and they have received a request from Tinder to remove the dataset.  As such, the facial data set previously hosted on Kaggle has been removed.  A TechCrunch article about the dataset in question can be found [here](https://techcrunch.com/2017/04/28/someone-scraped-40000-tinder-selfies-to-make-a-facial-dataset-for-ai-experiments/).

## Additional Information

- The use of the words `hoe` and `hoes` as data structures within the original script was an oversight.  This syntax was borrowed from a [Tinder auto-liker](https://github.com/jaungiers/Tinder-py_auto_liker), which I used as a reference when learning to interact with the Tinder API programmatically.  I regret this oversight, and the code has been corrected.
- The [Tinder API Documentation]( https://gist.github.com/rtt/10403467) has been available to the public for years, and there are numerous open source projects on GitHub such as [Pynder]( https://github.com/charliewolf/pynder) showing how to make Tinder bots and interact with the Tinder API.  
 
## Future Work 
 
I plan on using the aforementioned dataset with TensorFlow's Inception to try and create a CNN that is capable of distinguishing between men and women.

**UPDATE:**  I have created a CNN capable of classifying men and women with 86.5% accuracy.  This CNN was trained without using any images scraped from Tinder.  The code for this project can be found in the [GenderClassifierCNN](https://github.com/scoliann/GenderClassifierCNN) repository.
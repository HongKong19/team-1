import requests
import json
from credentials import getCredentials

# set to your own subscription key valuedir
subscription_key = getCredentials() #hidden due to sensitive info
assert subscription_key

# replace <My Endpoint String> with the string from your endpoint URL
face_api_url = "https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect"
#face_api_url = 'https://codeforgood.cognitiveservices.azure.com/face/v1.0'



headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}



#print(emotions)

neg_emotions = ["anger","contempt","fear","sadness", "surprise", "disgust"]


def getSentiment(img_url):
    image_url = img_url
    response = requests.post(face_api_url, params=params,
                             headers=headers, json={"url": image_url})
    response = json.loads(json.dumps(response.json()))
    emotions = response[0]["faceAttributes"]["emotion"]
    sum = 0;
    for i in emotions:
        if(i in neg_emotions):
            sum+=emotions[i]
    return (sum/6)
    #detected_emotions.append(str(i)+": "+str(emotions[i]))
#print(getSentiment('https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'))
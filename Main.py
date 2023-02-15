from pytube import YouTube
from moviepy.editor import *
import os
urlList = []
importVideo = 1
gifPrompt = 1 
counter = 0

projectName = input("Please input Project name: ")
print("Please type 'Done' to move onto the next Steps")

while(importVideo == 1):
    url = input("Please input URL: ")
    if url == "Done":
        break
    yt = YouTube(url)
    print("Downloading: ", yt.title)
    ys = yt.streams.get_highest_resolution()
 
    fileNumber = str(counter)
    # ys.download("Videos",filename=projectName+fileNumber)
    # downloadedVideo = "C:/Users/danie/Desktop/Content Farm/Videos/" + projectName+fileNumber+ ".mp4"
    # urlList.append(downloadedVideo)
    # print("Stored: ", urlList)
    # print("counter: ", counter)
    # counter = counter + 1
    # if counter == 13:
    #     break

# if counter == 1:
#     vid1 = VideoFileClip(urlList[0])

#     final_Vid = concatenate_videoclips([vid1],method='compose')
# if counter == 2:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])

#     final_Vid = concatenate_videoclips([vid1,vid2],method='compose')
# if counter == 3:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3],method='compose')
# if counter == 4:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4],method='compose')
# if counter == 5:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5],method='compose')
# if counter == 6:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])
#     vid6 = VideoFileClip(urlList[5])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6],method='compose')
# if counter == 7:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])
#     vid6 = VideoFileClip(urlList[5])
#     vid7 = VideoFileClip(urlList[6])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6,vid7],method='compose')
# if counter == 8:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])
#     vid6 = VideoFileClip(urlList[5])
#     vid7 = VideoFileClip(urlList[6])
#     vid8 = VideoFileClip(urlList[7])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6,vid7,vid8],method='compose')
# if counter == 9:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])
#     vid6 = VideoFileClip(urlList[5])
#     vid7 = VideoFileClip(urlList[6])
#     vid8 = VideoFileClip(urlList[7])
#     vid9 = VideoFileClip(urlList[8])


#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6,vid7,vid8,vid9],method='compose')
# if counter == 10:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])
#     vid6 = VideoFileClip(urlList[5])
#     vid7 = VideoFileClip(urlList[6])
#     vid8 = VideoFileClip(urlList[7])
#     vid9 = VideoFileClip(urlList[8])
#     vid10 = VideoFileClip(urlList[9])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6,vid7,vid8,vid9,vid10],method='compose')
# if counter == 11:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])
#     vid6 = VideoFileClip(urlList[5])
#     vid7 = VideoFileClip(urlList[6])
#     vid8 = VideoFileClip(urlList[7])
#     vid9 = VideoFileClip(urlList[8])
#     vid10 = VideoFileClip(urlList[9])
#     vid11 = VideoFileClip(urlList[10])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6,vid7,vid8,vid9,vid10,vid11],method='compose')
# if counter == 12:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])
#     vid6 = VideoFileClip(urlList[5])
#     vid7 = VideoFileClip(urlList[6])
#     vid8 = VideoFileClip(urlList[7])
#     vid9 = VideoFileClip(urlList[8])
#     vid10 = VideoFileClip(urlList[9])
#     vid11 = VideoFileClip(urlList[10])
#     vid12 = VideoFileClip(urlList[11])

#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6,vid7,vid8,vid9,vid10,vid11,vid12],method='compose')
# if counter == 13:
#     vid1 = VideoFileClip(urlList[0])
#     vid2 = VideoFileClip(urlList[1])
#     vid3 = VideoFileClip(urlList[2])
#     vid4 = VideoFileClip(urlList[3])
#     vid5 = VideoFileClip(urlList[4])
#     vid6 = VideoFileClip(urlList[5])
#     vid7 = VideoFileClip(urlList[6])
#     vid8 = VideoFileClip(urlList[7])
#     vid9 = VideoFileClip(urlList[8])
#     vid10 = VideoFileClip(urlList[9])
#     vid11 = VideoFileClip(urlList[10])
#     vid12 = VideoFileClip(urlList[11])
#     vid13 = VideoFileClip(urlList[12])
    
#     final_Vid = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6,vid7,vid8,vid9,vid10,vid11,vid12,vid13],method='compose')

# final_Vid.write_videofile("hi.mp4",fps=1)


# gif = input("Please input gif file name: ")
# gif = gif + ".gif"
# print("Please type 'Done' to move onto the next Steps. Max 5 GIFs.")
# counter = 0
# gifArray = []

# while gifPrompt:
#     if counter == 6:
#         break
#     gif = input("Please input gif name: ")
#     if gif == "Done":
#         break
#     gif = "C:/Users/danie/Desktop/Content Farm/gif/" + gif + ".gif"
#     gifArray.append(gif)
#     print("Stored: ", gifArray)
#     if gif == "Done":
#         break
#     counter = counter + 1

# if counter == 1:
#     vid1 = VideoFileClip(gifArray[0])
#     final_gif = concatenate_videoclips([vid1],method='compose')
# if counter == 2:
#     vid1 = VideoFileClip(gifArray[0])
#     vid2 = VideoFileClip(gifArray[1])
#     final_gif = concatenate_videoclips([vid1,vid2],method='compose')
# if counter == 3:
#     vid1 = VideoFileClip(gifArray[0])
#     vid2 = VideoFileClip(gifArray[1])
#     vid3 = VideoFileClip(gifArray[2])
#     final_gif = concatenate_videoclips([vid1,vid2,vid3],method='compose')
# if counter == 4:
#     vid1 = VideoFileClip(gifArray[0])
#     vid2 = VideoFileClip(gifArray[1])
#     vid3 = VideoFileClip(gifArray[2])
#     vid4 = VideoFileClip(gifArray[3])
#     final_gif = concatenate_videoclips([vid1,vid2,vid3,vid4],method='compose')
# if counter == 5:
#     vid1 = VideoFileClip(gifArray[0])
#     vid2 = VideoFileClip(gifArray[1])
#     vid3 = VideoFileClip(gifArray[2])
#     vid4 = VideoFileClip(gifArray[3])
#     vid5 = VideoFileClip(gifArray[4])
#     final_gif = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5],method='compose')
# if counter == 5:
#     vid1 = VideoFileClip(gifArray[0])
#     vid2 = VideoFileClip(gifArray[1])
#     vid3 = VideoFileClip(gifArray[2])
#     vid4 = VideoFileClip(gifArray[3])
#     vid5 = VideoFileClip(gifArray[4])
#     vid6 = VideoFileClip(gifArray[5])
#     final_gif = concatenate_videoclips([vid1,vid2,vid3,vid4,vid5,vid6],method='compose')

# final_gif.write_gif("combinedGIF.gif", fps=10)

# audio = AudioFileClip("hi.mp4")
# # Import the Image and set its duration same as the audio (Insert the location of your photo instead of photo.jpg)
# print("Audio File Found")
# test = audio.duration/VideoFileClip("C:/Users/danie/Desktop/Content Farm/combinedGIF.gif").duration
# clip = VideoFileClip("C:/Users/danie/Desktop/Content Farm/combinedGIF.gif").loop(n=test)
# print("Clip File Found")
# # Set the audio of the clip
# clip = clip.set_audio(audio)
# # # Export the clip
# clip.write_videofile("hi" + ".mp4", fps=10)

# os.remove("C:/Users/danie/Desktop/Content Farm/finalVid1.mp4")
# os.remove("C:/Users/danie/Desktop/Content Farm/combinedGIF.gif")



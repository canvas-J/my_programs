# import imageio
# imageio.plugins.ffmpeg.download() # C:\Users\gang\AppData\Local\imageio\ffmpeg\ffmpeg-win32-v3.2.4.exe
import moviepy.editor as mpy

#视频文件的本地路径
content = mpy.VideoFileClip("C:/Users/gang/Videos/20190208_113719.mp4")
# 剪辑78分55秒到79分6秒的片段。注意：不使用resize则不会修改清晰度 
c1 = content.subclip((00,00),(00,16)).resize((600,400))
c1.write_gif("gav.gif")
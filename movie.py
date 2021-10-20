from moviepy.editor import *


def write_text():
    clip = VideoFileClip(r"C:\Users\abdul\Desktop\Python Videos\1.mp4")
    # Generate a text clip. You can customize the font, color, etc.
    txt_clip = TextClip("Testing text edit", fontsize=70, color='white')

    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_pos('center').set_duration(clip.duration)

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, txt_clip])

    # Write the result to a file (many options available !)
    video.write_videofile("1_edited.mp4")


def speed():
    clip = VideoFileClip(r"C:\Users\abdul\Desktop\Python Videos\1.mp4")

    # getting only first 5 seconds
    clip = clip.subclip(0, 5)

    # applying speed effect
    final = clip.fx(vfx.speedx, 0.5)

    # showing final clip
    final.write_videofile("1_edited.mp4")

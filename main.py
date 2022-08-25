from pytube import YouTube

def ytmp4():
  try:
    yt4 = input("Masukkan Link YT [MP4]: ")
    print("please wait... Don't close!")
    YouTube(yt4).streams.filter(file_extension='mp4').first().download()
    print("Done!")
  except:
    print("Input Salah!")


def ytmp3():
  try:
    yt3 = input("Masukkan Link YT [MP3]: ")
    print("please wait... Don't close!")
    YouTube(yt3).streams.filter(only_audio=True).first().download()
    print("Done!")
  except:
    print("Input Salah!")

  
print("__  ________    ____  __ ")
print("\ \/ /_  __/   / __ \/ / ")
print(" \  / / /_____/ / / / /  ")
print(" / / / /_____/ /_/ / /___")
print("/_/ /_/     /_____/_____/")
print()
print("yt-dl v1.1 By IbrahLynx")
print()
print("[1] Format MP4")
print("[2] Format MP3")
print()

format = input("Pilih Format: ")

if format == "1":
  ytmp4()
elif format == "2":
  ytmp3()
else:
  print("Input Salah!")

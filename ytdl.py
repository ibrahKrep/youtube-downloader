from pytube import YouTube

def ytmp4(link):
  try:
    YouTube(link).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first().download()
  except:
    print("Input Salah!")

def ytmp3(link):
  try:
    YouTube(link).streams.filter(progressive=True, file_extension='mp3').order_by('resolution').first().download()
  except:
    print("Input Salah!")
  
print("__  ________    ____  __ ")
print("\ \/ /_  __/   / __ \/ / ")
print(" \  / / /_____/ / / / /  ")
print(" / / / /_____/ /_/ / /___")
print("/_/ /_/     /_____/_____/")
print()
print("yt-dl v1.0 By IbrahLynx")
print()

try:
  url = input("Silahkan Masukan Link: ")
  print("Pilih Format ")
  print("[1] Format MP4")
  print("[2] Format MP3")
  format = input("pilih format :")
  if format == "1":
    ytmp3(url)
  else format == "2":
    ytmp3(url)
  else:
    print("Input Salah!")
except:
    print("Input Salah!")

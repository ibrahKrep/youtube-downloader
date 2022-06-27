from pytube import YouTube

def ytmp4(link):
  try:
    print("Sedang Mendownload...")
    YouTube(link)
    .streams
    .filter(progressive=True, file_extension="mp4")
    .order_by('resolution')
    .first()
    .download()
  except:
    print("Input Salah!")
  
def ytmp3(link):
  try:
    print("Sedang Mendownload...")
    YouTube(link)
    .streams
    .filter(progressive=True, file_extension="mp3")
    .order_by('resolution')
    .first()
    .download()
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
print("Pilih Format ")
print("[1] Format MP4")
print("[2] Format MP4")
print()

format = input("Pilih Format: ")

if format == "1":
  ytmp4()
else format == "2":
  ytmp3()
else:
  print("Input Salah!")

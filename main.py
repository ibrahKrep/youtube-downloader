from pytube import YouTube, exceptions

def ytmp4():
  try:
    yt4 = input("Masukkan Link YT [MP4]: ")
    if(not yt4):
      print("URL Harus diisi!")
      exit(255)

    print("Mohon tunggu...")
    dl = YouTube(yt4)
    author = dl.author
    title = dl.title
    keywords = ", ".join(dl.keywords)
    publish = dl.publish_date
    publish = str(publish.year) + "-" + str(publish.month).zfill(2) + "-" + str(publish.day).zfill(2)
    views = dl.views
    print("\n")
    print(f"Pembuat : {author}\nJudul : {title}\nKata kunci : {keywords}\nDiupload : {publish}\nPenonton : {views}")
    print("\n")
    dl.streams.filter(file_extension="mp4").first().download()
    print("Selesai!")
  except SystemExit as e:
    if(e.code == 255):
      raise
    else:
     print("Exited with code", e.code)
  except exceptions.VideoUnavailable:
    print("Video tidak ditemukan!")
  except exceptions.RegexMatchError:
    print("URL Tidak valid atau tidak didukung!")
  except KeyboardInterrupt:
    print("Canceled")
  except EOFError:
    print("Canceled")
  except:
    print("Error!")


def ytmp3():
  try:
    yt3 = input("Masukkan Link YT [MP3]: ")
    if(not yt3):
      print("URL Harus diisi!")
      exit(255)

    print("Mohon tunggu...")
    dl = YouTube(yt3)
    author = dl.author
    title = dl.title
    keywords = ", ".join(dl.keywords)
    publish = dl.publish_date
    publish = str(publish.year) + "-" + str(publish.month).zfill(2) + "-" + str(publish.day).zfill(2)
    views = dl.views
    print("\n")
    print(f"Pembuat : {author}\nJudul : {title}\nKata kunci : {keywords}\nDiupload : {publish}\nPenonton : {views}")
    print("\n")
    dl.streams.filter(only_audio=True).first().download()
    print("Selesai!")
  except SystemExit as e:
    if(e.code == 255):
      raise
    else:
     print("Exited with code", e.code)
  except exceptions.VideoUnavailable:
    print("Video tidak ditemukan!")
  except exceptions.RegexMatchError:
    print("URL Tidak valid atau tidak didukung!")
  except KeyboardInterrupt:
    print("Canceled")
  except EOFError:
    print("Canceled")
  except:
    print("Error!")


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

try:
  format = input("Pilih Format: ")

  if format == "1":
    ytmp4()
  elif format == "2":
    ytmp3()
  else:
    print("Input Salah!")
except KeyboardInterrupt:
  print("Canceled")
except EOFError:
  print("Canceled")

import yt_dlp

channels = {
    'boundless':   'https://www.youtube.com/@BoundlessEntertainmentFilms/videos',
    'blackeye':    'https://www.youtube.com/@BlackEyeTechnologies/videos',
    'polygonflow': 'https://www.youtube.com/@polygonflow/videos',
}

opts = {
    'quiet': True,
    'extract_flat': True,
    'skip_download': True,
}

for name, url in channels.items():
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=False)
        entries = info.get('entries', [])
        print("=== " + name + " (" + str(len(entries)) + " videos) ===")
        for e in entries:
            vid_id = e.get('id', '')
            title  = e.get('title', '')
            print(vid_id + "|||" + title)

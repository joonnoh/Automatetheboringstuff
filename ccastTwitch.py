#!/usr/bin/env python
# In progress:
# Python script to Chromecast Twitch.tv

import time
import pychromecast

# Run in Python interpreter to list chromecasts on the network, but don't connect
# services, browser = pychromecast.discovery.discover_chromecasts()
# Shut down discovery
# pychromecast.discovery.stop_discovery(browser)

# Discover and connect to chromecasts named Living Room
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Living Room TV"])
[cc.device.friendly_name for cc in chromecasts]
#['Living Room TV']

cast = chromecasts[0]
# Start worker thread and wait for cast device to be ready
cast.wait()
#print(cast.device)
#DeviceStatus(friendly_name='Living Room TV', model_name='Chromecast', manufacturer='Google Inc.', uuid=UUID('a8ca9b5e-0d6b-e5c8-1924-5015c213a5d0'), cast_type='cast')

#print(cast.status)
#CastStatus(is_active_input=True, is_stand_by=False, volume_level=1.0, volume_muted=False, app_id='CC1AD845', display_name='Default Media Receiver', namespaces=['urn:x-cast:com.google.cast.player.message', 'urn:x-cast:com.google.cast.media'], session_id='CCA39713-9A4F-34A6-A8BF-5D97BE7ECA5C', transport_id='web-9', status_text='')

mc = cast.media_controller
mc.play_media('https://www.twitch.tv/cohhcarnage', 'video/mp4')
#mc.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', 'video/mp4')
mc.block_until_active()
print(mc.status)
#MediaStatus(current_time=42.458322, content_id='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4', content_type='video/mp4', duration=596.474195, stream_type='BUFFERED', idle_reason=None, media_session_id=1, playback_rate=1, player_state='PLAYING', supported_media_commands=15, volume_level=1, volume_muted=False)

#mc.pause()
#time.sleep(5)
#mc.play()

# Shut down discovery
#pychromecast.discovery.stop_discovery(browser)

# TODOS


## Features
- Add option to provide graphical border/padding to captured image
- option to do screen rect   -R<x,y,w,h> capture screen rect
-v capture video recording of the screen !!!

  -v        capture video recording of the screen
  -V<seconds> limits video capture to specified seconds
  -A<id>    captures audio during a video recording using default input. Optional specify the id of the audio source

-a/--alt-text: add alt text to HTML output and to file metadata
--meta add metadata:
    - taken with screencappy
    - timestamp
    - alt text

--scale w,h
    --scale -1,30      30% height
    --scale 80,90,px   reduce to 80x90px
    --scale 130,-1,pct scale to 130% of width

### variations
- black-white copy
- thumbnail
- framed
- low-quality


## Design
- There should be in Image class that wraps around Pillow image?

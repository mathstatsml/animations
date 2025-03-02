# Getting Started

1. Windows 11 (other operating systems should work, but you will not be able to run Step 21 providing LaTeX in subcaptions)
2. Python 3.9.13
3. Vapoursynth R57
4. VSCode
5. Git
6. uv
7. manim
8. A working LaTeX installation like MikTeX
  - Run MikTeX update
9. ffmpeg
  - add ffmpeg binary to path
10. Clone repo
11. Create .env file, following .env.example and paste your Eleven Labs API Key
12. `uv venv --python 3.9`
13. .\.venv\Scripts\activate
14. uv pip install -r pyproject.toml
15. uv pip install "numpy==1.23.5"
16. cd demo
17. manim -pqh .\main.py Demo
18. Create folder demo/processing/assets and drag Demo.mp4, Demo.srt, and Demo.wav into there
  - These files are located in demo/media/videos/main/1080p60
19. cd into demo/processing
20. python subtitles.py
21. Go into export.vpy and run the 4 commented-out commands at the bottom of the file

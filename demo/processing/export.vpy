import vapoursynth as vs # type: ignore
core = vs.core
core.std.LoadPlugin(path="VSFilterMod.dll")
core.std.LoadPlugin(path="BestSource.dll")

# Paths should be changed as appropriate
video = core.bs.VideoSource(source='./assets/Demo.mp4')
subtitled_video = core.vsfm.TextSubMod(video, './assets/Demo.ass')
subtitled_video.set_output()

# Paths should be changed as appropriate
# vspipe -c y4m .\export.vpy .\assets\temp.raw
# ffmpeg -i .\assets\temp.raw .\assets\temp.mp4
# ffmpeg -i .\assets\temp.mp4 -i .\assets\Demo.wav -c:v copy -c:a copy ..\output.mp4
# rm .\assets\ -r -force
import vapoursynth as vs # type: ignore
core = vs.core
core.std.LoadPlugin(path="VSFilterMod.dll")
core.std.LoadPlugin(path="BestSource.dll")

# replace
path_to_media = "../_template/media/"

# file names should be changed as appropriate
video = core.bs.VideoSource(source=f'{path}videos/main/1080p60/Template.mp4')
subtitled_video = core.vsfm.TextSubMod(video, f'{path}Template.ass')
subtitled_video.set_output()

# Paths should be changed as appropriate
# vspipe -c y4m ./export.vpy <path>temp.raw
# ffmpeg -i <path>temp.raw <path>temp.mp4
# ffmpeg -i <path>temp.mp4 -i <path>videos/main/1080p60/Template.wav -c:v copy -c:a copy <path>output.mp4
# export output.mp4 to YouTube
# rm <path> -r -force
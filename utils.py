def calculate_clip_end(clip_start, clip_duration, large_video_duration):
    return clip_start + clip_duration if clip_start + clip_duration < large_video_duration else large_video_duration

from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from utils import calculate_clip_end
import os
import time
import toml


if __name__ == '__main__':
    config = toml.load('config.toml')
    file = config['file']
    size = (config['size'][0], config['size'][1])
    clip_duration = config['clip_duration']
    text_prefix = config['text_prefix']
    bottom_text = config['bottom_text']

    results_dir = 'results/'
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        print(f'Created {results_dir} directory')

    large_video = VideoFileClip(file)
    clips_processed_total_duration = 0
    clips_processed = 0

    while clips_processed_total_duration < large_video.duration:
        j = clips_processed + 1

        clip_start = clips_processed * clip_duration
        clip_end = calculate_clip_end(clip_start, clip_duration, large_video.duration)

        clip_text = TextClip(f' {text_prefix} {j} ', fontsize=70, color='black', bg_color='white')
        clip_bottom_text = TextClip(
            bottom_text, fontsize=config['bottom_text_fontsize'], color='black', bg_color='white'
                                    )

        clip = large_video.subclip(clip_start, clip_end)
        clip = clip.resize(width=size[0])
        clip_text = clip_text.set_position(('center', size[1] * .1)).set_duration(clip.duration)
        clip_bottom_text = clip_bottom_text.set_position(
            ('center', size[1] * config['bottom_text_y_position'])
        ).set_duration(clip_duration)
        clip = clip.set_position(('center', 'center'))

        final_clip = CompositeVideoClip(
            [clip, clip_text, clip_bottom_text],
            size=size,
            bg_color=(0, 0, 0)
        )

        if config['test']:
            final_clip.save_frame('results/test.png')
        else:
            final_clip.write_videofile(f'results/{time.time()}_clip_{j}.mp4', codec='libx264')

        clips_processed_total_duration += clip.duration
        clips_processed += 1

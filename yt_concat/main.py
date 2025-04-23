from yt_concat.pipeline.steps.get_videos import GetVideoList
from yt_concat.pipeline.steps.steps import StepException
from yt_concat.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCgBN6eQyZPnsApiL1QW44Hg'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()

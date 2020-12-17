from . import models
from constance import config


def show_system_content(request):
    return {
        'blog_categories': models.BlogCategory.objects.all(),
        'video_cast_categories': models.VideoCastCategory.objects.all(),
        'podcast_categories': models.PodcastCategory.objects.all(),
        'podcasts': models.Podcast.objects.order_by('-pk').filter(publish=True)[:2],
        'config': config
    }

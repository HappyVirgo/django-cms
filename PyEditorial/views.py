from django.views import generic

from content import models as ContentModels

from constance import config


class Index(generic.ListView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_blog'] = ContentModels.Blog.objects.order_by('-pk').filter(publish=True)[:1]
        context['skills'] = ContentModels.Skill.objects.all()
        context['blogs'] = ContentModels.Blog.objects.order_by('-pk').filter(publish=True)[1:5]
        context['blogs_categories'] = ContentModels.BlogCategory.objects.all()
        context['videocasts'] = ContentModels.Videocast.objects.order_by('-pk').filter(publish=True)[1:5]
        context['videocasts_categories'] = ContentModels.VideocastCategory.objects.all()
        context['podcast'] = ContentModels.Podcast.objects.order_by('-pk').filter(publish=True)[1:5]
        context['podcast_categories'] = ContentModels.PodcastCategory.objects.all()
        context['config'] = config
        return context

    def get_queryset(self):
        pass

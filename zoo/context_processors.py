from .models import SiteConfiguration

def site_config(request):
    return {
        'config': SiteConfiguration.objects.first()
    }
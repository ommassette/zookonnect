from django.contrib import admin
from .models import SiteConfiguration, HeroSection, CoverageArea, NetworkMetricTile, RelocationRequest

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone_number', 'email_address')
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('heading_text', 'subheading_text')

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(CoverageArea)
class CoverageAreaAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'latitude', 'longitude', 'radius_multiplier', 'hex_color')
    search_fields = ('city_name',)

@admin.register(NetworkMetricTile)
class NetworkMetricTileAdmin(admin.ModelAdmin):
    list_display = ('title', 'metric_value', 'icon_class')

@admin.register(RelocationRequest)
class RelocationRequestAdmin(admin.ModelAdmin):
    list_display = ('contact_phone', 'current_address', 'new_address', 'preferred_move_date', 'created_at')
    list_filter = ('preferred_move_date', 'created_at')
    search_fields = ('contact_phone', 'current_address', 'new_address')
    readonly_fields = ('created_at',)

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address', 'phone_number', 'subject', 'created_at')
    list_filter = ('subject', 'created_at')
    search_fields = ('full_name', 'email_address', 'phone_number', 'message')
    readonly_fields = ('created_at',)



from django.contrib import admin
from .models import AboutHero, AboutStory, AboutStat, AboutMilestone, WhyChoose

class AboutStatInline(admin.TabularInline):
    model = AboutStat
    extra = 1
    fields = ("number", "label", "order")
    ordering = ("order",)

class AboutMilestoneInline(admin.TabularInline):
    model = AboutMilestone
    extra = 1
    fields = ("icon", "year", "title", "description", "order")
    ordering = ("order",)

@admin.register(AboutHero)
class AboutHeroAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active")
    list_filter = ("is_active",)
    fields = ("background_image", "subtitle", "breadcrumb_home", "breadcrumb_separator", "breadcrumb_current", "is_active")

@admin.register(AboutStory)
class AboutStoryAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    inlines = [AboutStatInline, AboutMilestoneInline]

@admin.register(WhyChoose)
class WhyChooseAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("order",)

from django.contrib import admin
from .models import ServicesHero, Service, Feature, Plan, CTA

@admin.register(ServicesHero)
class ServicesHeroAdmin(admin.ModelAdmin):
    list_display = ("id", "is_active")
    list_filter = ("is_active",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "tag_text", "tag_style", "is_active", "order")
    list_filter = ("is_active", "tag_style")
    search_fields = ("title", "description")
    ordering = ("order",)

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("order",)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "is_popular", "is_active", "order")
    list_filter = ("category", "is_popular", "is_active")
    search_fields = ("name", "description", "features")
    ordering = ("category", "order")

@admin.register(CTA)
class CTAAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
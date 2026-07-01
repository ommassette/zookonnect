from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

class SiteConfiguration(models.Model):
    logo = CloudinaryField('image', folder='config/logos/', help_text="Upload site logo")
    company_name = models.CharField(max_length=100, default="ZooKonnect")
    
    phone_number = models.CharField(max_length=20, default="+254 700 000 000")
    email_address = models.EmailField(default="support@ZooKonnect.co.ke")
    office_address = models.CharField(max_length=255, default="Nairobi, Kenya")
    whatsapp_url = models.URLField(default="https://wa.me/254700000000")
    
    meta_description = models.TextField(blank=True, help_text="SEO meta description tag")
    og_image = CloudinaryField('image', folder='config/seo/', blank=True, null=True, help_text="Open Graph image tag")

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return self.company_name


class HeroSection(models.Model):
    background_image = CloudinaryField('image', folder='hero/')
    heading_text = models.CharField(max_length=255, help_text="Use HTML tags like <span> for highlights")
    subheading_text = models.TextField()

    def __str__(self):
        return "Hero Configuration"


class CoverageArea(models.Model):
    city_name = models.CharField(max_length=100)
    image = CloudinaryField('image', folder='coverage/')
    latitude = models.FloatField(help_text="Latitude coordinate for map focus pointer marker")
    longitude = models.FloatField(help_text="Longitude coordinate for map focus pointer marker")
    radius_multiplier = models.FloatField(default=1.0, help_text="Multiplier radius dimension sizing map circle")
    hex_color = models.CharField(max_length=7, default="#F57C00", help_text="Hex color string indicator layout polygon")

    def __str__(self):
        return self.city_name


class NetworkMetricTile(models.Model):
    icon_class = models.CharField(max_length=50, help_text="Bootstrap icon class string name, e.g., bi-wifi")
    title = models.CharField(max_length=100)
    metric_value = models.CharField(max_length=100, help_text="E.g., 95% of Nairobi")

    def __str__(self):
        return self.title


class RelocationRequest(models.Model):
    current_address = models.CharField(max_length=255)
    new_address = models.CharField(max_length=255)
    preferred_move_date = models.DateField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format: +254700000000")
    contact_phone = models.CharField(validators=[phone_regex], max_length=17)
    additional_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Move request to {self.new_address} ({self.contact_phone})"
    



    from django.db import models
from django.core.validators import RegexValidator

class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('sales', 'Sales / New Connection'),
        ('support', 'Technical Support'),
        ('billing', 'Billing / Payments'),
        ('relocation', 'Relocation Request'),
        ('other', 'Other'),
    ]
    
    full_name = models.CharField(max_length=150)
    email_address = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format: +254700000000")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='general')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.full_name} - {self.get_subject_display()}"
    



from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField

ICON_CHOICES = [
    ("bi-wifi", "Wi-Fi"),
    ("bi-shield-check", "Shield Check"),
    ("bi-headset", "Headset"),
    ("bi-coin", "Coin"),
    ("bi-rocket-takeoff", "Rocket Takeoff"),
    ("bi-map", "Map"),
    ("bi-phone", "Phone"),
    ("bi-people", "People"),
    ("bi-trophy", "Trophy"),
    ("bi-lightning-fill", "Lightning"),
    ("bi-building", "Building"),
    ("bi-house-door", "House"),
    ("bi-globe", "Globe"),
    ("bi-speedometer2", "Speedometer"),
    ("bi-arrow-repeat", "Arrow Repeat"),
    ("bi-info-circle", "Info Circle"),
    ("bi-dot", "Dot"),
]

class AboutHero(models.Model):
    background_image = CloudinaryField('image', folder='about/hero/')
    subtitle = models.CharField(max_length=200, blank=True,
                                help_text="Subtitle below the main heading (e.g. 'We're on a mission...')")
    breadcrumb_home = models.CharField(max_length=50, default="Home")
    breadcrumb_separator = models.CharField(max_length=10, default=" / ")
    breadcrumb_current = models.CharField(max_length=50, default="About")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("About Hero")
        verbose_name_plural = _("About Heroes")

    def __str__(self):
        return "About Hero" if self.is_active else "About Hero (inactive)"


class AboutStory(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Main heading (e.g. 'Connecting Kenya Since 2020')")
    description = models.TextField(help_text="The main story paragraph.")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("About Story")
        verbose_name_plural = _("About Stories")

    def __str__(self):
        return self.title


class AboutStat(models.Model):
    story = models.ForeignKey(AboutStory, on_delete=models.CASCADE, related_name="stats")
    number = models.CharField(max_length=20, help_text="e.g. '5+'")
    label = models.CharField(max_length=100, help_text="e.g. 'Cities Covered'")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("About Stat")
        verbose_name_plural = _("About Stats")

    def __str__(self):
        return f"{self.number} {self.label}"


class AboutMilestone(models.Model):
    story = models.ForeignKey(AboutStory, on_delete=models.CASCADE, related_name="milestones")
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="bi-rocket-takeoff")
    year = models.CharField(max_length=20, help_text="e.g. '2020'")
    title = models.CharField(max_length=100, help_text="e.g. 'Launched in Nairobi'")
    description = models.CharField(max_length=200, help_text="e.g. 'Started with 100 customers.'")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = _("About Milestone")
        verbose_name_plural = _("About Milestones")

    def __str__(self):
        return f"{self.year} — {self.title}"


class WhyChoose(models.Model):
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="bi-wifi")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Why Choose Us Item")
        verbose_name_plural = _("Why Choose Us Items")

    def __str__(self):
        return self.title
    

from django.db import models
from cloudinary.models import CloudinaryField

ICON_CHOICES = [
    ("bi-wifi", "Wi-Fi"),
    ("bi-building", "Building"),
    ("bi-house-door", "House"),
    ("bi-speedometer2", "Speedometer"),
    ("bi-shield-check", "Shield Check"),
    ("bi-headset", "Headset"),
    ("bi-coin", "Coin"),
    ("bi-arrow-repeat", "Arrow Repeat"),
    ("bi-rocket-takeoff", "Rocket"),
    ("bi-globe", "Globe"),
    ("bi-check-circle-fill", "Check Circle"),
]

TAG_STYLE_CHOICES = [
    ("orange", "Orange"),
    ("gold", "Gold"),
    ("green", "Green"),
]

class ServicesHero(models.Model):
    background_image = CloudinaryField('image', folder='services/hero/')
    subtitle = models.CharField(max_length=200, blank=True)
    breadcrumb_home = models.CharField(max_length=50, default="Home")
    breadcrumb_separator = models.CharField(max_length=10, default=" / ")
    breadcrumb_current = models.CharField(max_length=50, default="Services")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Services Hero"

    def __str__(self):
        return "Services Hero" if self.is_active else "Services Hero (inactive)"


class Service(models.Model):
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="bi-wifi")
    title = models.CharField(max_length=100)
    description = models.TextField()
    tag_text = models.CharField(max_length=50)
    tag_style = models.CharField(max_length=20, choices=TAG_STYLE_CHOICES, default="orange")
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Feature(models.Model):
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="bi-speedometer2")
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Plan(models.Model):
    CATEGORY_CHOICES = [("home", "Home"), ("business", "Business")]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="home")
    name = models.CharField(max_length=50)
    speed = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    price_period = models.CharField(max_length=20, default="/mo")
    description = models.CharField(max_length=200)
    features = models.TextField(help_text="Comma-separated list")
    is_popular = models.BooleanField(default=False)
    button_text = models.CharField(max_length=50, default="Get Started")
    button_url = models.CharField(max_length=200, default="/contact/")
    button_style = models.CharField(max_length=20, choices=[("primary", "Primary"), ("outline", "Outline")], default="primary")
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "order"]

    def __str__(self):
        return f"{self.get_category_display()} - {self.name}"


class CTA(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=50, default="Sign Up Now")
    button_url = models.CharField(max_length=200, default="/contact/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Call to Action"

    def __str__(self):
        return self.title
from django.db import models
from django.core.validators import RegexValidator
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
    ("bi-check-circle-fill", "Check Circle"),
]

TAG_STYLE_CHOICES = [
    ("orange", "Orange"),
    ("gold", "Gold"),
    ("green", "Green"),
]


class SiteConfiguration(models.Model):
    company_name = models.CharField(max_length=150, blank=True, default="ZooKonnect")
    logo = CloudinaryField('image', folder='config/logos/', blank=True, null=True, help_text="Upload site logo")
    phone_number = models.CharField(max_length=20, blank=True, default="+254 700 000 000")
    email_address = models.EmailField(blank=True, default="support@ZooKonnect.co.ke")
    office_address = models.CharField(max_length=255, blank=True, default="Nairobi, Kenya")
    whatsapp_url = models.URLField(blank=True, default="https://wa.me/254700000000")
    meta_description = models.TextField(blank=True, help_text="SEO meta description tag")
    og_image = CloudinaryField('image', folder='config/seo/', blank=True, null=True, help_text="Open Graph image tag")

    class Meta:
        verbose_name = _("Site Configuration")
        verbose_name_plural = _("Site Configuration")

    def __str__(self):
        return self.company_name or "Site Configuration"


class HeroSection(models.Model):
    background_image = CloudinaryField('image', folder='hero/', blank=True, null=True)
    heading_text = models.CharField(max_length=255, blank=True, help_text="Use HTML tags like <span> for highlights")
    subheading_text = models.TextField(blank=True)

    def __str__(self):
        return "Hero Configuration"


class CoverageArea(models.Model):
    city_name = models.CharField(max_length=100, blank=True)
    image = CloudinaryField('image', folder='coverage/', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True, help_text="Latitude coordinate for map focus pointer marker")
    longitude = models.FloatField(blank=True, null=True, help_text="Longitude coordinate for map focus pointer marker")
    radius_multiplier = models.FloatField(default=1.0, blank=True, null=True, help_text="Multiplier radius dimension sizing map circle")
    hex_color = models.CharField(max_length=7, blank=True, default="#F57C00", help_text="Hex color string indicator layout polygon")

    def __str__(self):
        return self.city_name or "Coverage Area"


class NetworkMetricTile(models.Model):
    icon_class = models.CharField(max_length=50, blank=True, help_text="Bootstrap icon class string name, e.g., bi-wifi")
    title = models.CharField(max_length=100, blank=True)
    metric_value = models.CharField(max_length=100, blank=True, help_text="E.g., 95% of Nairobi")

    def __str__(self):
        return self.title or "Network Metric Tile"


class RelocationRequest(models.Model):
    current_address = models.CharField(max_length=255, blank=True)
    new_address = models.CharField(max_length=255, blank=True)
    preferred_move_date = models.DateField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format: +254700000000")
    contact_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    additional_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Move request to {self.new_address or 'Unknown'} ({self.contact_phone or 'No phone'})"


class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('general', 'General Inquiry'),
        ('sales', 'Sales / New Connection'),
        ('support', 'Technical Support'),
        ('billing', 'Billing / Payments'),
        ('relocation', 'Relocation Request'),
        ('other', 'Other'),
    ]
    
    full_name = models.CharField(max_length=150, blank=True)
    email_address = models.EmailField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Format: +254700000000")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='general', blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.full_name or 'Anonymous'} - {self.get_subject_display()}"


class AboutHero(models.Model):
    background_image = CloudinaryField('image', folder='about/hero/', blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True, help_text="Subtitle below the main heading")
    breadcrumb_home = models.CharField(max_length=50, blank=True, default="Home")
    breadcrumb_separator = models.CharField(max_length=10, blank=True, default=" / ")
    breadcrumb_current = models.CharField(max_length=50, blank=True, default="About")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("About Hero")
        verbose_name_plural = _("About Heroes")

    def __str__(self):
        return "About Hero" if self.is_active else "About Hero (inactive)"


class AboutStory(models.Model):
    title = models.CharField(max_length=200, blank=True, help_text="Main heading")
    description = models.TextField(blank=True, help_text="The main story paragraph.")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("About Story")
        verbose_name_plural = _("About Stories")

    def __str__(self):
        return self.title or "About Story"


class AboutStat(models.Model):
    story = models.ForeignKey(AboutStory, on_delete=models.CASCADE, related_name="stats", blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, help_text="e.g. '5+'")
    label = models.CharField(max_length=100, blank=True, help_text="e.g. 'Cities Covered'")
    order = models.PositiveSmallIntegerField(default=0, blank=True)

    class Meta:
        ordering = ["order"]
        verbose_name = _("About Stat")
        verbose_name_plural = _("About Stats")

    def __str__(self):
        return f"{self.number} {self.label}".strip() or "About Stat"


class AboutMilestone(models.Model):
    story = models.ForeignKey(AboutStory, on_delete=models.CASCADE, related_name="milestones", blank=True, null=True)
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="bi-rocket-takeoff", blank=True)
    year = models.CharField(max_length=20, blank=True, help_text="e.g. '2020'")
    title = models.CharField(max_length=100, blank=True, help_text="e.g. 'Launched in Nairobi'")
    description = models.CharField(max_length=200, blank=True, help_text="e.g. 'Started with 100 customers.'")
    order = models.PositiveSmallIntegerField(default=0, blank=True)

    class Meta:
        ordering = ["order"]
        verbose_name = _("About Milestone")
        verbose_name_plural = _("About Milestones")

    def __str__(self):
        return f"{self.year} — {self.title}".strip(" —") or "About Milestone"


class WhyChoose(models.Model):
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="bi-wifi", blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]
        verbose_name = _("Why Choose Us Item")
        verbose_name_plural = _("Why Choose Us Items")

    def __str__(self):
        return self.title or "Why Choose Item"


class ServicesHero(models.Model):
    background_image = CloudinaryField('image', folder='services/hero/', blank=True, null=True)
    subtitle = models.CharField(max_length=200, blank=True)
    breadcrumb_home = models.CharField(max_length=50, blank=True, default="Home")
    breadcrumb_separator = models.CharField(max_length=10, blank=True, default=" / ")
    breadcrumb_current = models.CharField(max_length=50, blank=True, default="Services")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Services Hero")
        verbose_name_plural = _("Services Heroes")

    def __str__(self):
        return "Services Hero" if self.is_active else "Services Hero (inactive)"


class Service(models.Model):
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="bi-wifi", blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    tag_text = models.CharField(max_length=50, blank=True)
    tag_style = models.CharField(max_length=20, choices=TAG_STYLE_CHOICES, default="orange", blank=True)
    order = models.PositiveSmallIntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title or "Service"


class Feature(models.Model):
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default="bi-speedometer2", blank=True)
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title or "Feature"


class Plan(models.Model):
    CATEGORY_CHOICES = [("home", "Home"), ("business", "Business")]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="home", blank=True)
    name = models.CharField(max_length=50, blank=True)
    speed = models.CharField(max_length=50, blank=True)
    price = models.CharField(max_length=50, blank=True)
    price_period = models.CharField(max_length=20, default="/mo", blank=True)
    description = models.CharField(max_length=200, blank=True)
    features = models.TextField(blank=True, help_text="Comma-separated list")
    is_popular = models.BooleanField(default=False)
    button_text = models.CharField(max_length=50, default="Get Started", blank=True)
    button_url = models.CharField(max_length=200, default="/contact/", blank=True)
    button_style = models.CharField(max_length=20, choices=[("primary", "Primary"), ("outline", "Outline")], default="primary", blank=True)
    order = models.PositiveSmallIntegerField(default=0, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "order"]

    def __str__(self):
        category = self.get_category_display() or "Plan"
        return f"{category} - {self.name}" if self.name else category


class CTA(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.TextField(blank=True)
    button_text = models.CharField(max_length=50, default="Sign Up Now", blank=True)
    button_url = models.CharField(max_length=200, default="/contact/", blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Call to Action")
        verbose_name_plural = _("Calls to Action")

    def __str__(self):
        return self.title or "Call to Action"
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import (
    SiteConfiguration, HeroSection, CoverageArea, NetworkMetricTile, 
    RelocationRequest, ContactMessage, AboutHero, AboutStory, 
    WhyChoose, ServicesHero, Service, Feature, Plan, CTA
)

def index_view(request):
    config = SiteConfiguration.objects.first()
    hero = HeroSection.objects.first()
    metric_tiles = NetworkMetricTile.objects.all()
    
    coverage_areas_list = []
    for area in CoverageArea.objects.all():
        coverage_areas_list.append({
            'city_name': area.city_name,
            'latitude': area.latitude,
            'longitude': area.longitude,
            'radius_multiplier': area.radius_multiplier,
            'hex_color': area.hex_color,
            'image_url': area.image.url if area.image else ''
        })
    
    context = {
        'config': config,
        'hero': hero,
        'coverage_areas': CoverageArea.objects.all(),
        'coverage_areas_json': coverage_areas_list,
        'metric_tiles': metric_tiles,
    }
    return render(request, 'index.html', context)

@require_POST
def process_relocation_view(request):
    current_addr = request.POST.get('current_address', '').strip()
    new_addr = request.POST.get('new_address', '').strip()
    move_date = request.POST.get('move_date', '').strip()
    phone = request.POST.get('contact_phone', '').strip()
    notes = request.POST.get('additional_notes', '').strip()

    if not (current_addr and new_addr and move_date and phone):
        messages.error(request, "Missing required parameter form inputs.")
        return redirect('index')

    RelocationRequest.objects.create(
        current_address=current_addr,
        new_address=new_addr,
        preferred_move_date=move_date,
        contact_phone=phone,
        additional_notes=notes
    )
    
    messages.success(request, "Request received! Our agent will contact you shortly.")
    return redirect('index')

def privacy_policy_view(request):
    config = SiteConfiguration.objects.first()
    return render(request, 'privacy_policy.html', {'config': config})

def contact_view(request):
    config = SiteConfiguration.objects.first()
    return render(request, 'contact.html', {'config': config})

@require_POST
def process_contact_view(request):
    name = request.POST.get('full_name', '').strip()
    email = request.POST.get('email_address', '').strip()
    phone = request.POST.get('phone_number', '').strip()
    subject = request.POST.get('subject', '').strip()
    msg_text = request.POST.get('message', '').strip()

    if not (name and email and phone and subject and msg_text):
        messages.error(request, "Please fill out all required fields.")
        return redirect('contact')

    ContactMessage.objects.create(
        full_name=name,
        email_address=email,
        phone_number=phone,
        subject=subject,
        message=msg_text
    )
    
    messages.success(request, "Your message has been sent successfully! Our team will get back to you shortly.")
    return redirect('contact')

def about_view(request):
    hero = AboutHero.objects.filter(is_active=True).first()
    story = AboutStory.objects.filter(is_active=True).prefetch_related('stats', 'milestones').first()
    why_items = WhyChoose.objects.filter(is_active=True).order_by("order")

    context = {
        "hero": hero,
        "story": story,
        "why_items": why_items,
    }
    return render(request, "about.html", context)

def services_view(request):
    hero = ServicesHero.objects.filter(is_active=True).first()
    services = Service.objects.filter(is_active=True).order_by("order")
    features = Feature.objects.filter(is_active=True).order_by("order")
    plans = Plan.objects.filter(is_active=True).order_by("category", "order")
    cta = CTA.objects.filter(is_active=True).first()

    context = {
        "hero": hero,
        "services": services,
        "features": features,
        "plans": plans,
        "cta": cta,
    }
    return render(request, "services.html", context)
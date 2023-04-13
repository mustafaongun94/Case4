from django.shortcuts import render,redirect,get_object_or_404
from django.utils.crypto import get_random_string
from .models import URL
from .forms import URLForm

def shorten_url(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            # Orijinal url'in daha önce databese'de var olup olmadığını kontrol eder.
            existing_url = URL.objects.filter(original_url=original_url).first()
            if existing_url:
                short_url = existing_url.short_url
            # İlk defa girilen url'in kısaltmasını yapar.
            else:
                short_url = get_random_string(length=6)
                url = URL(original_url=original_url, short_url=short_url)
                url.save()
            return render(request, 'shortened.html', {'url': url, 'short_url': short_url})
    else:
        form = URLForm()
    return render(request, 'shortener.html', {'form': form})


def redirect_to_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    url.visit_count += 1 
    url.save()
    return redirect(url.original_url)
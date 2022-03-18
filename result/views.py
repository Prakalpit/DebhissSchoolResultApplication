from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Result
from .forms import UploadResultForm
from django.contrib.auth.mixins import LoginRequiredMixin

# class HomeView(TemplateView):
#     template_name = 'results/index.html'
#     def get_data(self, request):
#         search_data = request.GET()
#         print(search_data)

def home(request):
    return render(request, 'results/index.html')

def ResultPage(request):
    passw = request.POST.get('password')
    passw = (passw.strip()).lower()
    if Result.objects.filter(password=passw).exists():
        queryset = Result.objects.get(password=passw)
        context = {
        'student_result': queryset,
        }
        return render(request, 'results/view-results.html', context)
    else:
        return render(request, 'results/withheld-or-wrong.html')



class DetailResultPage(DetailView):
    model = Result
    template_name = 'results/view-results.html'

class UploadView(LoginRequiredMixin,CreateView):
    # form_class = UploadResultForm
    model = Result
    template_name = 'results/UploadResults.html'
    fields = "__all__"
    success_url = reverse_lazy('upload-results')

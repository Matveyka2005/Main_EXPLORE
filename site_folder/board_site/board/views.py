from django.http import Http404, HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render

from board.forms import BbForm
from board.models import *
from board.service import *


class MainListView(ListView):
    paginate_by = 6
    model = Bb
    context_object_name = "bbs"
    template_name = "board/main.html"

    def get_queryset(self):
        return Bb.objects.select_related('rubric').all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class Search(ListView):
    template_name = "board/main.html"
    paginate_by = 6
    context_object_name = "bbs"
    
    # title__icontains -> нечувствительность к регистру
    # serching -> имя поля из html страницы, точнее значение, которое ввел пользователь в форму )
    def get_queryset(self):
        return Bb.objects.select_related('rubric').filter(title__icontains=self.request.GET.get("serching"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["serching"] = self.request.GET.get("serching")
        context['rubrics'] = get_all_objects(Rubric)
        return context


class BbCreateView(CreateView):
    template_name = "board/create.html"
    form_class = BbForm
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context

    def form_valid(self, form):
        form.save()
        # !connect by celery
        user_upload_connect(self.request.user, form.instance)
        return super().form_valid(form)


class ContentDetailView(DetailView):
    model = Bb
    template_name = 'board/bb_deteil.html'

    def get_queryset(self):
        return Bb.objects.select_related('rubric').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric) 
        return context


class ByRubricListView(ListView):
    model = Bb
    paginate_by = 6
    context_object_name = 'bbs'
    template_name = "board/main.html"

    def get_queryset(self):
        try:
            obj = Bb.objects.select_related('rubric').filter(rubric=self.kwargs['rubric_id'])
        except Exception as e:
            print(e)
            return Http404()
        else:
            return obj
        
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)

        try:
            current_rubric = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        except Exception:
            raise Http404

        context['current_rubric'] = current_rubric
        return context


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    template_name = 'board/edit_form.html'
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteUploadView(DeleteView):
    model = Bb
    template_name = "board/delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rubrics"] = Rubric.objects.all()
        return context 





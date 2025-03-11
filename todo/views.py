from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from .models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'

    def get_queryset(self):
        return Task.objects.all().order_by('is_done', '-created_at')


class TagsListView(ListView):
    model = Tag
    template_name = 'todo/tag_list.html'

    def get_queryset(self):
        return Tag.objects.all().order_by('name')


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task_list')


class TagsCreateView(CreateView):
    model = Tag
    fields = "__all__"
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('todo:tags_list')


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('todo:task_list')


class TagsUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    template_name = 'todo/tag_form.html'
    success_url = reverse_lazy('todo:tags_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('todo:task_list')


class TagsDeleteView(DeleteView):
    model = Tag
    template_name = 'todo/tag_confirm_delete.html'
    success_url = reverse_lazy('todo:tags_list')


class TaskToggleStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('todo:task_list')


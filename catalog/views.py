from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version


# Контроллер CBV
class HomeView(ListView):
    '''Класс вывода всех продуктов.'''
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self.get_queryset()

        for product in products:
            product.versions = Version.objects.filter(product=product)
            product.version = product.versions.filter(working_ver=True).first()

        return context


# Контроллер CBV
class ProductDetailView(DetailView):
    '''Класс вывода детальной информации о продукте.'''
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        versions = Version.objects.filter(product=product)
        context['versions'] = versions
        working_ver = versions.filter(working_ver=True).first()
        context['working_ver'] = working_ver

        return context


class ProductCreateView(CreateView):
    '''Класс создания нов.продукта.'''
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    '''Класс редактирования данных продукта.'''
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        '''Метод валидации.'''
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


def toggle_working_ver(request, pk):
    '''Функция вывода только рабочих версий'''
    version_item = get_object_or_404(Product, pk=pk)
    if version_item.working_ver:
        version_item.working_ver = False
    else:
        version_item.working_ver = True

    version_item.save()

    return redirect(reverse('catalog:home'))


class ProductDeleteView(DeleteView):
    '''Класс удаления продукта.'''
    model = Product
    success_url = reverse_lazy('catalog:home')


# Контроллер FBV
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    context = {
        'title': 'contact'
    }
    return render(request, 'catalog/contacts.html', context)


class BlogListView(ListView):
    '''Класс просмотра всех публикаций.'''
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    '''Класс просмотра детальной информации публикации.'''
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    '''Класс создания нов.публикации'''
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('catalog:blg')


class BlogUpdateView(UpdateView):
    '''Класс редактирования данных публикации'''
    model = Blog
    fields = ('title', 'content', 'image', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    '''Класс удаления публикации'''
    model = Blog
    success_url = reverse_lazy('catalog:blg')


def toggle_published(request, pk):
    '''Функция вывода только опубликованных публикаций'''
    publication_item = get_object_or_404(Blog, pk=pk)
    if publication_item.is_published:
        publication_item.is_published = False
    else:
        publication_item.is_published = True

    publication_item.save()

    return redirect(reverse_lazy('catalog:blg'))

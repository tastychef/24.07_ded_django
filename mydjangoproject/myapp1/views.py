from django.shortcuts import render

from myapp1.models import Worker


def index_page(request):
    new_worker = Worker(name='Лена', second_name='Солдатенко', salary='60000')
    new_worker.save()
    all_workers = Worker.objects.all()
    print(all_workers)

    workers_filtered = Worker.objects.filter(salary=150000)
    print(workers_filtered)

    for i in all_workers:
        print(f'Имя: {i.name}, Фамилия: {i.second_name}, ЗП: {i.salary}, ID: {i.id}')
    return render(request, 'index.html')


def about_page(request):
    return render(request, 'about.html')

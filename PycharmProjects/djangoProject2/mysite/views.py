from django.shortcuts import render, redirect
from .models import Calculation


def index(request):
    return render(request, 'mysite/index.html')


def ficha(request):
    return render(request, 'mysite/ficha.html')


def calculator(request):
    result = None
    if request.method == "POST":
        if 'delete' in request.POST:
            # Видалити обчислення
            Calculation.objects.filter(id=request.POST.get('delete')).delete()
        else:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Error: Division by zero'

            # Зберігаємо результат в базу даних
            if isinstance(result, (float, int)):  # Перевіряємо, чи результат числовий
                Calculation.objects.create(num1=num1, num2=num2, operation=operation, result=result)

    calculations = Calculation.objects.all()  # Отримуємо всі обчислення

    return render(request, 'mysite/calculator.html', {'result': result, 'calculations': calculations})


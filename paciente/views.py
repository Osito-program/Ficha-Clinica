from django.shortcuts import get_object_or_404, render
from .models import LugarAtencion, Paciente
from .forms import MedicoForm, PacienteForm
from django.shortcuts import redirect

# Create your views here.
def pacienteinicio(request):
    pacientes = Paciente.objects.all()  #select * from paciente
    traspaso = {
        'pacientes':pacientes
    }
    return render(request, 'index.html', traspaso)

def historial(request, rut):
    pacientes = Paciente.objects.filter(rut = rut)
    datos = {
        'pacientes':pacientes
    }
    return render(request, 'historial.html',datos)

def clinica(request):
    pacientes = Paciente.objects.filter(lugarAtencion_id = 1)
    datos = {
        'pacientes':pacientes
    }
    return render(request, 'clinica.html', datos)

def domicilio(request):
    pacientes = Paciente.objects.filter(lugarAtencion_id = 2)
    datos = {
        'pacientes':pacientes
    }
    return render(request, 'domicilio.html', datos)

def nuevoPaciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (pacienteinicio)
    else:
        form = PacienteForm
    return render(request, 'nuevopaciente.html', {'form':form})

def nuevoMedico(request):
    if request.method == "POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (pacienteinicio)
    else:
        form = MedicoForm
    return render(request, 'nuevomedico.html', {'form':form})

def editarPaciente(request, rut):
    post = get_object_or_404(Paciente, rut=rut)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PacienteForm(instance=post)
    return render(request, 'editarpaciente.html', {'form': form})

def eliminarPaciente(request, rut):
    paciente = Paciente.objects.get(rut=rut)
    paciente.delete()
    return redirect('index')

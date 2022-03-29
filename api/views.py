from django.shortcuts import render
from django.views import View
from .models import Lugar, Avistamiento, Especie
from django.http import JsonResponse
from django.utils.decorators import method_decorator
import json
from django.views.decorators.csrf import csrf_exempt

# CRUD LUGARES
class LugarView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            lugares=list(Lugar.objects.filter(id=id).values())
            if len(lugares)>0:
                lugar=lugares[0]
                datos ={'message':"Success", 'lugar':lugar}
            else:
                datos={'message':"Lugares not found"}
            return JsonResponse(datos)
        else:
            lugares=list(Lugar.objects.values())
            if len(lugares)>0:
                datos={'message':"Success", 'lugares':lugares}
            else:
                datos={'message':"Lugares not found"}
            return JsonResponse(datos)

    def post(self, request):
        
        jload = json.loads(request.body)
        Lugar.objects.create(name=jload['name'], id_ciudad_id=jload['id_ciudad_id'])
        datos = {'message':"Success"}

        return JsonResponse(datos)

    def put(self, request, id):
        jload = json.loads(request.body)
        lugares=list(Lugar.objects.filter(id=id).values())
        if len(lugares)>0:
            lugar = Lugar.objects.get(id=id)
            lugar.name=jload['name']
            lugar.id_ciudad_id=jload['id_ciudad_id']
            lugar.save()
            datos = {'message':"Lugar Update"}

        else:
            datos = {'message' : "Lugar not found"}

        return JsonResponse(datos)
        
    def delete(self, request, id):
        lugares=list(Lugar.objects.filter(id=id).values())
        if len(lugares)>0:
            Lugar.objects.filter(id=id).delete()
        else:
            datos={'message' : "Lugar not found"}
        return JsonResponse(datos)

class EspecieView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if (id>0):
            especies=list(Especie.objects.filter(id=id).values())
            if len(especies)>0:
                especie=especies[0]
                datos ={'message':"Success", 'especie':especie}
            else:
                datos={'message':"Especies not found"}
            return JsonResponse(datos)
        else:
            especies=list(Especie.objects.values())
            if len(especies)>0:
                datos={'message':"Success", 'especies':especies}
            else:
                datos={'message':"Especies not found"}
            return JsonResponse(datos)

    def post(self, request):
        
        jload = json.loads(request.body)
        Especie.objects.create(nameComun=jload['nameComun'], nameCientifico=jload['nameCientifico'], id_genero_id=jload['id_genero_id'], id_filo_id=jload['id_filo_id'], id_clase_id=jload['id_clase_id'],id_orden_id=jload['id_orden_id'], id_familia_id=jload['id_familia_id'])
        datos = {'message':"Success"}

        return JsonResponse(datos)

    def put(self, request, id):
        jload = json.loads(request.body)
        especies=list(Especie.objects.filter(id=id).values())
        if len(especies)>0:
            especie = Especie.objects.get(id=id)
            especie.name=jload['name']
            especie.id_ciudad_id=jload['id_ciudad_id']
            especie.save()
            datos = {'message':"Especie Update"}

        else:
            datos = {'message' : "Especie not found"}

        return JsonResponse(datos)
        
    def delete(self, request, id):
        especies=list(Especie.objects.filter(id=id).values())
        if len(especies)>0:
            Especie.objects.filter(id=id).delete()
        else:
            datos={'message' : "Especie not found"}
        return JsonResponse(datos)


class AvistamientoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            avistamientos=list(Avistamiento.objects.filter(id=id).values())
            if len(avistamientos)>0:
                avistamiento=avistamientos[0]
                datos ={'message':"Success", 'avistamiento':avistamiento}
            else:
                datos={'message':"Avistamiento not found"}
            return JsonResponse(datos)
        else:
            avistamientos=list(Avistamiento.objects.values())
            if len(avistamientos)>0:
                datos={'message':"Success", 'avistamientos':avistamientos}
            else:
                datos={'message':"Avistamientos not found"}
            return JsonResponse(datos)


    def post(self, request):
        jload = json.loads(request.body)
        Avistamiento.objects.create(name=jload['name'], nota=jload['nota'], autor=jload['autor'],latitud=jload['latitud'],longitud=jload['longitud'], id_lugar_id=['id_lugar_id'], id_especie_id=['id_especie_id'])
        datos = {'message':"Success"}

        return JsonResponse(datos)

    def put(self, request, id=0):
        jload = json.loads(request.body)
        avistamientos=list(Avistamiento.objects.filter(id=id).values())
        if len(avistamientos)>0:
            avistamiento = Avistamiento.objects.get(id=id)
            avistamiento.name=jload['name']
            avistamiento.nota=jload['nota']
            avistamiento.autor=jload['autor']
            avistamiento.latitud=jload['latitud']
            avistamiento.longitud=jload['longitud']
            avistamiento.id_lugar_id=jload['id_lugar_id']
            avistamiento.id_especie_id=jload['id_especie_id']
            avistamiento.save()
            datos = {'message':"Avistamiento Update"}

        else:
            datos = {'message' : "Avistamiento not found"}

        return JsonResponse(datos)
        
    def delete(self, request, id):
        avistamientos=list(Avistamiento.objects.filter(id=id).values())
        if len(avistamientos)>0:
            Avistamiento.objects.filter(id=id).delete()
        else:
            datos={'message' : "Avistamiento not found"}
        return JsonResponse(datos)
    
    def getBySpecie(self, request, ide):
        avistamiento = Avistamiento.objects.get(id=ide)
        if (avistamiento.id_especie_id==ide):
            if (id_especie_id>0):
                avistamientos=list(Avistamiento.objects.filter(id_especie_id=id_especie_id).values())
                if len(avistamientos)>0:
                    avistamiento=avistamientos[0]
                    datos ={'message':"Success", 'avistamiento':avistamiento}
            else:
                datos={'message':"avistamiento not found"}
            return JsonResponse(datos)




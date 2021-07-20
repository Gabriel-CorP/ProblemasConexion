from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from crearReportes.models import Usuario
from crearReportes.models import Direccion
from crearReportes.models import Problema
from crearReportes.models import Conexion
from crearReportes.models import Departamento
from crearReportes.models import Municipio
from crearReportes.models import Tipo_Conexion
from crearReportes.models import Tipo_Problema
from crearReportes.models import Proveedor
from crearReportes.models import Velocidad
from django.http import JsonResponse
import sweetify
#from django import forms
# Create your views here.
@requires_csrf_token
@csrf_exempt 
def guardar_reportes(request):
    departamentos=Departamento.objects.all()
    municipios=Municipio.objects.all()
    conexiones=Tipo_Conexion.objects.all()
    proveedores=Proveedor.objects.all()
    velocidades=Velocidad.objects.all()
    problemas=Tipo_Problema.objects.all()
    
    if request.method == "POST":
        nom=request.POST["nombres"]
        ape=request.POST["apellidos"]
        tel=request.POST["telefono"]
        document=request.POST["dui"]
        user=Usuario(dui=document, nombre=nom, apellido=ape, telefono=tel)
        user.save()
        usuarioFk=user.pk

        depa=request.POST["listaD"]
        muni=request.POST["listaM"]
        direccion=Direccion(departamento_id=depa, municipio_id=muni,usuario_id=usuarioFk)
        direccion.save()

        conec=request.POST["listaC"]
        prov=request.POST["listaP"]
        velo=request.POST["listaV"]
        conex=Conexion(tipo_conexion_id=conec, velocidad_id=velo,proveedor_id=prov)
        conex.save()

        ultmimaConexion=conex.pk
        tipoProblema=request.POST["listaProb"]
        descrip=request.POST["des"]
        problema=Problema(tipo_problema_id=tipoProblema, descripcion=descrip, usuario_id=usuarioFk, conexion_id=ultmimaConexion)
        problema.save()
        sweetify.success(request, 'Guardado con exito', text='Se ha enviado con exito su reporte', button='Ok', icon='success', timer=30000)    
    
    return render(request,"form.html",{"dep":departamentos, "muni":municipios, "conex":conexiones, "prov":proveedores, "vel":velocidades, "prob":problemas})


def Visualizar(request):
     #Problemas
     otro_count = Problema.objects.filter(tipo_problema_id=5).count()
     lineasCaidas_count = Problema.objects.filter(tipo_problema_id=4).count()
     velocidad_count = Problema.objects.filter(tipo_problema_id=1).count()
     perdida_count = Problema.objects.filter(tipo_problema_id=2).count()
     modem_count = Problema.objects.filter(tipo_problema_id=3).count()
     problemas_data = [lineasCaidas_count,velocidad_count,perdida_count,modem_count,otro_count]

     #Proveedores
     tigo_count = Conexion.objects.filter(proveedor_id=2).count()
     claro_count = Conexion.objects.filter(proveedor_id=1).count()
     movistar_count = Conexion.objects.filter(proveedor_id=3).count()
     digicel_count = Conexion.objects.filter(proveedor_id=4).count()
     salnet_count = Conexion.objects.filter(proveedor_id=5).count()
     japi_count = Conexion.objects.filter(proveedor_id=6).count()
     proveedor_data = [tigo_count,claro_count,movistar_count,digicel_count,salnet_count,japi_count]

     #Conexiones
     fibraOptica_count = Conexion.objects.filter(tipo_conexion_id=1).count()
     wifi_count = Conexion.objects.filter(tipo_conexion_id=2).count()
     datosMoviles_count = Conexion.objects.filter(tipo_conexion_id=3).count()
     cable_count = Conexion.objects.filter(tipo_conexion_id=4).count()
     conexion_data = [fibraOptica_count,wifi_count,datosMoviles_count,cable_count]

     #Velocidades
     unMBPS_count = Conexion.objects.filter(velocidad_id=1).count()
     dosMBPS_count = Conexion.objects.filter(velocidad_id=2).count()
     tresMBPS_count = Conexion.objects.filter(velocidad_id=3).count()
     cincoMBPS_count = Conexion.objects.filter(velocidad_id=4).count()
     diezMBPS_count = Conexion.objects.filter(velocidad_id=5).count()
     veinteMBPS_count = Conexion.objects.filter(velocidad_id=6).count()
     treintaMBPS_count = Conexion.objects.filter(velocidad_id=7).count()
     velocidad_data = [unMBPS_count,dosMBPS_count,tresMBPS_count,cincoMBPS_count,diezMBPS_count,veinteMBPS_count,treintaMBPS_count]

     #Departamentos
     ahuachapan_count = Direccion.objects.filter(departamento_id=1).count()
     cabanas_count = Direccion.objects.filter(departamento_id=9).count()
     chalatenango_count = Direccion.objects.filter(departamento_id=5).count()
     cuscatlan_count = Direccion.objects.filter(departamento_id=7).count()
     lalibertad_count = Direccion.objects.filter(departamento_id=4).count()
     lapaz_count = Direccion.objects.filter(departamento_id=8).count()
     launion_count = Direccion.objects.filter(departamento_id=14).count()
     morazan_count = Direccion.objects.filter(departamento_id=12).count()
     sanmiguel_count = Direccion.objects.filter(departamento_id=13).count()
     sansalvador_count = Direccion.objects.filter(departamento_id=6).count()
     sanvicente_count = Direccion.objects.filter(departamento_id=10).count()
     santaana_count = Direccion.objects.filter(departamento_id=2).count()
     sonsonate_count = Direccion.objects.filter(departamento_id=3).count()
     usulutan_count = Direccion.objects.filter(departamento_id=11).count()
     departamento_data = [ahuachapan_count,cabanas_count,chalatenango_count,cuscatlan_count,lalibertad_count,lapaz_count,launion_count,morazan_count,sanmiguel_count,sansalvador_count,sanvicente_count,santaana_count,sonsonate_count,usulutan_count]

     contexto = {'problemasCount':problemas_data,'proveedorCount':proveedor_data,'conexionCount':conexion_data,'velocidadCount':velocidad_data,'departamentoCount':departamento_data}
     return render(request,"Estadisticas.html",contexto)

def Update(request):
     #Problemas
     otro_count = Problema.objects.filter(tipo_problema_id=5).count()
     lineasCaidas_count = Problema.objects.filter(tipo_problema_id=4).count()
     velocidad_count = Problema.objects.filter(tipo_problema_id=1).count()
     perdida_count = Problema.objects.filter(tipo_problema_id=2).count()
     modem_count = Problema.objects.filter(tipo_problema_id=3).count()
     problemas_data = [lineasCaidas_count,velocidad_count,perdida_count,modem_count,otro_count]

     #Proveedores
     tigo_count = Conexion.objects.filter(proveedor_id=2).count()
     claro_count = Conexion.objects.filter(proveedor_id=1).count()
     movistar_count = Conexion.objects.filter(proveedor_id=3).count()
     digicel_count = Conexion.objects.filter(proveedor_id=4).count()
     salnet_count = Conexion.objects.filter(proveedor_id=5).count()
     japi_count = Conexion.objects.filter(proveedor_id=6).count()
     proveedor_data = [tigo_count,claro_count,movistar_count,digicel_count,salnet_count,japi_count]

     #Conexiones
     fibraOptica_count = Conexion.objects.filter(tipo_conexion_id=1).count()
     wifi_count = Conexion.objects.filter(tipo_conexion_id=2).count()
     datosMoviles_count = Conexion.objects.filter(tipo_conexion_id=3).count()
     cable_count = Conexion.objects.filter(tipo_conexion_id=4).count()
     conexion_data = [fibraOptica_count,wifi_count,datosMoviles_count,cable_count]

     #Velocidades
     unMBPS_count = Conexion.objects.filter(velocidad_id=1).count()
     dosMBPS_count = Conexion.objects.filter(velocidad_id=2).count()
     tresMBPS_count = Conexion.objects.filter(velocidad_id=3).count()
     cincoMBPS_count = Conexion.objects.filter(velocidad_id=4).count()
     diezMBPS_count = Conexion.objects.filter(velocidad_id=5).count()
     veinteMBPS_count = Conexion.objects.filter(velocidad_id=6).count()
     treintaMBPS_count = Conexion.objects.filter(velocidad_id=7).count()
     velocidad_data = [unMBPS_count,dosMBPS_count,tresMBPS_count,cincoMBPS_count,diezMBPS_count,veinteMBPS_count,treintaMBPS_count]

     #Departamentos
     ahuachapan_count = Direccion.objects.filter(departamento_id=1).count()
     cabanas_count = Direccion.objects.filter(departamento_id=9).count()
     chalatenango_count = Direccion.objects.filter(departamento_id=5).count()
     cuscatlan_count = Direccion.objects.filter(departamento_id=7).count()
     lalibertad_count = Direccion.objects.filter(departamento_id=4).count()
     lapaz_count = Direccion.objects.filter(departamento_id=8).count()
     launion_count = Direccion.objects.filter(departamento_id=14).count()
     morazan_count = Direccion.objects.filter(departamento_id=12).count()
     sanmiguel_count = Direccion.objects.filter(departamento_id=13).count()
     sansalvador_count = Direccion.objects.filter(departamento_id=6).count()
     sanvicente_count = Direccion.objects.filter(departamento_id=10).count()
     santaana_count = Direccion.objects.filter(departamento_id=2).count()
     sonsonate_count = Direccion.objects.filter(departamento_id=3).count()
     usulutan_count = Direccion.objects.filter(departamento_id=11).count()
     departamento_data = [ahuachapan_count,cabanas_count,chalatenango_count,cuscatlan_count,lalibertad_count,lapaz_count,launion_count,morazan_count,sanmiguel_count,sansalvador_count,sanvicente_count,santaana_count,sonsonate_count,usulutan_count]

     contexto = {'problemasCount':problemas_data,'proveedorCount':proveedor_data,'conexionCount':conexion_data,'velocidadCount':velocidad_data,'departamentoCount':departamento_data}
     return (JsonResponse(contexto))
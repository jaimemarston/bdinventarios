from rest_framework import serializers

from gestionapp.models import Deposito, Articulo, Cliente, Proveedor, Unidad, Programagastos, Mcotizacion, Dcotizacion, \
    Clientesdireccion, Banco, CotizacionEstado


class BancoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = ('id', 'codigo', 'descripcion')


class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ('id', 'codigo', 'descripcion')


class UnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = ('id', 'codigo', 'descripcion', 'placa', 'npasajeros', 'color', 'foto1', 'foto2')


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'codigo', 'descripcion',
                  'cantidad', 'color', 'deposito')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'codigo', 'nombre', 'ruc',
                  'telefono1', 'telefono2', 'telefono3', 'contacto', 'telcontacto',
                  'direccion', 'correo', 'paginaweb', 'tipocc', 'destipocc',
                  'banco_nombre1', 'banco_cuenta1', 'banco_moneda1', 'banco_nombre2', 'banco_cuenta2',
                  'banco_moneda2', 'fechanac', 'fechaini', 'fechafin', 'grupo', 'pais', 'idioma')

    def create(self, validated_data):
        last_id = Cliente.objects.last().id if Cliente.objects.last() else 1
        validated_data['codigo'] = str(last_id).zfill(6)  # is not None

        return Cliente.objects.create(**validated_data)
    

"""
    def create(self, validated_data):
      #  validated_data['codigo'] = str(Cliente.objects.last().id).zfill(6)
      validated_data['codigo'] = str(Cliente.objects.last().id).zfill(6) if Cliente.objects.last().id  is not None else str(1)
      return Cliente.objects.create(**validated_data)
"""


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id', 'codigo', 'nombre', 'ruc',
                  'telefono1', 'telefono2', 'telefono3', 'contacto', 'telcontacto',
                  'direccion', 'correo', 'paginaweb', 'tipocc', 'destipocc',
                  'banco_nombre1', 'banco_cuenta1', 'banco_moneda1', 'banco_nombre2', 'banco_cuenta2',
                  'banco_moneda2', 'fechanac', 'fechaini', 'fechafin', 'grupo', 'pais', 'idioma')

    def create(self, validated_data):
        last_id = Proveedor.objects.last().id if Proveedor.objects.last() else 1
        validated_data['codigo'] = str(last_id).zfill(6)  # is not None

        return Proveedor.objects.create(**validated_data)


"""
    def create(self, validated_data):
      #  validated_data['codigo'] = str(Cliente.objects.last().id).zfill(6)
      validated_data['codigo'] = str(Cliente.objects.last().id).zfill(6) if Cliente.objects.last().id  is not None else str(1)
      return Cliente.objects.create(**validated_data)
"""


class DcotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dcotizacion
        fields = ('id', 'codigo', 'codpro', 'descripcion', 'unimed', 'desunimed', 'cantidad', 'precio', 'impsubtotal',
                  'impanticipos', 'impdescuentos',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'desgrupo1', 'desgrupo2', 'lugorigen', 'lugdestino', 'opcviaje',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'conductor', 'nvuelo',
                  'proveedor', 'obs', 'tipodoc', 'estado', 'estadodoc', 'posmapa', 'master' )

     

class McotizacionSerializer(serializers.ModelSerializer):
    cotizaciones = DcotizacionSerializer(many=True, read_only=True)

    class Meta:
        model = Mcotizacion
        fields = ('id', 'codigo', 'descripcion', 'tipdoc', 'destipdoc', 'seriedoc', 'numerodoc', 'fechadoc',
                  'fecentrega', 'ruc', 'desruc', 'telruc', 'paisruc', 'dptoruc', 'provruc', 'distruc', 'codpostalruc',
                  'dirruc', 'conpag', 'desconpag', 'monedapago', 'desmonepago', 'tc_dolares', 'tc_euros', 'tc_yen',
                  'numeroguia', 'numordserv', 'vendidopor', 'fechapago', 'autorizadosunat', 'impsubtotal',
                  'impdescuentos',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'correoruc', 'unidadtransporte',
                  'lugorigen', 'lugdestino', 'opcviaje',
                  'estado', 'grupo', 'posmapa', 'cotizaciones')



class ClientesdireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientesdireccion
        fields = ('direccion', 'telefono')
        # fields = '__all__'


class ClientesdirecciondetalleSerializer(serializers.ModelSerializer):
    clientesdirecciones = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cliente
        fields = ('nombre', 'ruc', 'clientesdirecciones')


class CotizacionEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CotizacionEstado
        fields = '__all__'

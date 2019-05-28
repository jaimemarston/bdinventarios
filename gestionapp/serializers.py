from rest_framework import serializers

from gestionapp.models import Deposito, Material, Articulo, Cliente, Proveedor, Unidad, Programagastos, Mcotizacion, Dcotizacion, \
    Clientesdireccion, Banco, CotizacionEstado, MaterialesEstado, Mmateriales, Dmateriales


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


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('id', 'codigo', 'descripcion',
                  'cantidad', 'color', 'deposito',
                   'descolor','stock1','codbarra','stockalm1','stockalm2','stockalm3','afectoigv','preciocosto','precioventa', 
                   'aplicadscto','cc1','descc1','modelo','genero','talla','ruc','desruc','unimed',
                   'desunimed','umdsali','umdsaliconv','monedacompra','desmonecompra','tipo')


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ('id', 'codigo', 'descripcion',
                  'cantidad', 'color', 'deposito',
                   'descolor','stock1','codbarra','stockalm1','stockalm2','stockalm3','afectoigv','preciocosto','precioventa', 
                   'aplicadscto','cc1','descc1','modelo','genero','talla','ruc','desruc','unimed',
                   'desunimed','umdsali','umdsaliconv','monedaventa','desmoneventa','tipo')

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
                  'proveedor', 'obs', 'tipodoc', 'estado', 'estadodoc', 'posmapa','modelo','genero','talla','tipo', 'master' )

     

class McotizacionSerializer(serializers.ModelSerializer):
    cotizaciones = DcotizacionSerializer(many=True, read_only=True)

    class Meta:
        model = Mcotizacion
        fields = ('id', 'codigo', 'descripcion', 'tipdoc', 'destipdoc', 'seriedoc', 'numerodoc', 'fechadoc',
                  'fecentrega', 'ruc', 'desruc', 'telruc', 'paisruc', 'dptoruc', 'provruc', 'distruc', 'codpostalruc',
                  'dirruc', 'conpag', 'desconpag', 'monedapago', 'desmonepago', 'tc_dolares', 'tc_euros', 'tc_yen',
                  'numeroguia', 'numordserv', 'vendidopor', 'fechapago', 'autorizadosunat', 'impsubtotal',
                  'impdescuentos','imppagado',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'correoruc', 'unidadtransporte',
                  'lugorigen', 'lugdestino', 'opcviaje',
                  'estado', 'grupo', 'posmapa', 'cotizaciones')


# Materiales

class DmaterialesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dmateriales
        fields = ('id', 'codigo', 'codpro', 'descripcion', 'unimed', 'desunimed', 'cantidad', 'precio', 'impsubtotal',
                  'impanticipos', 'impdescuentos',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'desgrupo1', 'desgrupo2', 'lugorigen', 'lugdestino', 'opcviaje',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'conductor', 'nvuelo',
                  'proveedor', 'obs', 'tipodoc', 'estado', 'estadodoc', 'posmapa','modelo','genero','talla','tipo', 'master' )

     

class MmaterialesSerializer(serializers.ModelSerializer):
    materiales = DmaterialesSerializer(many=True, read_only=True)

    class Meta:
        model = Mmateriales
        fields = ('id', 'codigo', 'descripcion', 'tipdoc', 'destipdoc', 'seriedoc', 'numerodoc', 'fechadoc',
                  'fecentrega', 'ruc', 'desruc', 'telruc', 'paisruc', 'dptoruc', 'provruc', 'distruc', 'codpostalruc',
                  'dirruc', 'conpag', 'desconpag', 'monedapago', 'desmonepago', 'tc_dolares', 'tc_euros', 'tc_yen',
                  'numeroguia', 'numordserv', 'vendidopor', 'fechapago', 'autorizadosunat', 'impsubtotal',
                  'impdescuentos','imppagado',
                  'impvalorventa', 'impisc', 'impigv', 'nvaligv', 'impotroscargos', 'impotrostributos', 'imptotal',
                  'cc1', 'cc2', 'cc3', 'fechaini', 'fechafin', 'horaini', 'horafin', 'correoruc', 'unidadtransporte',
                  'lugorigen', 'lugdestino', 'opcviaje',
                  'estado', 'grupo', 'posmapa', 'materiales')


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


class MaterialesEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialesEstado
        fields = '__all__'
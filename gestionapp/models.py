from django.db import models

# Create your models here.

COLORES = (
    ('0', 'Blanco'),
    ('1', 'Negro'),
    ('2', 'Rojo'),
    ('3', 'Amarillo'),
    ('4', 'Azul'),
)


class Camposcomunes_masterdoc(models.Model):
    codigo = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=30, null=True, blank=True)
    tipdoc = models.CharField(max_length=30, null=True, blank=True)
    destipdoc = models.CharField(max_length=30, null=True, blank=True)
    seriedoc = models.CharField(max_length=30, null=True, blank=True)
    numerodoc = models.CharField(max_length=30, null=True, blank=True)
    fechadoc = models.DateField(null=True, blank=True)
    fecentrega = models.DateField(null=True, blank=True)  # Fecha entrega pedido
    ruc = models.CharField(max_length=30, null=True, blank=True)
    desruc = models.CharField(max_length=150, null=True, blank=True)
    telruc = models.CharField(max_length=30, null=True, blank=True)
    paisruc = models.CharField(max_length=30, null=True, blank=True)
    dptoruc = models.CharField(max_length=30, null=True, blank=True)
    provruc = models.CharField(max_length=30, null=True, blank=True)
    distruc = models.CharField(max_length=30, null=True, blank=True)
    codpostalruc = models.CharField(max_length=30, null=True, blank=True)
    dirruc = models.CharField(max_length=150, null=True, blank=True)
    conpag = models.CharField(max_length=30, null=True, blank=True)
    desconpag = models.CharField(max_length=50, null=True, blank=True)
    monedapago = models.IntegerField(default=0)  # soles,dolares,euros,yen
    desmonepago = models.CharField(max_length=50, null=True, blank=True)
    tc_dolares = models.DecimalField(default=0, max_digits=8, decimal_places=3, null=True, blank=True)
    tc_euros = models.DecimalField(default=0, max_digits=8, decimal_places=3, null=True, blank=True)
    tc_yen = models.DecimalField(default=0, max_digits=8, decimal_places=3, null=True, blank=True)
    numeroguia = models.IntegerField(default=0)
    numordserv = models.IntegerField(default=0)
    vendidopor = models.CharField(max_length=30, null=True, blank=True)
    fechapago = models.DateField(null=True, blank=True)
    unidadtransporte = models.CharField(max_length=50, null=True, blank=True)
    autorizadosunat = models.IntegerField(default=0)
    impsubtotal = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impanticipos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impdescuentos =models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impvalorventa = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impisc = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impigv = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    nvaligv = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impotroscargos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impotrostributos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    imptotal = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    imppagado = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    cc1 = models.CharField(max_length=30, null=True, blank=True)  # cc para saber donde se hace gasto
    cc2 = models.CharField(max_length=30, null=True, blank=True)
    cc3 = models.CharField(max_length=30, null=True, blank=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    correoruc = models.CharField(max_length=150, null=True, blank=True)
    horaini = models.CharField(max_length=30, null=True, blank=True)
    horafin = models.CharField(max_length=30, null=True, blank=True)
    lugorigen = models.CharField(max_length=50, null=True, blank=True)
    lugdestino = models.CharField(max_length=50, null=True, blank=True)
    opcviaje = models.CharField(max_length=30, null=True, blank=True)
    grupo = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True


class Camposcomunes_detaildoc(models.Model):
    codigo = models.IntegerField(default=0)
    codpro = models.CharField(max_length=30, null=True, blank=True)
    descripcion = models.CharField(max_length=150, null=True, blank=True)
    unimed = models.CharField(max_length=60, null=True, blank=True)
    desunimed = models.CharField(max_length=60, null=True, blank=True)
    cantidad = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    precio = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impsubtotal = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impanticipos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impdescuentos = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impvalorventa = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    impisc = models.IntegerField(default=0, null=True, blank=True)
    impigv = models.IntegerField(default=0, null=True, blank=True)
    nvaligv = models.IntegerField(default=0, null=True, blank=True)
    impotroscargos = models.IntegerField(default=0, null=True, blank=True)
    impotrostributos = models.IntegerField(default=0, null=True, blank=True)
    imptotal = models.DecimalField(default=0, max_digits=15, decimal_places=2, null=True, blank=True)
    desgrupo1 = models.CharField(max_length=30, null=True, blank=True)
    desgrupo2 = models.CharField(max_length=30, null=True, blank=True)
    cc1 = models.CharField(max_length=30, null=True, blank=True)  # cc para saber donde se hace gasto
    cc2 = models.CharField(max_length=30, null=True, blank=True)
    cc3 = models.CharField(max_length=30, null=True, blank=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    horaini = models.CharField(max_length=30, null=True, blank=True)
    horafin = models.CharField(max_length=30, null=True, blank=True)
    lugorigen = models.CharField(max_length=50, null=True, blank=True)
    lugdestino = models.CharField(max_length=50, null=True, blank=True)
    opcviaje = models.CharField(max_length=30, null=True, blank=True)
    conductor = models.CharField(max_length=50, null=True, blank=True)
    nvuelo = models.CharField(max_length=50, null=True, blank=True)
    proveedor = models.CharField(max_length=50, null=True, blank=True)
    tipodoc = models.CharField(max_length=50, null=True, blank=True)
    obs = models.CharField(max_length=50, null=True, blank=True)
    modelo = models.CharField(max_length=60, blank=True, null=True)
    genero = models.CharField(max_length=30, blank=True, null=True)
    talla = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)
    estadodoc = models.ForeignKey('CotizacionEstado', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Camposcomunes_auditoria(models.Model):
    sucursal = models.CharField(max_length=10, blank=True, null=True)
    estado = models.IntegerField(default=0)
    anulado = models.IntegerField(default=0)
    fecregistro = models.DateField(null=True, blank=True)
    aud_idusu = models.CharField(max_length=30, blank=True, null=True)
    aud_feccre = models.DateTimeField(auto_now=True)
    aud_fecmod = models.DateField(null=True, blank=True)
    aud_feceli = models.DateField(null=True, blank=True)
    posmapa = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Camposcomunes_personal(models.Model):
    codigo = models.CharField(max_length=15, blank=True, null=True)
    ruc = models.CharField(max_length=15, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono1 = models.CharField(max_length=20, blank=True, null=True)
    telefono2 = models.CharField(max_length=20, blank=True, null=True)
    telefono3 = models.CharField(max_length=20, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telcontacto = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    correo = models.CharField(max_length=150, blank=True, null=True)
    paginaweb = models.CharField(max_length=150, blank=True, null=True)
    tipocc = models.IntegerField(default=0, blank=True, null=True)
    destipocc = models.CharField(max_length=100, blank=True, null=True)
    condcompvent = models.CharField(max_length=100, blank=True, null=True)
    banco_nombre1 = models.CharField(max_length=100, blank=True, null=True)
    banco_cuenta1 = models.CharField(max_length=100, blank=True, null=True)
    banco_moneda1 = models.CharField(max_length=20, blank=True, null=True)
    banco_nombre2 = models.CharField(max_length=100, blank=True, null=True)
    banco_cuenta2 = models.CharField(max_length=100, blank=True, null=True)
    banco_moneda2 = models.CharField(max_length=20, blank=True, null=True)
    fechanac = models.DateField(null=True, blank=True, help_text="Ingrese si esta activo u otro stado ")
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    grupo = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    idioma = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True


class Deposito(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30, blank=True, null=True)


# Unidades de Transporte
class Unidad(models.Model):
    codigo = models.CharField(max_length=15, blank=True, null=True)
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    placa = models.CharField(max_length=30, blank=True, null=True)
    npasajeros = models.CharField(max_length=150, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)
    foto1 = models.ImageField(upload_to='unidad', null=True, blank=True)
    foto2 = models.ImageField(upload_to='unidad', null=True, blank=True)


# Programa gastos,Mantenimiento para unidades
class Programagastos(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    unidad = models.CharField(max_length=30, blank=True, null=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)


class Programagasto(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=30, blank=True, null=True)
    unidad = models.CharField(max_length=30, blank=True, null=True)
    fechaini = models.DateField(null=True, blank=True)
    fechafin = models.DateField(null=True, blank=True)


class Material(models.Model):
    codigo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    cantidad = models.DecimalField(default=0, max_digits=15, decimal_places=4)
    color = models.CharField(max_length=2, default=0, choices=COLORES)
    descolor = models.CharField(max_length=60, blank=True, null=True)
    deposito = models.ForeignKey(Deposito, null=True, on_delete=models.SET_NULL)
    stock1 = models.IntegerField(default=0)
    codbarra = models.CharField(max_length=60, blank=True, null=True)
    stockalm1 = models.IntegerField(default=0)
    stockalm2 = models.IntegerField(default=0)
    stockalm3 = models.IntegerField(default=0)
    afectoigv = models.IntegerField(default=0)
    preciocosto = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    precioventa = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    aplicadscto = models.IntegerField(default=0)
    cc1 = models.CharField(max_length=60, blank=True, null=True)
    descc1 = models.CharField(max_length=60, blank=True, null=True)
    modelo = models.CharField(max_length=60, blank=True, null=True)
    genero = models.CharField(max_length=30, blank=True, null=True)
    talla = models.CharField(max_length=30, blank=True, null=True)
    ruc = models.CharField(max_length=11, blank=True, null=True)
    desruc = models.CharField(max_length=60, blank=True, null=True)
    unimed = models.CharField(max_length=30, blank=True, null=True)
    desunimed = models.CharField(max_length=30, blank=True, null=True)
    umdsali = models.CharField(max_length=30, blank=True, null=True)
    umdsaliconv = models.CharField(max_length=30, blank=True, null=True)
    monedacompra = models.IntegerField(default=0)  # soles,dolares,euros,yen
    desmonecompra = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)


class Articulo(models.Model):
    codigo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    cantidad = models.DecimalField(default=0, max_digits=15, decimal_places=4)
    color = models.CharField(max_length=2, default=0, choices=COLORES)
    descolor = models.CharField(max_length=60, blank=True, null=True)
    deposito = models.ForeignKey(Deposito, null=True, on_delete=models.SET_NULL)
    stock1 = models.IntegerField(default=0)
    codbarra = models.CharField(max_length=60, blank=True, null=True)
    stockalm1 = models.IntegerField(default=0)
    stockalm2 = models.IntegerField(default=0)
    stockalm3 = models.IntegerField(default=0)
    afectoigv = models.IntegerField(default=0)
    preciocosto = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    precioventa = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    aplicadscto = models.IntegerField(default=0)
    cc1 = models.CharField(max_length=60, blank=True, null=True)
    descc1 = models.CharField(max_length=60, blank=True, null=True)
    modelo = models.CharField(max_length=60, blank=True, null=True)
    genero = models.CharField(max_length=30, blank=True, null=True)
    talla = models.CharField(max_length=30, blank=True, null=True)
    ruc = models.CharField(max_length=11, blank=True, null=True)
    desruc = models.CharField(max_length=60, blank=True, null=True)
    unimed = models.CharField(max_length=30, blank=True, null=True)
    desunimed = models.CharField(max_length=30, blank=True, null=True)
    umdsali = models.CharField(max_length=30, blank=True, null=True)
    umdsaliconv = models.CharField(max_length=30, blank=True, null=True)
    monedaventa = models.IntegerField(default=0)  # soles,dolares,euros,yen
    desmoneventa = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=60, blank=True, null=True)


class Centrodecosto1(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    totingresos = models.IntegerField(default=0)
    totgastos = models.IntegerField(default=0)


class Banco(models.Model):
    codigo = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=60, blank=True, null=True)


# centro de costo para monitor de flujo gasto ingreso


class Cliente(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Proveedor(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Transporte(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


class Chofer(Camposcomunes_personal, Camposcomunes_auditoria):
    pass


# ARCHIVOS DE MOVIMIENTO COTIZACIONES O PRODUCTOS

class Mcotizacion(Camposcomunes_masterdoc, Camposcomunes_auditoria):
    pass


class Dcotizacion(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    master = models.ForeignKey(Mcotizacion, related_name='cotizaciones', on_delete=models.CASCADE, null=True)


# ARCHIVOS DE MOVIMIENTO MATERIALES

class Mmateriales(Camposcomunes_masterdoc, Camposcomunes_auditoria):
    pass


class Dmateriales(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    master = models.ForeignKey(Mmateriales, related_name='materiales', on_delete=models.CASCADE, null=True)


class Mguia(models.Model):
    pass


class Dguia(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    pass


class Mgasto(models.Model):
    pass


class Dgasto(Camposcomunes_detaildoc, Camposcomunes_auditoria):
    pass


class Clientesdireccion(models.Model):
    master = models.ForeignKey(Cliente, related_name='clientesdirecciones', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)

    class Meta:
        unique_together = ('master', 'id')
        ordering = ['id']

    def __unicode__(self):
        return '%d: %s' % (self.direccion, self.telefono)


class CotizacionEstado(models.Model):
    name = models.CharField(max_length=254)
    color = models.CharField(max_length=100)


class MaterialesEstado(models.Model):
    name = models.CharField(max_length=254)
    color = models.CharField(max_length=100)

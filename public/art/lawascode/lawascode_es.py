#!/usr/bin/env python3
"""
# ---------------------------------------------------------------------------
#                         LEY COMO CÓDIGO (MADRID)
#            Código Civil, 1889 -- compilado en Python
#
#  Este programa es un compilador. No compila fuente a código máquina.
#  Compila el deseo humano en propiedad legal.
#
#  Cada función es un artículo. Cada excepción es una nulidad.
#  Cada comentario es una glosa de notario.
#
#  Para ejecutar:   python3 lawascode_es.py
#  Para leer:       ábrelo en cualquier editor. La ley es el código.
# ---------------------------------------------------------------------------
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, List, Dict
from datetime import datetime


# ===========================================================================
#  LEYES ESTATALES -- El Estado español habla primero.
# ===========================================================================

class CodigoCivil1889:
    """
    Artículo 348: El propietario de una cosa tiene derecho a gozar y disponer
    de ella con exclusión de terceros, salvo las limitaciones establecidas
    en las leyes.

    # NOTA: La propiedad no es absoluta. El Código Civil la circunscribe.
    #       Como el alma, la propiedad tiene límites que ella misma no elige.
    """
    @staticmethod
    def validate_sale_consideration(price: float) -> bool:
        return price > 0.0  # Cero euros es una donación, no una venta.


class LeyHipotecaria1946:
    """
    Artículo 1: El Registro de la Propiedad tiene por objeto la inscripción
    o anotación de los actos y contratos relativos al dominio y demás derechos
    reales sobre bienes inmuebles.

    # NOTA: En España, el Registro de la Propiedad es la fe pública registral.
    #       Sin inscripción, la compraventa no oponible a terceros.
    #       La fe pública del notario no basta; hace falta la del registro.
    """
    @staticmethod
    def verify_registry_inscription(deed: Escritura, registry: str) -> bool:
        """
        La escritura no vive hasta que el Registrador la inscribe.
        Madrid tiene 26 registros de la propiedad.
        Cada uno con su propio índice, sus propias colas, su propio silencio.
        """
        return deed.is_inscribed and deed.registry_office == registry

    @staticmethod
    def verify_notarial_public_deed(deed: Escritura) -> bool:
        """
        Artículo 146 LH: Los actos y contratos de enajenación deben
        otorgarse en escritura pública para su inscripción.

        # NOTA: El notario no valida la legalidad; da fe de las partes.
        #       Pero sin escritura pública, no hay entrada al registro.
        #       Es el umbral. La puerta de entrada.
        """
        return deed.is_public_deed and deed.notary_name != ""


class LeyEnjuiciamientoCivil2000:
    """
    Artículo 250: Son bienes inmuebles por su naturaleza, los terrenos,
    construcciones, minas y demás pertenencias.

    # NOTA: El proceso civil español protege la posesión y la propiedad.
    #       La posesión es el hecho; la propiedad es el derecho.
    """
    pass  # Marcador conceptual. El procedimiento es el alma del derecho.


class LeyArrendamientosUrbanos1994:
    """
    LAU: Regula los contratos de arrendamiento de vivienda y de locales.

    # NOTA: En España, alquilar es distinto de comprar, pero la ley protege
    #       al arrendatario de vivienda con fuerza casi posesoria.
    #       El inquilino débil tiene la fuerza del Estado.
    """
    @staticmethod
    def verify_tenancy_term(years: int) -> bool:
        """Artículo 9 LAU: Duración mínima de 5 años para vivienda habitual."""
        return years >= 5


class LeyConsumidores1999:
    """
    Ley 7/1999: Protección de los consumidores en la compra de vivienda.

    # NOTA: El comprador de vivienda es consumidor si compra para habitar.
    #       El promotor debe entregar la vivienda en plazo; si no, indemnización.
    """
    @staticmethod
    def verify_consumer_deadline(delivery_date: datetime, promised: datetime) -> bool:
        """El plazo de entrega es sagrado cuando el comprador es persona física."""
        return delivery_date <= promised


# ===========================================================================
#  MADRID AUTONÓMICO -- La Comunidad habla después. Su voz es local.
# ===========================================================================

class LeySueloMadrid2001:
    """
    Ley 9/2001, de 17 de julio, del Suelo y de Ordenación Urbanística
    de la Comunidad de Madrid.

    # NOTA: Madrid tiene su propio planeamiento. El PGOU (Plan General de
    #       Ordenación Urbana) divide el suelo en urbano, urbanizable y rústico.
    #       Cualquier parcela tiene una calificación urbanística.
    """
    @staticmethod
    def verify_urban_qualification(qualification: str) -> bool:
        """
        El suelo debe estar calificado para el uso previsto.
        Suelo rústico no puede ser vivienda sin requalificación.
        """
        return qualification.lower() in ("urbano", "urbanizable")


class NormativaVPOComunidadMadrid:
    """
    Vivienda de Protección Oficial (VPO) -- régimen de precio limitado.

    # ADVERTENCIA: Las VPO tienen precio limitado y restricciones de venta.
    #              No pueden venderse libremente hasta cumplir el plazo de
    #              vigencia (normalmente 10-30 años según convocatoria).
    #              Una VPO no liberada es una promesa que no puede cumplirse.
    """
    @staticmethod
    def is_vpo_restricted(vpo_type: str) -> bool:
        return vpo_type.upper().startswith("VPO")

    @staticmethod
    def can_transfer_vpo(vpo_restricted: bool, liberation_years: int, required: int = 10) -> bool:
        if not vpo_restricted:
            return True
        # ERROR: No se puede enajenar una VPO sin cumplir el plazo de vigencia.
        #        ^^^ Type mismatch: se esperaba 'libre mercado', se obtuvo 'restringido'
        #        Solución: Esperar. O solicitar liberación a la Comunidad de Madrid.
        return liberation_years >= required


class PlusvaliaMunicipalMadrid:
    """
    Impuesto sobre el Incremento de Valor de los Terrenos de Naturaleza Urbana.
    Gestiona el Ayuntamiento de Madrid.

    # NOTA: La plusvalía municipal grava el incremento de valor del suelo.
    #       Es municipal, no estatal. Cada ayuntamiento tiene sus propias tablas.
    #       Madrid ha sufrido reformas recientes (sentencia del TC 2021).
    """
    @classmethod
    def calculate_plusvalia(cls, cadastral_value: float, years_held: int) -> float:
        """
        Cálculo objetivo basado en valor catastral y años de tenencia.
        Madrid aplica coeficientes por baremo municipal.
        """
        # Simplificación artística del cálculo objetivo
        coef = min(years_held * 0.034, 0.45)  # Coeficiente creciente con techo
        return cadastral_value * coef * 0.26  # Tipo impositivo aproximado Madrid


class ITEComunidadMadrid:
    """
    Inspección Técnica de Edificios -- obligatoria para edificios > 50 años.
    Ley 8/2013, de 26 de junio, de Rehabilitación del Suelo Urbano de Madrid.

    # NOTA: Sin ITE positiva, no se puede vender con garantía.
    #       El edificio viejo debe demostrar que no se cae.
    """
    @staticmethod
    def verify_ite_passed(building_age: int, ite_status: str) -> bool:
        if building_age < 50:
            return True  # No obligatoria
        return ite_status.lower() in ("favorable", "positiva", "sin defectos")


class CedulaHabitabilidadMadrid:
    """
    Cédula de Habitabilidad / Cédula de Primera Ocupación.

    # NOTA: Para viviendas nuevas o rehabilitadas, es obligatoria.
    #       El Ayuntamiento de Madrid la expide. Sin ella, no se puede habitar.
    #       Es el acta de nacimiento domiciliaria.
    """
    @staticmethod
    def verify_habitability(has_cedula: bool, is_new: bool) -> bool:
        if not is_new:
            return True  # Para reventa, no siempre obligatoria
        return has_cedula


class CertificadoEnergetico:
    """
    Real Decreto 235/2013: Certificado de Eficiencia Energética obligatorio
    en venta y alquiler de edificios.

    # NOTA: La etiqueta energética (A-G) es obligatoria desde 2013.
    #       Sin certificado, la venta es válida pero sancionable.
    """
    VALID_LABELS = ("A", "B", "C", "D", "E", "F", "G")

    @classmethod
    def verify_energy_label(cls, label: Optional[str]) -> bool:
        return label is not None and label.upper() in cls.VALID_LABELS


# ===========================================================================
#  FISCALIDAD -- La Hacienda Pública siempre habla.
# ===========================================================================

class ITPvsIVA:
    """
    ITP (Impuesto sobre Transmisiones Patrimoniales) -- 6% en Madrid para vivienda usada.
    IVA -- 10% para vivienda nueva (promotor), 21% para locales comerciales.

    # NOTA: Madrid tiene un ITP más bajo que otras comunidades (Andalucía 8-10%).
    #       Es una ventaja fiscal de la capital. El Estado cede; Madrid atrae.
    """
    ITP_RATE_MADRID: float = 0.06
    IVA_VIVIENDA_NUEVA: float = 0.10
    IVA_LOCAL_COMERCIAL: float = 0.21

    @classmethod
    def calculate_transfer_tax(cls, price: float, is_new: bool, is_commercial: bool) -> Dict[str, float]:
        if is_commercial:
            tax = price * cls.IVA_LOCAL_COMERCIAL
            return {"type": "IVA", "rate": cls.IVA_LOCAL_COMERCIAL, "amount": tax}
        if is_new:
            tax = price * cls.IVA_VIVIENDA_NUEVA
            return {"type": "IVA", "rate": cls.IVA_VIVIENDA_NUEVA, "amount": tax}
        tax = price * cls.ITP_RATE_MADRID
        return {"type": "ITP", "rate": cls.ITP_RATE_MADRID, "amount": tax}


class IBI_Madrid:
    """
    Impuesto sobre Bienes Inmuebles -- gestionado por el Ayuntamiento de Madrid.

    # NOTA: El IBI debe estar al día para vender sin gravámenes.
    #       El Ayuntamiento de Madrid es el acreedor silencioso de cada finca.
    """
    @staticmethod
    def verify_no_tax_debt(debt_amount: float) -> bool:
        return debt_amount == 0.0


class AJD_Madrid:
    """
    Actos Jurídicos Documentados -- gestionado por la Comunidad de Madrid.
    Grava las escrituras públicas sometidas a ITP.

    # NOTA: En Madrid, AJD es del 0.75% para vivienda habitual.
    #       Es el sello del Estado sobre el sello del notario.
    """
    AJD_RATE: float = 0.0075

    @classmethod
    def calculate_ajd(cls, price: float) -> float:
        return price * cls.AJD_RATE


# ===========================================================================
#  USO DEL SUELO -- Urbano, urbanizable, rústico. Madrid tiene sus zonas.
# ===========================================================================

class CalificacionSuelo(Enum):
    URBANO = auto()
    URBANIZABLE = auto()
    RUSTICO = auto()
    PROTEGIDO = auto()


class RequalificationRequired(Exception):
    """
    Ley del Suelo: El suelo rústico no puede edificarse sin requalificación.

    # ERROR: Calificación insuficiente.
    #        ^^^ Semantic error: 'SueloRustico' no puede convertirse implícitamente a 'ParcelaVivienda'
    #        Pista: Solicitar modificación de calificación al Ayuntamiento de Madrid.
    #               Esperar. Pagar. Esperar más.
    """
    pass


class RegimenPropiedad(Enum):
    """
    Propiedad plena: dominio absoluto.
    Propiedad horizontal: para edificios de viviendas (comunidad de propietarios).

    # NOTA: La propiedad horizontal es la forma española de dividir un edificio.
    #       Cada piso es una finca registral. La escalera es de todos.
    """
    PLENA = "plena"
    HORIZONTAL = "horizontal"


# ===========================================================================
#  ESTRUCTURAS DE DATOS -- Los átomos de la propiedad española.
# ===========================================================================

@dataclass
class ReferenciaCatastral:
    """Cada finca tiene una referencia catastral. El Catastro la cuenta."""
    ref_catastral: str  # 20 caracteres alfanuméricos
    municipio: str
    provincia: str
    poligono: str
    parcela: str


@dataclass
class Inmueble:
    """
    Bien inmueble según el Código Civil español: terrenos, construcciones,
    minas y sus accesorios adheridos al suelo.

    # NOTA: Un árbol en pie es inmueble. La leña cortada es mueble.
    #       El mismo objeto cambia de naturaleza jurídica al separarse del suelo.
    """
    catastro: ReferenciaCatastral
    metros_cuadrados: float
    calificacion: CalificacionSuelo
    requalificado: bool = False
    es_vpo: bool = False
    regimen: RegimenPropiedad = RegimenPropiedad.PLENA
    valor_catastral: float = 0.0
    valor_mercado: float = 0.0
    anios_edificio: int = 0


@dataclass
class Parte:
    """Una persona ante la ley. La ley no pregunta si sueña."""
    nombre: str
    es_promotor: bool = False
    es_administracion: bool = False


@dataclass
class Escritura:
    """
    La escritura pública es el instrumento de transferencia.
    Sin ella, no hay fe pública. Sin fe pública, no hay registro.

    # NOTA: Dos firmas ante notario. El notario da fe de identidad,
    #       de capacidad, y de que las partes comparecieron.
    #       La cadena de confianza empieza en el protocolo notarial.
    """
    escritura_numero: str
    fecha_otorgamiento: datetime
    vendedor: Parte
    comprador: Parte
    inmueble: Inmueble
    precio_venta: float
    firma_notario: str = ""
    es_escritura_publica: bool = False
    inscrita_registro: bool = False
    oficina_registro: str = ""
    itp_pagado: float = 0.0
    ajd_pagado: float = 0.0
    plusvalia_pagada: float = 0.0
    cedula_habitabilidad: bool = False
    certificado_energetico: Optional[str] = None
    ite_status: Optional[str] = None
    cargas: List[str] = field(default_factory=list)


# ===========================================================================
#  EL COMPILADOR -- Donde la ley se vuelve ejecutable.
# ===========================================================================

class ErrorCompilacion:
    """Un defecto en el código fuente legal. Diagnosticado como IDE."""
    def __init__(self, fichero: str, linea: int, severidad: str, codigo: str, mensaje: str):
        self.fichero = fichero
        self.linea = linea
        self.severidad = severidad  # ERROR, WARNING, INFO
        self.codigo = codigo
        self.mensaje = mensaje

    def __str__(self) -> str:
        return f"{self.fichero}:{self.linea}: {self.severidad}: [{self.codigo}] {self.mensaje}"


class CompiladorLegalEspana:
    """
    El compilador lee una escritura como fuente y produce:
        (a) un título válido -- compilación limpia, o
        (b) un log de diagnóstico -- los errores que impiden la existencia legal.

    Cada método es un filtro estatutario. La escritura debe pasar todos
    para compilarse en un título mercantil.
    """

    def __init__(self):
        self.diagnosticos: List[ErrorCompilacion] = []
        self.fichero_actual = "escritura.py"
        self._contador_linea = 0

    def _emitir(self, severidad: str, codigo: str, mensaje: str):
        self._contador_linea += 1
        err = ErrorCompilacion(
            fichero=self.fichero_actual,
            linea=self._contador_linea,
            severidad=severidad,
            codigo=codigo,
            mensaje=mensaje,
        )
        self.diagnosticos.append(err)

    def compilar(self, escritura: Escritura) -> bool:
        """
        Compila una escritura en un título.
        Devuelve True si el título es mercantil (compilación limpia).
        Devuelve False si hay defectos (compilación fallida).
        """
        print("=" * 72)
        print("COMPILADOR LEGAL -- EDICIÓN MADRID")
        print(f"Compilando escritura {escritura.escritura_numero}...")
        print("=" * 72)
        print()

        # -- Fase 1: Análisis Léxico -----------------------------------------
        # ¿Se puede leer el documento? ¿Es público? ¿Está firmado?
        self._check_escritura_publica(escritura)
        self._check_consideracion(escritura)

        # -- Fase 2: Análisis Semántico -- Cumplimiento Estatutario ----------
        self._check_inscripcion_registro(escritura)
        self._check_impuestos(escritura)
        self._check_calificacion_suelo(escritura)
        self._check_vpo(escritura)
        self._check_regimen_propiedad(escritura)
        self._check_ite(escritura)
        self._check_cedula_habitabilidad(escritura)
        self._check_certificado_energetico(escritura)
        self._check_cargas(escritura)

        # -- Fase 3: Enlace -- Catastro e Impuestos Locales -------------------
        self._check_ibi_al_dia(escritura)

        # -- Informe de Compilación ------------------------------------------
        print()
        print("-" * 72)
        errores = [d for d in self.diagnosticos if d.severidad == "ERROR"]
        advertencias = [d for d in self.diagnosticos if d.severidad == "WARNING"]
        infos = [d for d in self.diagnosticos if d.severidad == "INFO"]

        for d in self.diagnosticos:
            print(d)

        print()
        print(f"Compilación completa: {len(errores)} error(es), {len(advertencias)} advertencia(s), {len(infos)} nota(s).")
        if errores:
            print("TÍTULO NO MERCANTIL. Compilación fallida.")
            print()
            print("# La finca existe en el mundo físico,")
            print("# pero aún no existe en el mundo jurídico.")
            print("# El código se niega a compilar el anhelo en propiedad.")
            return False
        else:
            print("COMPILACIÓN LIMPIA. Título mercantil.")
            print()
            print("# La escritura ha pasado por la maquinaria estatutaria.")
            print("# El Estado reconoce: esta tierra tiene dueño.")
            return True

    # -- Comprobaciones Estatutarias Individuales --------------------------

    def _check_escritura_publica(self, escritura: Escritura):
        if not escritura.es_escritura_publica:
            self._emitir(
                "ERROR", "LH1946-EP",
                f"Escritura {escritura.escritura_numero} NO ES PÚBLICA. "
                "Art. 146 LH: La enajenación requiere escritura pública para inscribirse. "
                "Sin escritura pública, no hay fe. Sin fe, no hay registro."
            )
            # =================================================================
            #  ERROR: la escritura pública es el acta de nacimiento del contrato.
            #         Sin ella, el documento es un borrador sin fuerza.
            #         ^^^ Semantic error: escritura.tipo == 'privada'
            #         Pista: Comparecer ante Notario. Identificarse. Firmar. Pagar.
            #                El notario es el compilador humano. No se puede evitar.
            # =================================================================
        elif not escritura.firma_notario:
            self._emitir(
                "ERROR", "LH1946-NOT",
                "Escritura pública sin firma de notario. El notario da fe pública. "
                "Sin su firma, la escritura es un papel sin alma."
            )
        else:
            self._emitir("INFO", "LH1946-OK", f"Escritura pública ante Notario {escritura.firma_notario}.")

    def _check_consideracion(self, escritura: Escritura):
        if not CodigoCivil1889.validate_sale_consideration(escritura.precio_venta):
            self._emitir(
                "ERROR", "CC1889-PRECIO",
                "Precio de venta cero o no especificado. "
                "Art. 1445 CC: El precio debe ser cierto o determinable."
            )
        else:
            self._emitir("INFO", "CC1889-OK", f"Precio de EUR {escritura.precio_venta:,.2f} es válido.")

    def _check_inscripcion_registro(self, escritura: Escritura):
        if not escritura.inscrita_registro:
            self._emitir(
                "ERROR", "LH1946-NOREG",
                f"Escritura {escritura.escritura_numero} NO INSCRITA. "
                "Art. 38 LH: La inscripción es necesaria para que el derecho "
                "se oponga a terceros. Sin inscripción, la compra es válida pero frágil."
            )
            # =================================================================
            #  ERROR: la inscripción registral es el escudo contra el mundo.
            #         Sin ella, un tercero de buena fe puede tener mejor derecho.
            #         ^^^ Semantic error: escritura.inscrita == False
            #         Pista: Acudir al Registro de la Propiedad. Presentar escritura.
            #                Pagar tasas. Esperar la presentación. El registro habla.
            # =================================================================
        else:
            self._emitir("INFO", "LH1946-REG", f"Inscrita en Registro: {escritura.oficina_registro}")

    def _check_impuestos(self, escritura: Escritura):
        tax_info = ITPvsIVA.calculate_transfer_tax(
            escritura.precio_venta,
            is_new=False,  # Simplificación: asumimos reventa
            is_commercial=False
        )
        required_itp = tax_info["amount"]
        if escritura.itp_pagado < required_itp:
            deficit = required_itp - escritura.itp_pagado
            self._emitir(
                "ERROR", "ITP-MADRID",
                f"Déficit de ITP de EUR {deficit:,.2f}. "
                f"Pagado EUR {escritura.itp_pagado:,.2f}, requerido EUR {required_itp:,.2f}. "
                "El ITP es el precio de la seguridad jurídica en Madrid."
            )
        else:
            self._emitir("INFO", "ITP-OK", f"ITP satisfecho (EUR {escritura.itp_pagado:,.2f}).")

        required_ajd = AJD_Madrid.calculate_ajd(escritura.precio_venta)
        if escritura.ajd_pagado < required_ajd:
            deficit = required_ajd - escritura.ajd_pagado
            self._emitir(
                "ERROR", "AJD-MADRID",
                f"Déficit de AJD de EUR {deficit:,.2f}. "
                "Los Actos Jurídicos Documentados gravan la fe pública. "
                "Sin pagarlos, la escritura no tiene sello completo."
            )
        else:
            self._emitir("INFO", "AJD-OK", f"AJD satisfecho (EUR {escritura.ajd_pagado:,.2f}).")

    def _check_calificacion_suelo(self, escritura: Escritura):
        inm = escritura.inmueble
        if inm.calificacion == CalificacionSuelo.RUSTICO and not inm.requalificado:
            self._emitir(
                "ERROR", "LS2001-CALIF",
                f"Finca ref. {inm.catastro.ref_catastral} es suelo RÚSTICO "
                f"sin requalificación. Ley 9/2001 Madrid: suelo rústico no edificable. "
                "El Ayuntamiento de Madrid debe autorizar el cambio de calificación."
            )
            # =================================================================
            #  WARNING: La calificación urbanística es el ADN de la parcela.
            #           Sin requalificación, la tierra sueña con ser casa
            #           pero despierta siendo campo.
            #           ^^^ TypeError: no se puede convertir 'SueloRustico' a 'ParcelaUrbana'
            #           sin RequalificacionUrbanistica(solicitar=True, esperar=infinito)
            # =================================================================
        elif inm.calificacion == CalificacionSuelo.RUSTICO and inm.requalificado:
            self._emitir("INFO", "LS2001-OK", "Requalificación urbanística concedida.")

    def _check_vpo(self, escritura: Escritura):
        inm = escritura.inmueble
        if inm.es_vpo:
            self._emitir(
                "ERROR", "VPO-MADRID",
                f"Finca ref. {inm.catastro.ref_catastral} es Vivienda de Protección Oficial. "
                "Normativa VPO Comunidad de Madrid: enajenación restringida hasta liberación. "
                "El título es nulo de pleno derecho si no se cumple el plazo de vigencia."
            )
            # =================================================================
            #  FATAL ERROR: Vivienda de Protección Oficial detectada.
            #               ^^^ Esta vivienda fue entregada a una familia con precio limitado.
            #                   La Comunidad de Madrid recuerda. La enajenación no es defectuosa;
            #                   es imposible. No hay arreglo. Solo hay esperar o solicitar liberación.
            # =================================================================

    def _check_regimen_propiedad(self, escritura: Escritura):
        if escritura.inmueble.regimen == RegimenPropiedad.HORIZONTAL:
            self._emitir(
                "WARNING", "PH-CP",
                "Régimen de Propiedad Horizontal detectado. "
                "Verificar que la comunidad de propietarios está al corriente de cuotas. "
                "Sin certificación de la comunidad, la venta es arriesgada."
            )
            # =================================================================
            #  WARNING: La Propiedad Horizontal es la sociedad forzosa de vecinos.
            #           No es ilegal, pero tiene deudas ocultas: la escalera, el ascensor,
            #           la reparación del tejado. La cuota pendiente es una hipoteca social.
            #           ^^^ DeprecationWarning: RegimenPropiedad.HORIZONTAL requiere
            #               certificación de la comunidad y cuotas al día.
            # =================================================================
        else:
            self._emitir("INFO", "PH-OK", "Propiedad plena. Sin comunidad de vecinos.")

    def _check_ite(self, escritura: Escritura):
        inm = escritura.inmueble
        if inm.anios_edificio >= 50:
            if not ITEComunidadMadrid.verify_ite_passed(inm.anios_edificio, escritura.ite_status):
                self._emitir(
                    "ERROR", "ITE-MADRID",
                    f"Edificio de {inm.anios_edificio} años sin ITE favorable. "
                    "Ley 8/2013 Madrid: ITE obligatoria para edificios > 50 años. "
                    "Sin ITE, la venta carece de garantía estructural."
                )
            else:
                self._emitir("INFO", "ITE-OK", f"ITE favorable para edificio de {inm.anios_edificio} años.")

    def _check_cedula_habitabilidad(self, escritura: Escritura):
        if escritura.inmueble.anios_edificio < 5 and not escritura.cedula_habitabilidad:
            self._emitir(
                "WARNING", "CEDULA-MADRID",
                "Vivienda nueva o rehabilitada sin Cédula de Habitabilidad. "
                "El Ayuntamiento de Madrid exige cédula para primera ocupación. "
                "Sin ella, no se puede habitar legalmente."
            )
        elif escritura.cedula_habitabilidad:
            self._emitir("INFO", "CEDULA-OK", "Cédula de Habitabilidad en vigor.")

    def _check_certificado_energetico(self, escritura: Escritura):
        if not CertificadoEnergetico.verify_energy_label(escritura.certificado_energetico):
            self._emitir(
                "WARNING", "CEE-RD235",
                f"Certificado energético ausente o inválido: '{escritura.certificado_energetico}'. "
                "RD 235/2013: obligatorio en venta y alquiler. Etiqueta A-G requerida. "
                "Sin certificado, la venta es válida pero sancionable."
            )
        else:
            self._emitir("INFO", "CEE-OK", f"Certificado energético: {escritura.certificado_energetico}.")

    def _check_cargas(self, escritura: Escritura):
        if escritura.cargas:
            for carga in escritura.cargas:
                self._emitir(
                    "WARNING", "CARGA-REG",
                    f"Carga sobre el título: {carga}. "
                    "Nota simple registral muestra hipoteca/carga previa. "
                    "Mercantilidad condicionada a cancelación."
                )
        else:
            self._emitir("INFO", "CARGA-OK", "Nota simple registral limpia de cargas.")

    def _check_ibi_al_dia(self, escritura: Escritura):
        self._emitir(
            "INFO", "IBI-MADRID",
            f"Verificar IBI al día en Ayuntamiento de Madrid. "
            f"Ref. catastral: {escritura.inmueble.catastro.ref_catastral}. "
            "El IBI es la cara fiscal de la propiedad."
        )


# ===========================================================================
#  TRANSACCIÓN DE EJEMPLO -- Una escritura defectuosa. El arte está en el fallo.
# ===========================================================================

def main():
    """
    Aquí hay una transmisión de propiedad. Es hermosa en sus defectos.
    Como un cuerpo con cicatrices, cuenta la historia de lo que la ley permite
    y lo que prohíbe.

    # NOTA: Esta escritura es INTENCIONADAMENTE defectuosa. Ejecutar el compilador
    #       producirá errores. Los errores SON el arte.
    #       Cada error es un verso en el poema del derecho inmobiliario.
    """

    catastro = ReferenciaCatastral(
        ref_catastral="12345A6789012BCDEF3GH",
        municipio="Madrid",
        provincia="Madrid",
        poligono="15",
        parcela="234",
    )

    la_finca = Inmueble(
        catastro=catastro,
        metros_cuadrados=85.0,
        calificacion=CalificacionSuelo.RUSTICO,  # Pero se vende como vivienda!
        requalificado=False,                     # ^^^ ERROR aquí
        es_vpo=True,                             # ^^^ ERROR FATAL aquí
        regimen=RegimenPropiedad.HORIZONTAL,     # ^^^ ADVERTENCIA aquí
        valor_catastral=180_000.0,
        valor_mercado=450_000.0,
        anios_edificio=65,                       # ^^^ ITE obligatoria
    )

    # El vendedor es un promotor. Pero no hay escritura pública.
    # ^^^ ERROR: promover() llamado sin escritura pública.
    #            El edificio se anuncia pero no existe en el protocolo notarial.
    vendedor = Parte(nombre="Promociones Chamartin SL", es_promotor=True)

    comprador = Parte(nombre="Ana García López")

    escritura_defectuosa = Escritura(
        escritura_numero="M-2024-44592",
        fecha_otorgamiento=datetime(2024, 3, 15),
        vendedor=vendedor,
        comprador=comprador,
        inmueble=la_finca,
        precio_venta=450_000.0,
        firma_notario="",          # Sin notario. Sin fe pública.
                                   # ^^^ ERROR: escritura.firma_notario está vacía.
        es_escritura_publica=False,  # Escritura privada. No inscribible.
                                     # ^^^ ERROR: escritura.tipo == 'privada'
        inscrita_registro=False,    # No inscrita en el Registro de la Propiedad.
                                    # ^^^ ERROR: escritura.inscrita == False
        oficina_registro="",
        itp_pagado=10_000.0,        # Muy por debajo de los ~EUR 27,000 requeridos.
                                    # ^^^ ERROR: ITP insuficiente.
        ajd_pagado=0.0,             # AJD no pagado.
                                    # ^^^ ERROR: AJD pendiente.
        plusvalia_pagada=0.0,
        cedula_habitabilidad=False,  # Vivienda nueva sin cédula.
                                     # ^^^ ADVERTENCIA: falta cédula.
        certificado_energetico=None,  # Sin etiqueta energética.
                                      # ^^^ ADVERTENCIA: certificado ausente.
        ite_status="deficiente",    # ITE desfavorable.
                                    # ^^^ ERROR: ITE no favorable.
        cargas=["Hipoteca a Banco Santander, 2021, EUR 280,000"],
                                    # ^^^ ADVERTENCIA: carga registral previa.
    )

    compilador = CompiladorLegalEspana()
    compilador.compilar(escritura_defectuosa)

    # =======================================================================
    #  OBSERVACIÓN FINAL: Este programa no simula la ley.
    #                     La ejecuta. Las excepciones son reales.
    #                     La nulidad es real. La VPO es real.
    #                     Cuando lo ejecutas, ves lo que ve el Estado:
    #                     un documento que quiere ser propiedad pero aún no lo es.
    #
    #  Para que compile limpio, corrige los errores anteriores:
    #    - Otorgar escritura pública ante Notario.
    #    - Inscribir en Registro de la Propiedad de Madrid.
    #    - Pagar ITP completo (EUR 27,000+).
    #    - Pagar AJD (EUR 3,375 aprox.).
    #    - Obtener requalificación urbanística del Ayuntamiento de Madrid.
    #    - Verificar que NO es VPO (o solicitar liberación).
    #    - Obtener ITE favorable (edificio > 50 años).
    #    - Obtener Cédula de Habitabilidad.
    #    - Obtener Certificado Energético (etiqueta A-G).
    #    - Cancelar hipoteca con Banco Santander.
    #    - Certificar cuotas al día de la comunidad (Propiedad Horizontal).
    #
    #  Hasta entonces, la tierra es un poema que el compilador se niega a parsear.
    # =======================================================================


if __name__ == "__main__":
    main()

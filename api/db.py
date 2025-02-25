from typing import List
from uuid import uuid4
from api.models import Aplicacion


db: List[Aplicacion] = [
    Aplicacion(
        id=uuid4(),
        nombre="pangea",
        descripcion="44444444",
        url="pangea@correo.com",
        marca="des_soe_panea",
        dominio="des_soe_pangea",
        responsable = "juan",
        first_nivel = [
            {
                "nombre": "smc",
                "soporte": {
                    "nombre": "soporte1",
                    "grupo_remedy": "grupo1",
                    "telefono": "123456789",
                    "correo": "soporte@correo.com"
                }
            },
            {
                "nombre": "tmc",
                "soporte": {
                    "nombre": "soporte2",
                    "grupo_remedy": "grupo2",
                    "telefono": "123456789",
                    "correo": "soporte2@correo.com"
                }
            }             
        ],
        second_nivel = [],
        tercer_nivel = [],
        coordinador= [],
        horario_servicio="24x7",
        horario_atencion="24x7",
        ventana_intervencion="24x7",
        ventana_intervencion_semanal="24x7",
        ventana_intervencion_mensual="24x7",
        observaciones="observaciones",
        centro_afectado="centro_afectado",
        impacto_negocio="impacto_neg",
    ),
]

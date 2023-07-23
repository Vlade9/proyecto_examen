# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError



class ModelTratamiento(models.Model):
    _name = 'model.tratamiento'
    _rec_name = "codigo_tratamiento"


    codigo_tratamiento = fields.Char(string="Codigo de tratamiento")
    nombre_tratamiento = fields.Char(string="Nombre de tratamiento")
    medico_tratante = fields.Char(string="Medico tratante")


    @api.constrains('codigo_tratamiento')
    def _check_codigo_tratamiento(self):
        for item in self:
            if "026" in item.codigo_tratamiento:
                raise ValidationError('El Codigo de tratamiento no debe contener 026 en su valor.')




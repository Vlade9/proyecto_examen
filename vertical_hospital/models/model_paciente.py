# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError



class ModelPaciente(models.Model):
    _name = 'model.paciente'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = "dni"


    code = fields.Char(string="Secuencia", default=lambda self: self.env['ir.sequence'].next_by_code('model.paciente'), readonly=True)
    name = fields.Char(string="Nombre y Apellidos")
    dni = fields.Char(string="DNI")
    tratamiento_ids = fields.Many2many(comodel_name='model.tratamiento', required=True, string="Tratamientos")
    fecha_alta = fields.Datetime(string="Fecha y hora de alta")
    fecha_actualizacion = fields.Datetime(string="Fecha y hora de actualizacion")
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('alta', 'Alta'),
        ('baja', 'Baja'),
    ], string='Estado', default='draft', track_visibility='onchange', copy=False)
    # tracking=True


    @api.constrains('dni')
    def _check_dni(self):
        for item in self:
            if not item.dni.isnumeric():
                raise ValidationError('El DNI no debe contener letras en su valor.')



    def getPaciente(self, codigo):
        result = self.sudo().search([('code', '=', codigo)])
        if result:
            return {
                "seq": result.code,
                "name": result.name,
                "dni": result.dni,
                "state": result.state
            }
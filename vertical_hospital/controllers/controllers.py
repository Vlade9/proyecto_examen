# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import requests
import json


class HospitalController(http.Controller):

    @http.route('/pacientes/consulta/<string:secuencia>', type='http', auth="none")
    def get_paciente(self, secuencia):
        result = request.env['model.paciente'].sudo().search([('code', '=', secuencia)])
        data = {}
        if result:
            data.update({
                "seq": result.code,
                "name": result.name,
                "dni": result.dni,
                "state": result.state
            })
        return request.make_json_response(data)

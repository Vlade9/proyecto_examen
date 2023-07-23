# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    webservice_url = fields.Char(string="URL del Webservice", config_parameter='account.payment_process_days')

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('vertical_hospital.webservice_url', self.webservice_url)
        return res

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        value = self.env['ir.config_parameter'].sudo().get_param('vertical_hospital.webservice_url')
        res.update(
            webservice_url=value
        )
        return res



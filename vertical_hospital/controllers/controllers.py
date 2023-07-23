# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class HospitalController(http.Controller):

    # @http.route(['/web/payment_invoice/<int:payment_id>/<string:mode>'], type='http', auth="public")
    # def download_payment_invoices(self, payment_id, mode):
    #     stream = io.BytesIO()
    #     zip_archive = zipfile.ZipFile(stream, 'w', compression=zipfile.ZIP_DEFLATED)
    #
    #     payment = request.env['account.payment'].search([('id', '=', payment_id)])
    #
    #     if mode == 'multi_file':
    #         for i in payment.reconciled_invoice_ids.ids:
    #             document = request.env['ir.actions.report'].sudo()._render_qweb_pdf('sit_print_format_new.report_delpalmito_invoice', res_ids=i)
    #             zip_archive.writestr("{0}.pdf".format(i), document[0])
    #             # zip_archive.write(data_file.name, "Reporte.pdf")
    #     if mode == 'single_file':
    #         document = request.env['ir.actions.report'].sudo()._render_qweb_pdf('sit_print_format_new.report_delpalmito_invoice', res_ids=payment.reconciled_invoice_ids.ids)
    #         zip_archive.writestr("{0}.pdf".format("InvoicePack"), document[0])
    #     zip_archive.close()
    #     bytes_of_zipfile = stream.getvalue()
    #
    #     return request.make_response(bytes_of_zipfile,
    #                                  [('Content-Type', 'application/zip'), ('Content-Disposition', 'attachment;filename=InvoicePack.zip;')])
    #

    # # @http.route('/pacientes/consulta/<string:secuencia>', type='json', auth='public', methods=['POST', 'GET'], csrf=False, cors="*")
    # @http.route('/api', auth='public', methods=['GET'], csrf=False)
    # def hello(self, *kw):

        # try:
        #     data = request.env['modelo.paciente'].search_read([('code', '=', secuencia)], ['code', 'name', 'dni', 'state'])
        # except ValueError as exc:
        #     raise werkzeug.exceptions.BadRequest("Resultados invalidos") from exc
        # return request.make_json_response(data)

    def _get_paciente(self, secuencia):
        result = request.env['modelo.paciente'].sudo().search([('code', '=', secuencia)])
        if result:
            return {
                "seq": result.code,
                "name": result.name,
                "dni": result.dni,
                "state": result.state
            }

    @http.route('/pacientes/consulta/<string:secuencia>', type='http', auth="public", method=['GET'])
    def get_paciente(self, secuencia):
        data = self._get_paciente(secuencia)
        return request.make_json_response(data)

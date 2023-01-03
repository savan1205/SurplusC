from odoo import http
from odoo.http import request


class BrandsPage(http.Controller):

    # Controller for Opening all Contact's/partner's after clicking Contacts Menu
    @http.route(route='/brands', type='http', auth='public', website=True)
    def brands_page(self, **kw):
        brands = request.env['product.brand'].search([])
        return request.render('surplus_charges.brand_page', {'brands': brands})

    @http.route('/contact/<model("res.partner"):contact>', type='http', auth="public", website=True)
    def contact_details(self, contact, **kw):
        return request.render('surplus_charges.brand_pages', {'contact': contact})
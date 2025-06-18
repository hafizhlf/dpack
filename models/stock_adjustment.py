from odoo import api, fields, models


class DragonInventoryAdjustment(models.Model):
    _name = "dragon.stock.adjustment"
    _description = "Inventory Adjustment"

    dummy_field_as_button = fields.Char(string="")
    product_id = fields.Many2one('product.product', string='Product')
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    quantity = fields.Float('Quantity')
    stock_location_id = fields.Many2one('stock.location', string='Stock Location')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        for rec in self:
            rec.uom_id = rec.product_id.uom_id.id
            rec.quantity = rec.product_id.qty_available
            quants = self.env['stock.quant'].search([('product_id', '=', rec.product_id.id),("on_hand", "=", True),("location_id.usage", "=", "internal")])
            rec.stock_location_id = False
            for quant in quants:
                rec.stock_location_id = quant.location_id.id

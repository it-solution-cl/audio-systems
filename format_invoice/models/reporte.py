# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
   
    _inherit = 'account.move'
    
    barcode = fields.Char('codigo de barras')
    
    

            
    def total_discount(self):
      
        total = sum(self.invoice_line_ids.mapped('discount'))
  
        amount_total=0
        for line in  self.invoice_line_ids:
            
            subtotal = line.price_subtotal * (line.discount/100)
            amount_total+= subtotal
            
        return amount_total
        
    
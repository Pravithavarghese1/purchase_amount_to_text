# -*- coding: utf-8 -*-


from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_is_zero, float_compare

from odoo.tools import amount_to_text_en, float_round

from odoo.exceptions import UserError, AccessError
from odoo.tools.misc import formatLang
from odoo.addons.base.res.res_partner import WARNING_MESSAGE, WARNING_HELP
import odoo.addons.decimal_precision as dp


#inherit purchase_order module
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    _description = "Purchase Order"



    @api.multi
    def amount_to_text(self, amount, currency):
        
        convert_amount_in_words = amount_to_text_en.amount_to_text(amount, lang='en', currency='')
        convert_amount_in_words = convert_amount_in_words.replace(' and Zero Cent', ' Only ')
        convert_amount_in_words = convert_amount_in_words.replace('Cents', 'Dirhams Only ')
        return convert_amount_in_words

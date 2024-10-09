from odoo.tests.common import TransactionCase, tagged

@tagged('-at_install', 'post_install', 'mon_module')
class TestCommissionMixin(TransactionCase):

    def setUp(self):
        super(TestCommissionMixin, self).setUp()
        self.CommissionMixin = self.env['commission.mixin']

    def test_get_commission(self):
        selling_price = 1000.0
        expected_commission = 50.0  # 5% of 1000
        commission = self.CommissionMixin._get_commission(selling_price)
        self.assertEqual(commission, expected_commission, "Commission calculation is correct")
    
    def test_get_commission_zero_selling_price(self):
        selling_price = 0.0
        expected_commission = 0.0
        commission = self.CommissionMixin._get_commission(selling_price)
        self.assertEqual(commission, expected_commission, "Commission calculation is correct")
    
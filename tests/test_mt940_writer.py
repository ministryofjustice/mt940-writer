from datetime import date
from decimal import Decimal
from unittest import TestCase

import mt940_writer as mt940


class MT940WriterTestCase(TestCase):

    def test_write_statement(self):
        stmt_date = date(2016, 9, 22)
        account = mt940.Account('80008000', '102030')
        opening_balance = mt940.Balance(Decimal('12.99'), stmt_date, 'GBP')
        closing_balance = mt940.Balance(Decimal('15'), stmt_date, 'GBP')
        transactions = [
            mt940.Transaction(stmt_date, Decimal('1'), mt940.TransactionType.transfer, 'Payment 1'),
            mt940.Transaction(stmt_date, Decimal('1'), mt940.TransactionType.miscellaneous, 'Payment 2'),
            mt940.Transaction(stmt_date, Decimal('1'), mt940.TransactionType.transfer, 'Payment 3'),
            mt940.Transaction(stmt_date, Decimal('-0.99'), mt940.TransactionType.miscellaneous, 'Payment 4')
        ]

        expected_output = (
            ':20:59716\n'
            ':25:80008000 102030\n'
            ':28C:1/1\n'
            ':60F:C160922GBP12,99\n'
            ':61:1609220922C1,00NTRFPayment 1\n'
            ':61:1609220922C1,00NMSCPayment 2\n'
            ':61:1609220922C1,00NTRFPayment 3\n'
            ':61:1609220922D0,99NMSCPayment 4\n'
            ':62F:C160922GBP15,00'
        )

        statement = mt940.Statement(
            '59716',
            account,
            '1/1',
            opening_balance,
            closing_balance,
            transactions
        )

        self.assertEqual(str(statement), expected_output)
    def test_write_statement_with_additional_transaction_info(self):
            stmt_date = date(2016, 9, 22)
            account = mt940.Account('80008000', '102030')
            opening_balance = mt940.Balance(Decimal('12.99'), stmt_date, 'GBP')
            closing_balance = mt940.Balance(Decimal('15'), stmt_date, 'GBP')
            transactions = [
                mt940.Transaction(stmt_date, Decimal('1'), mt940.TransactionType.transfer, 'Payment 1',
                                  mt940.TransactionAdditionalInfo('ADDITIONAL/DATA/1')),
                mt940.Transaction(stmt_date, Decimal('1'), mt940.TransactionType.miscellaneous, 'Payment 2',
                                  mt940.TransactionAdditionalInfo('ADDITIONAL/DATA/2')),
                mt940.Transaction(stmt_date, Decimal('1'), mt940.TransactionType.transfer, 'Payment 3'),
                mt940.Transaction(stmt_date, Decimal('-0.99'), mt940.TransactionType.miscellaneous, 'Payment 4')
            ]

            expected_output = (
                ':20:59716\n'
                ':25:80008000 102030\n'
                ':28C:1/1\n'
                ':60F:C160922GBP12,99\n'
                ':61:1609220922C1,00NTRFPayment 1\n'
                ':86:ADDITIONAL/DATA/1\n'
                ':61:1609220922C1,00NMSCPayment 2\n'
                ':86:ADDITIONAL/DATA/2\n'
                ':61:1609220922C1,00NTRFPayment 3\n'
                ':61:1609220922D0,99NMSCPayment 4\n'
                ':62F:C160922GBP15,00'
            )
            statement = mt940.Statement(
                '59716',
                account,
                '1/1',
                opening_balance,
                closing_balance,
                transactions
            )

            self.assertEqual(str(statement), expected_output)

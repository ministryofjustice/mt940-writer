from enum import Enum

VERSION = (0, 5)
__version__ = '.'.join(map(str, VERSION))
__author__ = 'Ministry of Justice Digital & Technology'


class TransactionType(Enum):
    miscellaneous = 'NMSC'
    interest_f = 'FINT'
    transfer = 'NTRF'
    brokerage_fee = 'NBRF'
    miscellaneous_f = 'FMSC'
    charges = 'NCHG'
    bill_of_exchange = 'NBOE'
    cash_letters = 'NCLR'
    cheques = 'NCHK'
    collection = 'NCOL'
    commission = 'NCOM'
    direct_debit = 'NDDT'
    documentary_credit = 'NDCR'
    loan_depost = 'NLDP'
    interest = 'NINT'
    dividends = 'NDIV'
    foreign_exchange = 'NFEX'
    eurocheques = 'NECK'
    equivalent_amount = 'NEQA'
    standing_order = 'NSTO'
    returned_item = 'NRTI'
    value_date_adjustment = 'NVDA'
    travellers_cheques = 'NTCK'


class Account:
    def __init__(self, account_number, sort_code):
        self.account_number = account_number
        self.sort_code = sort_code

    def __str__(self):
        return '{account_number} {sort_code}'.format(
            account_number=self.account_number,
            sort_code=self.sort_code
        )


class Balance:
    def __init__(self, amount, date, currency_code):
        self.amount = amount
        self.date = date
        self.currency_code = currency_code

    def __str__(self):
        return '{category}{date}{currency_code}{amount}'.format(
            category='C' if self.amount >= 0 else 'D',
            date=self.date.strftime('%y%m%d'),
            currency_code=self.currency_code,
            amount='{:0.2f}'.format(self.amount).replace('.', ',').replace('-', '')
        )


class Transaction:
    def __init__(self, date, amount, transaction_type, narrative):
        self.date = date
        self.amount = amount
        self.transaction_type = transaction_type
        self.narrative = narrative

    def __str__(self):
        return '{value_date}{entry_date}{category}{amount}{type_code}{narrative}'.format(
            value_date=self.date.strftime('%y%m%d'),
            entry_date=self.date.strftime('%m%d'),
            category='C' if self.amount >= 0 else 'D',
            amount='{:0.2f}'.format(self.amount).replace('.', ',').replace('-', ''),
            type_code=self.transaction_type.value,
            narrative=self.narrative
        )


class Statement:
    def __init__(self, reference_number, account, statement_number, opening_balance, closing_balance, transactions):
        self.reference_number = reference_number
        self.account = account
        self.statement_number = statement_number
        self.opening_balance = opening_balance
        self.closing_balance = closing_balance
        self.transactions = transactions

    def __iter__(self):
        yield ':20:%s' % self.reference_number
        yield ':25:%s' % self.account
        yield ':28C:%s' % self.statement_number
        yield ':60F:%s' % self.opening_balance
        for transaction in self.transactions:
            yield ':61:%s' % transaction
        yield ':62F:%s' % self.closing_balance

    def __str__(self):
        return '\n'.join(self)

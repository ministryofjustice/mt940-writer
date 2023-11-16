from enum import Enum

VERSION = (0, 7)
__version__ = '.'.join(map(str, VERSION))

__all__ = ['Account', 'Balance', 'Statement', 'Transaction', 'TransactionAdditionalInfo', 'TransactionType']


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
        return f'{self.account_number} {self.sort_code}'


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
            amount=f'{self.amount:0.2f}'.replace('.', ',').replace('-', ''),
        )


class Transaction:
    def __init__(self, date, amount, transaction_type, narrative, additional_info=None):
        self.date = date
        self.amount = amount
        self.transaction_type = transaction_type
        self.narrative = narrative
        self.additional_info = additional_info

    def __str__(self):
        return '{value_date}{entry_date}{category}{amount}{type_code}{narrative}'.format(
            value_date=self.date.strftime('%y%m%d'),
            entry_date=self.date.strftime('%m%d'),
            category='C' if self.amount >= 0 else 'D',
            amount=f'{self.amount:0.2f}'.replace('.', ',').replace('-', ''),
            type_code=self.transaction_type.value,
            narrative=self.narrative,
        )


class TransactionAdditionalInfo:
    def __init__(self, information):
        self.information = information

    def __str__(self):
        return f'{self.information}'

    def __bool__(self):
        return bool(self.information)


class Statement:
    def __init__(self, reference_number, account, statement_number, opening_balance, closing_balance, transactions):
        self.reference_number = reference_number
        self.account = account
        self.statement_number = statement_number
        self.opening_balance = opening_balance
        self.closing_balance = closing_balance
        self.transactions = transactions

    def __iter__(self):
        yield f':20:{self.reference_number}'
        yield f':25:{self.account}'
        yield f':28C:{self.statement_number}'
        yield f':60F:{self.opening_balance}'
        for transaction in self.transactions:
            yield f':61:{transaction}'
            if transaction.additional_info:
                yield f':86:{transaction.additional_info}'
        yield f':62F:{self.closing_balance}'

    def __str__(self):
        return '\n'.join(self)

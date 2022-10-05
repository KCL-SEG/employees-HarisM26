"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.salaryType = SalaryType(self.name)
        self.salaryTypeStr = self.salaryType.getSalaryTypeStr()
        self.contractPay = ContractPay(self.name, self.salaryType.isSalaryMonthly())
        self.totalContractStr = self.contractPay.getContractStr()
        self.totalContractPay = self.contractPay.getTotalContractPay()
        self.commissionType = CommissionType(self.name)
        self.commissionTypeStr = self.commissionType.getCommissionTypeStr()
        self.commissionPay = CommissionPay(self.name, self.commissionType.receivesCommission(), self.commissionType.isCommissionFixed())
        self.totalCommissionStr = self.commissionPay.getTotalCommissionStr()
        self.totalCommissionPay = self.commissionPay.getTotalCommissionPay()
        self.totalPay = self.totalContractPay + self.totalCommissionPay

    def get_pay(self):
        return self.totalPay

    def __str__(self):
        return f"{self.name} {self.salaryTypeStr} {self.totalContractStr}{self.commissionTypeStr}{self.totalCommissionStr}. Their total pay is {self.totalPay}."


class ContractPay:
    def __init__(self, name, isSalaryMonthly):
        self.name = name
        self.isSalaryMonthly = isSalaryMonthly
        self.setTotalContractPay()

    def setTotalContractPay(self):
        if self.name == "Billie":
            self.monthlySal = 4000
        elif self.name == "Charlie":
            self.hourlySal = 25
            self.hours = 100
        elif self.name == "Renee":
            self.monthlySal = 3000
        elif self.name == "Jan":
            self.hourlySal = 25
            self.hours = 150
        elif self.name == "Robbie":
            self.monthlySal = 2000
        elif self.name == "Ariel":
            self.hourlySal = 30
            self.hours = 120

    def getTotalContractPay(self):
        if self.isSalaryMonthly:
            return self.monthlySal
        else:
            return self.hourlySal * self.hours

    def getContractStr(self):
        if self.isSalaryMonthly:
            return str(self.monthlySal)
        else:
            return f"{self.hours} hours at {self.hourlySal}/hour"


class CommissionPay:
    def __init__(self, name, receivesCommission, isCommissionFixed=""):
        self.name = name
        self.commissionPay = ""
        self.numCommissionContracts = ""
        self.perContract = ""
        self.bonusCommission = ""
        self.receivesCommission = receivesCommission
        self.isCommissionFixed = isCommissionFixed
        self.setTotalCommissionPay()
        self.calculateCommissionPay()

    def setTotalCommissionPay(self):
        if self.name == "Billie":
            self.commissionPay = 0
        elif self.name == "Charlie":
            self.commissionPay = 0
        elif self.name == "Renee":
            self.numCommissionContracts = 4
            self.perContract = 200
        elif self.name == "Jan":
            self.numCommissionContracts = 3
            self.perContract = 220
        elif self.name == "Robbie":
            self.bonusCommission = 1500
        elif self.name == "Ariel":
            self.bonusCommission = 600

    def calculateCommissionPay(self):
        if self.receivesCommission:
            if self.isCommissionFixed:
                self.commissionPay = self.bonusCommission
            else:
                self.commissionPay = self.numCommissionContracts * self.perContract

    def getTotalCommissionPay(self):
        return self.commissionPay

    def getTotalCommissionStr(self):
        if self.receivesCommission:
            if self.isCommissionFixed:
                return f" {self.bonusCommission}"
            else:
                return f" {self.numCommissionContracts} contract(s) at {self.perContract}/contract"
        else:
            return ""


class SalaryType:
    Name_IsSalaryMonthly = {'Billie':True, 'Charlie':False, 'Renee':True, 'Jan':False, 'Robbie':True, 'Ariel':False}

    def __init__(self, name):
        self.name = name

    def getSalaryTypeStr(self):
        if self.isSalaryMonthly() == True:
            return "works on a monthly salary of"
        else:
            return "works on a contract of"

    def isSalaryMonthly(self):
        return self.Name_IsSalaryMonthly[self.name]


class CommissionType:
    Name_ReceivesCommission = {'Billie':False, 'Charlie':False, 'Renee':True, 'Jan':True, 'Robbie':True, 'Ariel':True}
    Name_IsCommissionFixed = {'Renee':False, 'Jan':False, 'Robbie':True, 'Ariel':True}

    def __init__(self, name):
        self.name = name

    def getCommissionTypeStr(self):
        if self.receivesCommission():
            if self.isCommissionFixed():
                return " and receives a bonus commission of"
            else:
                return " and receives a commission for"
        else:
            return ""

    def isCommissionFixed(self):
        if self.name in self.Name_IsCommissionFixed:
            return self.Name_IsCommissionFixed[self.name]
        else:
            return ""

    def receivesCommission(self):
        return self.Name_ReceivesCommission[self.name]



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')

class HRManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        if employee_id not in self.employees:
            self.employees[employee_id] = {
                'name': name,
                'position': position,
                'department': department,
                'salary': salary
            }
            return True
        else:
            return False

    def remove_employee(self, employee_id):
        if employee_id not in self.employees:
            return False
        else:
            del self.employees[employee_id]
            return True

    def update_employee(self, employee_id: int, employee_info: dict):
        employee = self.get_employee(employee_id)
        if not employee == False:
            for key, value in employee_info.items():
                if key not in employee:
                    return False
            for key, value in employee_info.items():
                employee[key] = value
            return True
        else:
            return False

    def get_employee(self, employee_id):
        if employee_id not in self.employees:
            return False
        else:
            return self.employees[employee_id]

    def list_employees(self):
        employee_data = {}
        if self.employees:
            for employee_id, employee_info in self.employees.items():
                employee_details={}
                employee_details["employee_ID"]=employee_id
                for key, value in employee_info.items():
                    employee_details[key]=value
                employee_data[employee_id]=employee_details
        return  employee_data

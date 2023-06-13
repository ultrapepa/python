from employee import Employee

employee_1 = Employee(
    name="Kevin Bacon",
    title="Executive Producer",
    email_address="kbacon@example.com",
    phone_number="555-867-5309"
)

employee_2 = Employee("Bruce Wayne", "bwayne@example.com", "CEO")

employee_1.email_signature(include_phone=True)
while True:
    user_action = input('Type "start" to calcualte or "exit": ')
    user_action = user_action.strip()

    match user_action:
        case "start":
            invoice_amount = int(input("Type invoice amount: €"))
            vat = int(input("Type VAT amount: %"))

            vat_calculation = invoice_amount + ((invoice_amount * vat)/100)

            print(f"Amount: {invoice_amount}€ VAT: {vat}% Total: {vat_calculation}€")

        case "exit":
            break

        case _:
            print("Unknown command was typed")

print("Bye!")
def logicalc(app, operation):
    if operation == "C":
        app.formula = ''
    elif operation == 'DEL':
        app.formula = app.formula[0:-1]
    elif operation == '=':
        app.formula = str(eval(app.formula))
    elif operation == 'X^2':
        app.formula = str((eval(app.formula)) ** 2)
    elif operation == '%':
        app.formula = str((eval(app.formula)) / 100)
    else:
        if app.formula == '0':
            app.formula = ''
        app.formula += operation

    update(app)


def update(app):
    if app.formula == '':
        app.formula = '0'
    app.lbl.configure(text=app.formula)

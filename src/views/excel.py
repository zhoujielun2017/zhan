import flask_excel as excel

excel.init_excel(app)
@app.route('/export')
def export():
    return excel.make_response_from_array([[1, 2], [3, 4]], "csv",
                                          file_name="export_data")
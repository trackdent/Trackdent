# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
#from datetime import datetime

import teethchart_functions
from gluon.fileutils import read_file

def index():
    if len(db().select(db.patients.ALL))<1:
        db.patients.insert(lastname=T('Patient'), firstname=T('Default'), notes=T('Default patient'))
    if not session.current_id:
            session.current_id = db(db.patients.id>0).select(orderby=~db.patients.id).first().id
    if request.vars.lastname:
        search_str=request.vars.lastname.capitalize()
        pattern = request.vars.lastname.capitalize() + '%'
        query = db.patients.lastname.like(pattern)
        table_title = T("Patients List")
    elif request.vars.contacts:
        query = db.patients.contact == True
        search_str=""
        table_title = T("Contacts List")
    else:
        query = db.patients.lastname
        search_str=""
        table_title = T("Patients List")
    rows = db(query).select(db.patients.ALL, orderby=~db.patients.id)
    if not rows:
        table1 = TABLE(THEAD(TR(TH(T('Lastname')), TH(T('Firstname')), TH(T('Address')), TH(T('City')), TH(T('Date of Birth')), TH(T('Last Visit')), TH(T('Tel Home')), TH(T('Tel Work')), TH(T('Tel Mobile')), TH(T('Profession')))), TBODY(), _id='table_patients', _class='pretty2')
    else:    
        extracolumns1 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='patient_id_' + str(row.id)))}]
        table1 = SQLTABLE(rows, _id="table_patients", _class='pretty2', headers='labels', columns=["patients.lastname", "patients.firstname", "patients.address", "patients.city", "patients.birthday", "patients.datelastvisit", "patients.telhome", "patients.telwork", "patients.telmobile", "patients.profession" ], extracolumns=extracolumns1)
    if request.args(0):
        patient_name = '%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    else:
        patient_id = db(db.patients.id>0).select(orderby=~db.patients.id).first().id
        redirect(URL('index', args=patient_id))
    return dict(table1=table1, patient_name=patient_name, table_title=table_title)

def labs():
    search_str=""
    table_title = T("Labs List")
    rows = db().select(db.dental_labs.ALL, orderby=~db.dental_labs.lastname)
    if not rows:
        table1 = TABLE(THEAD(TR(TH(T('Lastname')), TH(T('Firstname')), TH(T('Address')), TH(T('City')), TH(T('Tel Home')), TH(T('Tel Work')), TH(T('Tel Mobile')))), TBODY(), _id='table_labs', _class='pretty2')
    else:    
        extracolumns1 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='patient_id_' + str(row.id)))}]
        table1 = SQLTABLE(rows, _id="table_labs", _class='pretty2', headers='labels', columns=["dental_labs.lastname", "dental_labs.firstname", "dental_labs.address", "dental_labs.city", "dental_labs.tel1", "dental_labs.tel2", "dental_labs.telmobile" ], extracolumns=extracolumns1)
    if request.args(0):
        patient_name = '%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    else:
        lab_id = db(db.dental_labs.id>0).select(orderby=~db.dental_labs.id).first().id
        redirect(URL('index', args=lab_id))
    return dict(table1=table1, patient_name=patient_name, table_title=table_title)

def lab_update():
    patient_name = '%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    return dict(patient_name=patient_name)

def lab_update_details():
    if request.args(2)=='new':
        record = None
    else:
        record = db.dental_labs(request.args(1)) # returns an object of type row (section 6.17.2 web2py book: "Fetching a row")
    form=SQLFORM( db.dental_labs, record , hidden = dict(active_tab = '', del_b = '')) 
    form.element('textarea[name=notes]')['_style']='width:150px;height:100px'
    form.element('input[name=lastname]')['_style']='width:150px'
    form.element('input[name=firstname]')['_style']='width:150px'
    form.element('input[name=address]')['_style']='width:150px'
    form.element('input[name=city]')['_style']='width:150px'
    form.element('input[name=zipcode]')['_style']='width:150px'
    form.element('input[name=tel1]')['_style']='width:150px'
    form.element('input[name=tel2]')['_style']='width:150px'
    form.element('input[name=telmobile]')['_style']='width:150px'
    form.element('input[name=email]')['_style']='width:150px'
    if form.process().accepted:
        response.flash = False
        if request.vars.del_b:
            form.deleted = True
            record.delete_record()
            redirect(URL('labs', args = [request.args(0)], extension=False), client_side=True)
        if request.args(1) == 'new':
            redirect(URL('lab_update', args = [request.args(0), form.vars.id], extension=False), client_side=True)
        redirect(URL('lab_update_details', args = [request.args(0), form.vars.id]))
    elif form.errors:
        response.flash = T('there are errors!')
    return dict(form=form)

def patient_update():
    if request.args(1) == 'new':
        patient_name = T('New Patient')
    else:
        patient_name = '%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    return dict(patient_name=patient_name)

def patient_update_details():
    if not request.args(0) or request.args(1)=='new':
        record = None
    else:
        record = db.patients(request.args(0)) # returns an object of type row (section 6.17.2 web2py book: "Fetching a row")
    form=SQLFORM( db.patients, record , hidden = dict(active_tab = '', del_b = '')) 
    form.element('select[name=sex]')['_style']='width:80px'
    form.element('input[name=birthday]')['_style']='width:150px'
    form.element('input[name=datefirstvisit]')['_style']='width:80px'
    form.element('input[name=datelastvisit]')['_style']='width:80px'
    form.element('input[name=daterecall]')['_style']='width:80px'
    form.element('input[name=balance]')['_style']='width:50px'
    form.element('textarea[name=notes]')['_style']='width:460px;height:100px'
    form.element('input[name=lastname]')['_style']='width:150px'
    form.element('input[name=firstname]')['_style']='width:150px'
    form.element('input[name=fathername]')['_style']='width:150px'
    form.element('input[name=profession]')['_style']='width:150px'
    form.element('input[name=insurance]')['_style']='width:150px'
    form.element('input[name=referredby]')['_style']='width:150px'
    form.element('input[name=referredby_tel]')['_style']='width:150px'
    patient_age=T("Unknown")
    if record:
        session.current_id = record.id
        if record.birthday:
            #form.custom.patient_age=int(round((datetime.date.today() - record.birthday).days/365.25))
            patient_age=int(round((datetime.date.today() - record.birthday).days/365.25))
    if form.process().accepted:
        response.flash = False
        if request.vars.del_b:
            form.deleted = True
            record.delete_record()
            redirect(URL('index', extension=False), client_side=True)
        if form.vars.birthday:
            form.custom.patient_age=int(round((datetime.date.today() - form.vars.birthday).days/365.25))
        else:
            form.custom.patient_age=T("Unknown")
        tab=request.vars.active_tab
        if request.args(1) == 'new':
            redirect(URL('patient_update', args = [form.vars.id], extension=False), client_side=True)
        redirect(URL('patient_update_details', args = [request.args(0)], vars=dict(tab=tab)))
    elif form.errors:
        response.flash = T('there are errors!')
    form_med = SQLFORM(db.medical_conditions, hidden = dict(action = '', med_id=''), _id='form_med')
    if form_med.validate():
        if request.vars.action=='upd':
            db(db.medical_conditions.id == request.vars.med_id).update(name=request.vars.name)
        if request.vars.action=='new':
            db.medical_conditions.insert(name=request.vars.name)
        redirect(URL('patient_update_details', args = request.args(0), vars=dict(tab='li_tab2')))
    return dict(form=form, form_med=form_med, patient_age=patient_age)

def medical_delete():
    remove = db(db.medical_conditions.id==request.args(0)).delete()
    
def medical_update():
    db(db.medical_conditions.id==request.args(1)).validate_and_update(name=request.vars.name)

#Δύο τρόποι για delete: 
#a)Με <a> και link για controller/view, delete manually (view δεν χρειάζεται, γίνεται redirect)
#    remove = db(db.medical_conditions.id==request.args(0)).delete()
#    if remove:
#        redirect(URL('patient_update', args=session.current_id))
#b)Με  BUTTON(T('DELETE'), _class='btn btn-large delete', _onclick='return confirm("' + T("Are you sure?") + '")', _type="submit", _name="delete", #   _value="delete")
#To BUTTON πρέπει να είναι μέσα στην φόρμα.
#Και:
#    if form.process().accepted:
#        response.flash = False
#        if request.vars.delete:
#            form.deleted = True
#            record.delete_record()
#            redirect(URL('patient_update', args=session.current_id))
#
#Ο δεύτερος τρόπος απαιτεί φόρμα.
#Ο πρώτος απαιτεί ξεχωριστή controller function για delete.

def endo():
    query1 = (db.endo.patient == request.args(0))
    rows1 = db(query1).select(db.endo.ALL, orderby=~db.endo.date)
    if not rows1:
        table1 = TABLE(THEAD(TR( TH(T('TOOTH')))), TBODY(), _id='endo', _class='master pretty2 table-condensed')
    else:    
        extracolumns1 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='endo_id_' + str(row.id)))}]
        table1 = SQLTABLE(rows1, _id="endo", _class='master pretty2 table-condensed',  headers='labels', columns=["endo.tooth" ], 
extracolumns=extracolumns1) 
    patient_name='%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    return dict(table1=table1, patient_name=patient_name )

def endo_details():
    db.endo.patient.default = request.args(0)
    if not request.args(1) or request.args(1)=='new':
        record = None
    else:
        record = db.endo(request.args(1))
    form=SQLFORM( db.endo, record, hidden = dict(del_b = '', reload_page = ''))
    if not request.args(1):
        form.element('input[name=date]')['_value']=''   
    form.element('input[name=date]')['_style']='width:80px'
    form.element('select[name=tooth]')['_style']='width:70px'
    form.element('textarea[name=notes]')['_style']='width:250px; height:60px'
    form.element('select[name=eplength]')['_style']='width:60px'
    form.element('select[name=epdieyr]')['_style']='width:60px'
    form.element('select[name=eptaper]')['_style']='width:60px'
    form.element('select[name=eglength]')['_style']='width:60px'
    form.element('select[name=egdieyr]')['_style']='width:60px'
    form.element('select[name=egtaper]')['_style']='width:60px'
    form.element('select[name=aplength]')['_style']='width:60px'
    form.element('select[name=apdieyr]')['_style']='width:60px'
    form.element('select[name=aptaper]')['_style']='width:60px'
    form.element('select[name=aglength]')['_style']='width:60px'
    form.element('select[name=agdieyr]')['_style']='width:60px'
    form.element('select[name=agtaper]')['_style']='width:60px'
    form.element('select[name=ylength]')['_style']='width:60px'
    form.element('select[name=ydieyr]')['_style']='width:60px'
    form.element('select[name=ytaper]')['_style']='width:60px' 
    if form.process().accepted:
        response.flash = False
        if request.vars.del_b:
            form.deleted = True
            record.delete_record()
            redirect(URL("endo", args=[request.args(0)], extension=False), client_side=True)
        if request.vars.reload_page:
            redirect(URL('endo', args = [request.args(0), form.vars.id], extension=False ), client_side=True)
    elif form.errors:
        response.flash = T('there are errors!') 
    return dict(form=form)
    
def color():
    query1 = (db.colors.patient == request.args(0))
    rows1 = db(query1).select(db.colors.ALL, orderby=~db.colors.date)
    if not rows1:
        table1 = TABLE(THEAD(TR( TH(T('DATE')), TH(T('TOOTH')), TH('NECK'), TH('INCISAL'), TH('MESIAL'), TH('DISTAL') )), TBODY(), _id='colors', _class='master pretty2 table-condensed')
    else:    
        extracolumns1 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='color_id_' + str(row.id)))}]
        table1 = SQLTABLE(rows1, _id="colors", _class='master pretty2 table-condensed',  headers='labels', columns=["colors.date", "colors.tooth", "colors.n_color", "colors.i_color", "colors.m_color", "colors.d_color"], extracolumns=extracolumns1) 
    patient_name='%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    return dict(table1=table1, patient_name=patient_name )

def color_details():
    db.colors.patient.default = request.args(0)
    if not request.args(1) or request.args(1)=='new':
        record = None
    else:
        record = db.colors(request.args(1))
    form=SQLFORM( db.colors, record, hidden = dict(del_b = '', reload_page = '') )
    if not request.args(1):
        form.element('input[name=date]')['_value']=''   
    form.element('select[name=tooth]')['_style']='width:50px'
    form.element('input[name=date]')['_style']='width:80px'
    form.element('input[name=n_color]')['_style']='width:80px'
    form.element('input[name=i_color]')['_style']='width:80px'
    form.element('input[name=m_color]')['_style']='width:80px'
    form.element('input[name=d_color]')['_style']='width:80px'
    if form.process().accepted:
        response.flash = False
        if request.vars.del_b:
            form.deleted = True
            record.delete_record()
            redirect(URL("color", args=[request.args(0)], extension=False), client_side=True)
        if request.vars.reload_page:
            redirect(URL('color', args = [request.args(0), form.vars.id], extension=False ), client_side=True)
    elif form.errors:
        response.flash = T('there are errors!')
    return dict(form=form)

def payments():
    query1 = (db.payments.patient == request.args(0))
    rows1 = db(query1).select(db.payments.ALL, orderby=~db.payments.date)
    if not rows1:
        table1 = TABLE(THEAD(TR( TH(T('Date')), TH(T('Amount')), TH('Receipt No'), TH('Receipt Amount') )), TBODY(), _id='payments', _class='master pretty2 table-condensed')
    else:    
        extracolumns1 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='pay_id_' + str(row.id)))}]
        table1 = SQLTABLE(rows1, _id="payments", _class='master pretty2 table-condensed',  headers='labels', columns=["payments.date", "payments.amount", "payments.receipt_no", "payments.receipt_amount" ], extracolumns=extracolumns1)         
    patient_name = '%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    patient_job = db.patients[request.args(0)].profession
    patient_address = '%(address)s %(city)s' %dict(address = db.patients[request.args(0)].address, city = db.patients[request.args(0)].city)
    return dict(table1=table1, patient_name=patient_name, patient_job=patient_job, patient_address=patient_address)

def payments_details():
    db.payments.patient.default = request.args(0)
    if not request.args(1) or request.args(1)=='new':
        record = None
    else:
        record = db.payments(request.args(1))
    form=SQLFORM( db.payments, record, hidden = dict(del_b = '', reload_page = '') )
    if not request.args(1):
        form.element('input[name=date]')['_value']=''   
    form.element('input[name=date]')['_style']='width:80px'
    form.element('input[name=amount]')['_style']='width:80px'
    form.element('input[name=receipt_no]')['_style']='width:80px'
    form.element('input[name=receipt_amount]')['_style']='width:80px'
    if form.process().accepted:
        response.flash = False
        if request.vars.del_b:
            form.deleted = True
            record.delete_record()
            redirect(URL("payments", args=[session.current_id], extension=False), client_side=True)
        if request.vars.reload_page:
            redirect(URL('payments', args = [session.current_id, form.vars.id], extension=False ), client_side=True)
    elif form.errors:
        response.flash = T('there are errors!')
    return dict(form=form)

def images():
    db.images.patient.default = request.args(0)
    image = None
    if type(request.vars.img_files) == list:
        for i in request.vars.img_files:
            image = db.images.img_file.store(i.file, i.filename)
            img_id = db.images.insert(date = db.images.date.default, img_file=image)
    else:
        try:
            image = db.images.img_file.store(request.vars.img_files.file, request.vars.img_files.filename)
            img_id = db.images.insert(date = db.images.date.default, img_file=image)
        except:
            pass
    query1 = (db.images.patient == request.args(0))
    rows1 = db(query1).select(db.images.ALL, orderby=~db.images.date)
    if not rows1:
        table1 = TABLE(THEAD(TR( TH(T('DATE')), TH(T('FILE')), TH(T('PREVIEW')) )), TBODY(), _id='images', _class='master pretty2 table-condensed')
    else:    
        extracolumns1 = [{'label':T('PREVIEW') , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(IMG(_src=URL('download', args=row.img_file), _height="60px"))}, {'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='image_id_' + str(row.id)))} ]
        table1 = SQLTABLE(rows1, _id="images", _class='master pretty2 table-condensed',  headers='labels', columns=["images.date", "images.notes", "images.img_file" ], extracolumns=extracolumns1, upload=URL('download'))        
    patient_name = '%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    return dict(table1=table1, patient_name=patient_name)
    
def images_details():
    img=None
    db.images.patient.default = request.args(0)
    if not request.args(1) or request.args(1)=='new':
        record = None
    else:
        record = db.images(request.args(1))
        img=IMG(_src=URL('download', args=record.img_file), _height="280px")
    form=SQLFORM( db.images, record, hidden = dict(del_b = '') )
    if not request.args(1):
        form.element('input[name=date]')['_value']=''
    form.element('input[name=date]')['_style']='width:80px;'
    form.element('textarea[name=notes]')['_style']='height:40px;'
    if form.process().accepted:
        response.flash = False
        if request.vars.del_b:
            form.deleted = True
            record.delete_record()
            redirect(URL("images", args=[session.current_id], extension=False), client_side=True)
        redirect(URL('images', args = [session.current_id, form.vars.id], extension=False ), client_side=True)
    elif form.errors:
            response.flash = T('there are errors!')
    return dict(form=form, img=img)

def diagram():
    patient_name = '%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname) 
    return dict( patient_name = patient_name )

def select_dental_work():
    insert_forms = {}
    categ_names = {}
    for categ in db().select(db.dental_work_categories.ALL):
        d_works_insert_fields=[]
        query = (db.dental_works.category == categ.id)
        d_works_insert_fields.append(Field('d_works_field', db.dental_works, requires=IS_IN_DB(db(query), 'dental_works.id', '%(name)s', zero=None)))
        d_works_insert_fields.append(db.dental_record.dental_work_date)
        d_works_insert_fields.append(db.dental_record.material)
        d_works_insert_fields.append(db.dental_record.dental_lab)
        d_works_insert_fields.append(db.dental_record.charge)
        form = SQLFORM.factory(*d_works_insert_fields)
        form.element('select[name=d_works_field]')['_style']='width:100%;'
        form.element('select[name=d_works_field]')['_size']='15'
        form.element('input[name=dental_work_date]')['_style']='width:50%;'
        form.element('input[name=charge]')['_style']='width:30%;'
        form.element('select[name=material]')['_style']='width:90%;'
        form.element('select[name=dental_lab]')['_style']='width:90%;'
        insert_forms[categ.id] = form
        categ_names[categ.id] = categ.name
        form_name = 'form_' + str(categ.id)
        if form.process(formname = form_name).accepted:
            #response.flash = 'form accepted'    
            session.dental_work = form.vars.d_works_field
            session.dental_work_date = form.vars.dental_work_date
            session.charge = form.vars.charge
            session.material = form.vars.material
            session.dental_lab = form.vars.dental_lab
            response.flash = False
        elif form.errors:
            response.flash = 'form has errors'
    prices = {}
    for row in db().select(db.dental_works.id, db.dental_works.price):
        prices[row.id] = row.price
    return dict( insert_forms = insert_forms, categ_names = categ_names, prices = prices )

def diagram_insert(): 
    form = FORM(hidden = dict(x_value = '', y_value = '', ins_action = '', perm = 'True'), _id = 'x_y_vals') 
    if form.process().accepted:
        x_value = request.vars.x_value
        y_value = request.vars.y_value
        if request.vars.perm == 'False':
            perm = False
        else:
            perm = True
        ins_action = request.vars.ins_action[3:]
        ddental_work = session.dental_work
        separation = db.dental_works(ddental_work).separation
        try:
            dtooth = teethchart_functions.get_tooth_from_coordinates(db, x_value, y_value, separation, perm)
        except:
            redirect(URL('diagram_insert', args=[request.args(0)], vars = dict(tab=request.vars.ins_action, perm=request.vars.perm)))  
        dpatient = request.args(0)
        #dpatient = session.current_id
        ddental_work_date = session.dental_work_date
        dcharge = session.charge
        ddental_lab = session.dental_lab
        dmaterial = session.material
        if ins_action == "0":
            db.dental_record.insert(patient = dpatient,  dental_work = ddental_work, dental_work_date = ddental_work_date, charge = dcharge, tooth = dtooth, dental_lab = ddental_lab, material = dmaterial, done = True)
        elif ins_action == "1":
            db.dental_record.insert(patient = dpatient,  dental_work = ddental_work, dental_work_date = ddental_work_date, charge = dcharge, tooth = dtooth, dental_lab = ddental_lab, material = dmaterial, done = False)
        elif ins_action == "2":
            db.pre_existing_dental_works.insert(patient = dpatient,  dental_work = ddental_work, tooth = dtooth, material = dmaterial)
        redirect(URL('diagram_insert', args=[request.args(0)], vars = dict(tab=request.vars.ins_action, perm=request.vars.perm)))
    dental_works1 = teethchart_functions.get_dental_works(db, request.args(0), 1, True)       
    dental_works2 = teethchart_functions.get_dental_works(db, request.args(0), 2, True)              
    dental_works3 = teethchart_functions.get_dental_works(db, request.args(0), 3, True)
    dental_works1j = teethchart_functions.get_dental_works(db, request.args(0), 1, False)         
    dental_works2j = teethchart_functions.get_dental_works(db, request.args(0), 2, False)             
    dental_works3j = teethchart_functions.get_dental_works(db, request.args(0), 3, False)             
    return dict(form = form, dental_works1 = dental_works1, dental_works2 = dental_works2, dental_works3 = dental_works3, dental_works1j = dental_works1j, dental_works2j = dental_works2j, dental_works3j = dental_works3j)
    
def dental_record(): 
    patient_name = '%(lastname)s %(firstname)s' % dict(lastname=db.patients[request.args(0)].lastname, firstname=db.patients[request.args(0)].firstname)
    query1 = (db.dental_record.patient == request.args(0)) & (db.dental_record.done == True)
    rows1 = db(query1).select(db.dental_record.ALL, orderby=~db.dental_record.dental_work_date)
    if not rows1:
        table1 = TABLE(THEAD(TR(TH(T('DATE')), TH(T('TOOTH')), TH(T('DENTAL WORK')), TH(T('CHARGE')), TH(T('LAB')), TH(T('MATERIAL')), TH(T('')))), TBODY(), _id='d_rec', _class='master pretty1')
    else:    
        extracolumns1 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='work_id_'+str(row.id)))}]
        table1 = SQLTABLE(rows1, _id="d_rec", _class='master pretty1', headers='labels', columns=["dental_record.dental_work_date", "dental_record.tooth", "dental_record.dental_work", "dental_record.charge", "dental_record.dental_lab", "dental_record.material" ], 
extracolumns=extracolumns1)
    query2 = (db.dental_record.patient == request.args(0)) & (db.dental_record.done == False)
    rows2 = db(query2).select(db.dental_record.ALL, orderby=~db.dental_record.dental_work_date)
    if not rows2:
        table2 = TABLE(THEAD(TR(TH(T('DATE')), TH(T('TOOTH')), TH(T('DENTAL WORK')), TH(T('CHARGE')), TH(T('LAB')), TH(T('MATERIAL')), TH(T('')))), TBODY(), _id='cdw', _class='master pretty1')
    else:    
        extracolumns2 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='work_id_'+str(row.id)))}]
        table2 = SQLTABLE(rows2, _id="cdw", _class='master pretty1', headers='labels', columns=["dental_record.dental_work_date", "dental_record.tooth", "dental_record.dental_work", "dental_record.charge", "dental_record.dental_lab", "dental_record.material" ], 
extracolumns=extracolumns2) 
    rows3 = db(db.therapy_plan.patient == request.args(0)).select(db.therapy_plan.ALL)
    if not rows3:
        table3 = TABLE(THEAD(TR(TH(T('DATE')), TH(T('PLAN')), TH(T('')))), TBODY(), _id='t_p', _class='master pretty1')
    else:
        extracolumns3 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='ther_plan_id_'+str(row.id)))}]
        table3 = SQLTABLE(rows3, _id="t_p", _class='master pretty1', headers='labels', columns=[ "therapy_plan.tp_name",  "therapy_plan.tp_date"], extracolumns=extracolumns3)  
    rows5 = db(db.pre_existing_dental_works.patient == request.args(0)).select(db.pre_existing_dental_works.ALL)
    if not rows5:
        table5 = TABLE(THEAD(TR( TH(T('TOOTH')), TH(T('DENTAL WORK')), TH(T('MATERIAL')), TH(T('')))), TBODY(), _id='pre_ex', _class='pretty1')
    else: 
        extracolumns5 = [{'label':'', 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: INPUT(_type='checkbox', _style="visibility: hidden;", _name='pre_ex_work_id_'+str(row.id))}]
        table5 = SQLTABLE(rows5, _id="pre_ex", _class='master pretty1', headers='labels', columns=[ "pre_existing_dental_works.tooth",  
"pre_existing_dental_works.dental_work", "pre_existing_dental_works.material" ], extracolumns=extracolumns5)   
    form_details_pre_ex = SQLFORM.factory(db.pre_existing_dental_works.id, db.pre_existing_dental_works.dental_work, db.pre_existing_dental_works.material, db.pre_existing_dental_works.tooth, table_name='pre_ex_table', _id='form_details_pre_ex')
    form_details_pre_ex.element('select[name=tooth]')['_style']='width:60px'
    form_details_pre_ex.element('select[name=dental_work]')['_style']='width:250px'
    form_details_pre_ex.element('select[name=material]')['_style']='width:250px'
    if form_details_pre_ex.validate(form_name='pre_ex'):
        if request.vars.action == 'del_work':
            for i in request.vars:
                if i[:15] == 'pre_ex_work_id_': 
                    db(db.pre_existing_dental_works.id == i[15:]).delete()      
        if request.vars.action == 'save_work':
            i = request.vars.cur_rec_id
            db(db.pre_existing_dental_works.id == i).validate_and_update(tooth = request.vars.tooth, material = request.vars.material, dental_work = request.vars.dental_work)
        redirect(URL('dental_record', args=[request.args(0)], vars = dict(tab='li_tab2')))
    form_details_dr = SQLFORM.factory(db.dental_record.id, db.dental_record.dental_work_date,  db.dental_record.tooth, db.dental_record.dental_work, db.dental_record.charge, db.dental_record.dental_lab, db.dental_record.material, table_name='dr_table', _id='form_details_dr')
    form_details_dr.element('input[name=dental_work_date]')['_style']='width:100px'
    form_details_dr.element('select[name=tooth]')['_style']='width:60px'
    form_details_dr.element('select[name=dental_work]')['_style']='width:250px'
    form_details_dr.element('input[name=charge]')['_style']='width:100px'
    form_details_dr.element('select[name=dental_lab]')['_style']='width:250px'
    form_details_dr.element('select[name=material]')['_style']='width:250px'
    if form_details_dr.validate(form_name='dr'):
        if request.vars.action == 'del_work':
            for i in request.vars:
                if i[:8] == 'work_id_': 
                    db(db.dental_record.id == i[8:]).delete()
        if request.vars.action == 'save_work':
            i = request.vars.cur_rec_id
            db(db.dental_record.id == i).validate_and_update(dental_work_date = request.vars.dental_work_date, tooth = request.vars.tooth, dental_work = request.vars.dental_work, dental_lab = request.vars.dental_lab, material = request.vars.material)
        if request.vars.action == 'transf_work':
            for i in request.vars:
                if i[:8] == 'work_id_':
                    db(db.dental_record.id == i[8:]).update(done = not db.dental_record(i[8:]).done)
        redirect(URL('dental_record', args=[request.args(0)], vars = dict(tab='li_tab0')))
    form_t_p = SQLFORM.factory(db.therapy_plan.id, db.therapy_plan.tp_date,  db.therapy_plan.tp_name, table_name='t_p_table', _id='form_t_p')
    form_t_p.element('input[name=tp_date]')['_style']='width:100px'
    form_t_p.element('input[name=tp_name]')['_style']='width:150px'
    if form_t_p.validate(form_name='tp'):
        if request.vars.action == 'del_work':
            for i in request.vars:
                if i[:13] == 'ther_plan_id_': 
                    db(db.therapy_plan.id == int(i[13:])).delete()
        if request.vars.action == 'save_work':
            i = request.vars.cur_rec_id
            db(db.therapy_plan.id == i).validate_and_update(tp_date = request.vars.tp_date, tp_name = request.vars.tp_name)
        redirect(URL('dental_record', args=[request.args(0)], vars = dict(tab='li_tab3')))
    db.therapy_plan.patient.default = request.args(0)
    form_add_tp = SQLFORM(db.therapy_plan)
    #form_add_tp.vars.patient = request.args(0)
    if form_add_tp.process(form_name='tp_add').accepted:
        response.flash = 'form accepted'
        redirect(URL('dental_record', args=[request.args(0)], vars = dict(tab='li_tab3')))
    form_details_ctp = SQLFORM.factory(db.dental_record.id, db.dental_record.dental_work_date,  db.dental_record.tooth, db.dental_record.dental_work, db.dental_record.charge, db.dental_record.dental_lab, db.dental_record.material, hidden=dict(tp_id='', sum_adj=''), table_name='ctp_table', _id='form_details_ctp')
    form_details_ctp.element('input[name=dental_work_date]')['_style']='width:100px'
    form_details_ctp.element('select[name=tooth]')['_style']='width:60px'
    form_details_ctp.element('select[name=dental_work]')['_style']='width:250px'
    form_details_ctp.element('input[name=charge]')['_style']='width:100px'
    form_details_ctp.element('select[name=dental_lab]')['_style']='width:250px'
    form_details_ctp.element('select[name=material]')['_style']='width:250px'
    if form_details_ctp.validate(form_name='ctp'):
        if request.vars.action == 'sum_adjust':
            sum1 = 0
            sum2 = int(request.vars.sum_adj)
            for i in request.vars:
                if i[:8] == 'work_id_': 
                    sum1 = sum1 + db.dental_record(i[8:]).charge
            for i in request.vars:
                if i[:8] == 'work_id_': 
                    charge_orig = db.dental_record(i[8:]).charge
                    db(db.dental_record.id == i[8:]).update(charge = (charge_orig*sum2)/sum1)
        if request.vars.action == 'del_work':
            for i in request.vars:
                if i[:8] == 'work_id_': 
                    db(db.dental_record.id == i[8:]).delete()
        if request.vars.action == 'save_work':
            i = request.vars.cur_rec_id
            db(db.dental_record.id == i).validate_and_update(dental_work_date = request.vars.dental_work_date, tooth = request.vars.tooth, dental_work =  request.vars.dental_work, dental_lab = request.vars.dental_lab, material = request.vars.material, charge = request.vars.charge)
        if request.vars.action == 'transf_work':
            ids = []
            for i in request.vars:
                if i[:8] == 'work_id_': 
                    db(db.dental_record.id == i[8:]).update(done = not db.dental_record(i[8:]).done, dental_work_date = db.dental_record.dental_work_date.default) 
        if request.vars.action == 'copy_work':
            for i in request.vars:
                if i[:8] == 'work_id_': 
                    row = db.dental_record(i[8:])
                    therapy_plan_id = request.vars.tp_id[6:]
                    dental_work = row.dental_work
                    tooth = row.tooth
                    material = row.material
                    dental_lab = row.dental_lab
                    charge = row.charge
                    tpid = db.therapy_plan_works.insert(dental_work = dental_work, tooth = tooth, material = material, dental_lab = dental_lab, charge = charge, therapy_plan = therapy_plan_id)
        if request.vars.action == 'move_work':
            for i in request.vars:
                if i[:8] == 'work_id_': 
                    row = db.dental_record(i[8:])
                    therapy_plan_id = request.vars.tp_id[6:]
                    dental_work = row.dental_work
                    tooth = row.tooth
                    material = row.material
                    dental_lab = row.dental_lab
                    charge = row.charge
                    tpid = db.therapy_plan_works.insert(dental_work = dental_work, tooth = tooth, material = material, dental_lab = dental_lab, charge = charge, therapy_plan = therapy_plan_id)
                    if tpid:
                       db(db.dental_record.id == i[8:]).delete()
        redirect(URL('dental_record', args=[request.args(0)], vars = dict(tab='li_tab1')))
    active_tab = INPUT(_name='active_tab', _type='hidden')
    cur_rec_id = INPUT(_name='cur_rec_id', _type='hidden')
    return locals()

def therapy_plan_details(): 
    if (request.vars.action == 'set_tp_current') or (request.vars.action == 'add_tp_current'):
        therapy_plan_id = request.vars.tp_id[13:]
        if request.vars.action == 'set_tp_current':
            db(db.dental_record.done == False).delete()
        query = (db.therapy_plan_works.therapy_plan == therapy_plan_id)
        rows = db(query).select(db.therapy_plan_works.ALL)
        for row in rows:
            tooth = row.tooth
            dental_work = row.dental_work
            material = row.material
            dental_lab = row.dental_lab
            charge = row.charge
            dental_work_date = row.tpw_date
            tpid = db.dental_record.insert(patient = request.args(0), dental_work = dental_work, tooth = tooth, material = material, dental_lab = dental_lab, charge = charge, dental_work_date =dental_work_date, done = False)
        redirect(URL('dental_record', args=request.args(0), vars=dict(tab='li_tab1'), extension=False), client_side=True)
    form_tp_details = SQLFORM.factory(db.therapy_plan_works.id, db.therapy_plan_works.tpw_date,  db.therapy_plan_works.dental_work, db.therapy_plan_works.dental_lab,db.therapy_plan_works.material,db.therapy_plan_works.tooth, db.therapy_plan_works.charge, hidden=dict(tp_id='', sum_adj=''), table_name='tp_details_table', _id='form_tp_details')
    form_tp_details.element('input[name=tpw_date]')['_style']='width:80px'
    form_tp_details.element('select[name=tooth]')['_style']='width:60px'
    form_tp_details.element('select[name=dental_work]')['_style']='width:130px'
    form_tp_details.element('input[name=charge]')['_style']='width:80px'
    form_tp_details.element('select[name=dental_lab]')['_style']='width:120px'
    form_tp_details.element('select[name=material]')['_style']='width:130px'   
    if form_tp_details.validate():
        response.flash = False
        if request.vars.action == 'sum_adjust':
            sum1 = 0
            sum2 = int(request.vars.sum_adj)
            for i in request.vars:
                if i[:8] == 'tpdw_id_': 
                    sum1 = sum1 + db.therapy_plan_works(i[8:]).charge
            for i in request.vars:
                if i[:8] == 'tpdw_id_': 
                    charge_orig = db.therapy_plan_works(i[8:]).charge
                    db(db.therapy_plan_works.id == i[8:]).update(charge = (charge_orig*sum2)/sum1)
        if request.vars.action == 'del_work':
            for i in request.vars:
                if i[:8] == 'tpdw_id_': 
                    db(db.therapy_plan_works.id == i[8:]).delete()
        if request.vars.action == 'save_work':
            i = request.vars.cur_rec_id
            db(db.therapy_plan_works.id == i).validate_and_update(tpw_date = request.vars.tpw_date, tooth = request.vars.tooth, dental_work = request.vars.dental_work, dental_lab = request.vars.dental_lab, material = request.vars.material, charge = request.vars.charge)
        if request.vars.action == 'copy_work':
            for i in request.vars:
                if i[:8] == 'tpdw_id_': 
                    row = db.therapy_plan_works(i[8:])
                    therapy_plan_id = request.vars.tp_id[6:]
                    dental_work = row.dental_work
                    tooth = row.tooth
                    material = row.material
                    dental_lab = row.dental_lab
                    charge = row.charge
                    tpid = db.therapy_plan_works.validate_and_insert(dental_work = dental_work, tooth = tooth, material = material, dental_lab = dental_lab, charge = charge, therapy_plan = therapy_plan_id)
        if request.vars.action == 'move_work':
            for i in request.vars:
                if i[:8] == 'tpdw_id_': 
                    row = db.therapy_plan_works(i[8:])
                    therapy_plan_id = request.vars.tp_id[6:]
                    dental_work = row.dental_work
                    tooth = row.tooth
                    material = row.material
                    dental_lab = row.dental_lab
                    charge = row.charge
                    tpid = db.therapy_plan_works.validate_and_insert(dental_work = dental_work, tooth = tooth, material = material, dental_lab = dental_lab, charge = charge, therapy_plan = therapy_plan_id)
                    if tpid:
                       db(db.therapy_plan_works.id == i[8:]).delete()           
    if request.args(1):
        rows4 = db(db.therapy_plan_works.therapy_plan == request.args(1)).select(db.therapy_plan_works.ALL, orderby=~db.therapy_plan_works.tpw_date)
    else:
        rows4 = [] 
    if not rows4:
        table4 = TABLE(THEAD(TR(TH(T('DATE')), TH(T('TOOTH')), TH(T('DENTAL WORK')), TH(T('CHARGE')), TH(T('LAB')), TH(T('MATERIAL')), TH(T('')))), TBODY(), _id='tp_dw', _class='master pretty1')
    else:    
        extracolumns4 = [{'label':'' , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc: SPAN(INPUT(_type='checkbox', _style="visibility: hidden;", _name='tpdw_id_' + str(row.id)))}]
        table4 = SQLTABLE(rows4, _id="tp_dw", _class='master pretty1', headers='labels', columns=["therapy_plan_works.tpw_date", "therapy_plan_works.tooth", "therapy_plan_works.dental_work", "therapy_plan_works.charge", "therapy_plan_works.dental_lab", "therapy_plan_works.material" ], 
extracolumns=extracolumns4)
    active_tab = INPUT(_name='active_tab', _type='hidden')
    cur_rec_id = INPUT(_name='cur_rec_id', _type='hidden')
    rows3 = db(db.therapy_plan.patient == request.args(0)).select(db.therapy_plan.ALL)
    return dict(table4=table4, form_tp_details=form_tp_details, active_tab = active_tab, cur_rec_id = cur_rec_id, rows3=rows3)

def delete_dental_record():
    remove = db(db.dental_record.id == request.args(0)).delete()
    if remove:
        redirect(URL('dental_record', args=session.current_id))
    return dict(remove=remove)      
        
def calendar():
    patient_name = '%(lastname)s %(firstname)s' % dict(lastname=db.patients(request.args(0)).lastname, firstname=db.patients(request.args(0)).firstname)
    form=SQLFORM( db.appointments )
    form.element('input[name=ap_start]')['_style']='width:70px'
    form.element('input[name=ap_end]')['_style']='width:70px'
    form.element('textarea[name=notes]')['_style']='width:360px;height:80px'
    db(db.therapy_plan.patient == request.args(0)).select(db.therapy_plan.ALL)
    if form.process().accepted:
        response.flash = 'record Saved!' 
        if request.vars.delete:
            db.appointments().delete_record()
            redirect(URL('index')) 
        redirect(URL('calendar', args=(request.args or session.current_id)))  
    elif form.errors:
        response.flash = T('there are errors!')
    return dict(form=form, patient_name=patient_name)

def events_to_json():
    start = datetime.datetime.fromtimestamp(int(request.vars.start)).strftime('%Y-%m-%d %H:%M:%S')
    end = datetime.datetime.fromtimestamp(int(request.vars.end)).strftime('%Y-%m-%d %H:%M:%S')
    rows = db((db.appointments.ap_start < end) & (db.appointments.ap_start > start)).select()
    events=[]
    for i,row in enumerate(rows):
        events.append({'title': row.title,
            'id': row.id,
            'notes': row.notes,
            'allDay': False,
            'start': row.ap_start.strftime('%Y-%m-%d %H:%M:%S'),
            'end': row.ap_end.strftime('%Y-%m-%d %H:%M:%S'),
            'patient': row.patient})
    import gluon.contrib.simplejson
    return gluon.contrib.simplejson.dumps(events)

def delete_appointment():
    remove = db(db.appointments.id==request.args(0)).delete()

def update_appointment():
    if  request.vars.title:
        db(db.appointments.id==request.args(0)).validate_and_update(title=request.vars.title)
    if  request.vars.ap_end:
        db(db.appointments.id==request.args(0)).validate_and_update(ap_end=request.vars.ap_end)
    if  request.vars.ap_start:
        db(db.appointments.id==request.args(0)).validate_and_update(ap_start=request.vars.ap_start)
    db(db.appointments.id==request.args(0)).validate_and_update(notes=request.vars.notes)
    db(db.appointments.id==request.args(0)).validate_and_update(patient=request.vars.patient)   
 
def create_appointment():
    event_id = db.appointments.validate_and_insert(title=request.vars.title, ap_end=request.vars.ap_end, ap_start=request.vars.ap_start, notes=request.vars.notes, patient=request.vars.patient)
    return "$('#calendar').fullCalendar( 'refetchEvents' );"

def appointments():
    query1 = (db.appointments.patient==request.args(0))
    rows1 = db(query1).select(db.appointments.ALL, orderby=~db.appointments.ap_start)
    if not rows1:
        table1 = TABLE(THEAD(TR( TH(T('Start')), TH(T('Notes')), TH(T('Duration')) )), TBODY(), _id='appointments', _class='master pretty2 table-condensed')
    else:
        extracolumns1 = [{'label':T('Duration') , 'selected': False, 'class':'', 'width':'', 'content':lambda row,rc:(row.ap_end-row.ap_start).seconds/60}]
        table1 = SQLTABLE(rows1, _id="appointments", _class='master pretty2 table-condensed',  headers='labels', columns=["appointments.ap_start", "appointments.notes" ], extracolumns=extracolumns1)
    query2 = (db.dental_record.patient == request.args(0)) & (db.dental_record.done == True)
    rows2 = db(query2).select(db.dental_record.ALL, orderby=~db.dental_record.dental_work_date)
    if not rows2:
        table2 = TABLE(THEAD(TR( TH(T('Date')), TH(T('Dental Work')), TH(T('Charge')) )), TBODY(), _id='table_d_works', _class='master pretty2 table-condensed')
    else:
        table2 = SQLTABLE(rows2, _id="table_d_works", _class='master pretty2 table-condensed',  headers='labels', columns=["dental_record.dental_work_date", "dental_record.dental_work", "dental_record.charge" ])
    patient_name = '%(lastname)s %(firstname)s' %dict(lastname = db.patients[request.args(0)].lastname, firstname = db.patients[request.args(0)].firstname)
    return dict(table1=table1, table2=table2, patient_name=patient_name)

def danger_zone():
    return locals()

def reset_database():
    db.endo.truncate()
    db.colors.truncate()
    db.payments.truncate()
    db(db.images.id>0).delete()
    db.images.truncate()
    db.dental_work_materials.truncate()
    db.pre_existing_dental_works.truncate()
    db.therapy_plan_works.truncate()
    db.therapy_plan.truncate()
    db.dental_record.truncate()
    db.contacts.truncate()
    db.dental_labs.truncate()
    db.dental_labs.insert(lastname=T('LAB'), firstname='1')
    db.dental_labs.insert(lastname=T('LAB'), firstname='2')
    db.dental_work_materials.insert(name='Composite 1')
    db.dental_work_materials.insert(name='Composite 2')
    db.patients.truncate()
    db.appointments.truncate()
    db.medical_conditions.truncate()
    db.patients.insert(lastname=T('Patient'), firstname=T('Default'), notes=T('Default patient'))
    session.current_id = db(db.patients.id>0).select(orderby=~db.patients.id).first().id
    for i in (T('Hepatitis'), T('AIDS'), T('Heart'), T('Antimicrobial prophylaxis'), T('Diabetes')):
        db.medical_conditions.insert(name=i)
    db.dental_works.truncate()
    db.dental_work_categories.truncate()
    for i in ( T('DIRECT RESTOR.'), T('ENDO'), T('PERIO'), T('FIXED PROSTH.'), T('DENTURES'), T('SURGICAL'), T('DIAGNOSTICS') ):
        db.dental_work_categories.insert(name=i)
    db(db.dental_work_graphics.id>0).delete()
    db.dental_work_graphics.truncate()
    import os
    filenames = ('MASIT_1.png', 'MASIT_2.png', 'MASIT_3.png', 'EGGYS_1.png', 'EGGYS_2.png', 'EGGYS_3.png', 'APO_1.png', 'APO_2.png', 'APO_3.png', 'ANASYST_APO_1.png', 'ANASYST_APO_2.png','ANASYST_APO_3.png', 'ANASYST_EGG_1.png', 'ANASYST_EGG_2.png','ANASYST_EGG_3.png', 'APO_MAS_1.png', 'APO_MAS_2.png','APO_MAS_3.png', 'AYXEN_1.png', 'AYXEN_2.png','AYXEN_3.png','AYXEN_4.png','AYXEN_5.png','AYXEN_6.png', 'AYXEN_7.png', 'DONTIA_MERIKIS.png', 'EGG_AP_MAS_1.png', 'EGG_AP_MAS_2.png','EGG_AP_MAS_3.png', 'EGGYS_MAS_1.png', 'EGGYS_MAS_2.png', 'EGGYS_MAS_3.png', 'EKSAGOGES_FINAL.png', 'ENDO.png', 'KATHAR.png', 'ODONTOSTOIXIES.png', 'PROKAT_AXONES.png', 'STEFANES2.png', 'XYTOI_AXONES.png')
    titles = ( T('OCCL. BLUE 1'), T('OCCL. YELLOW'),T('OCCL. BLUE 2'), T('MESIAL BLUE 1'), T('MESIAL YELLOW '), T('MESIAL BLUE 2'), T('DISTAL BLUE 1'), T('DISTAL YELLOW'), T('DISTAL BLUE 2'), T('BIG DISTAL BLUE 1'), T('BIG DISTAL YELLOW'), T('BIG DISTAL BLUE 2'), T('BIG MESIAL BLUE'), T('BIG MESIAL YELLOW'), T('BIG MESIAL RED'), T('DISTAL OCCL. BLUE 1'),  T('DISTAL OCCL. YELLOW'), T('DISTAL OCCL. BLUE 2'),  T('CERVICAL BLUE 1'), T('CERVICAL YELLOW'),T('CERVICAL BLUE 2'), T('CERVICAL GREEN'), T('CERVICAL PINK'), T('CERVICAL RED 1'), T('CERVICAL RED 2'), T('DENTURE TEETH'), T('MES-DIST-OCCL BLUE 1'), T('MES-DIST-OCCL YELLOW'), T('MES-DIST-OCCL BLUE 2'), T('MESIAL OCCL. BLUE 1'), T('MESIAL OCCL. YELLOW'), T('MESIAL OCCL. BLUE 2'), T('EXTRACTION'), T('ENDO'), T('PERIO'), T('DENTURE'), T('PREFABRICATED POST'), T('CROWN'), T('CAST POST') )
    for i,x  in zip(filenames, titles):
        pathfilename=os.path.join(request.folder, 'static', 'images', 'dentworks_old', i )
        stream = open(pathfilename, 'rb')
        db.dental_work_graphics.insert(title = x, file = stream)
    db.separation.truncate()
    for i in (T('TOOTH'), T('JAW'), T('MOUTH QUARTER'), T('FRONT-BACK LEFT-BACK RIGHT'), T('FULL MOUTH')):
        db.separation.insert(separation_name=i)
    db.dental_works.insert(name=T('OCCLUSAL FILLING'), category='1', graphic='1', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('MESIAL OCCL.FILLING'), category='1', graphic='30', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('DISTAL OCCL.FILLING'), category='1', graphic='16', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('MESIAL FILLING'), category='1', graphic='4', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('DISTAL FILLING'), category='1', graphic='7', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('LARGE MESIAL FILLING'), category='1', graphic='13', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('LARGE DISTAL FILLING'), category='1', graphic='10', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('MES-OCCL-DIST FILLING'), category='1', graphic='27', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('CERVICAL FILLING'), category='1', graphic='19', graphic_category='4', separation='1', price=60 )
    db.dental_works.insert(name=T('ROOT CANAL ANTERIOR'), category='2', graphic='34', graphic_category='4', separation='1', price=100 )
    db.dental_works.insert(name=T('ROOT CANAL POSTERIOR'), category='2', graphic='34', graphic_category='4', separation='1', price=150 )
    db.dental_works.insert(name=T('CLEANING'), category='3', graphic='35', graphic_category='5', separation='5', price=50 )
    db.dental_works.insert(name=T('GINGIVITIS THERAPY'), category='3', graphic='35', graphic_category='5', separation='5', price=150 )
    db.dental_works.insert(name=T('PERIODONTITIS THERAPY'), category='3', graphic='35', graphic_category='5', separation='5', price=1000 )
    db.dental_works.insert(name=T('PORCELAIN-FUSED-TO-METAL CROWN'), category='4', graphic='38', graphic_category='4', separation='1', price=300 )
    db.dental_works.insert(name=T('ALL CERAMIC CROWN'), category='4', graphic='38', graphic_category='4', separation='1', price=400 )
    db.dental_works.insert(name=T('DENTURE'), category='5', graphic='36', graphic_category='1', separation='2', price=600 )
    db.dental_works.insert(name=T('PARTIAL DENTURE'), category='5', separation='2', price=700)
    db.dental_works.insert(name=T('PARTIAL DENTURE TOOTH'), category='5', graphic='26', graphic_category='3', separation='1', price=0 )
    db.dental_works.insert(name=T('EXTRACTION SIMPLE'), category='6', graphic='33', graphic_category='2', separation='1', price=60 )
    db.dental_works.insert(name=T('EXTRACTION SURGICAL'), category='6', graphic='33', graphic_category='2', separation='1', price=250 )
    db.dental_works.insert(name=T('X-RAY'), category='7', price=20 )
    db.dental_works.insert(name=T('EXAMINATION-DIAGNOSIS'), category='7', price=40 )
    db.teeth.truncate()
    pathfilename = os.path.join(request.folder, 'db_teeth_original.csv' )
    db.teeth.import_from_csv_file(open(pathfilename, 'r'))
    db.teeth.insert(tooth=T('UPPER JAW'), upper=True, permanent=True, separation='2', x1=0, y1=0, x2=622, y2=148, horizontal_offset_for_source=0)
    db.teeth.insert(tooth=T('LOWER JAW'), upper=False, permanent=True, separation='2', x1=0, y1=149, x2=622, y2=296, horizontal_offset_for_source=0)
    db.teeth.insert(tooth=T('FULL MOUTH'), upper=False, permanent=True, separation='5', x1=0, y1=0, x2=622, y2=296, horizontal_offset_for_source=0)
    redirect(URL('danger_zone'))

def reset_patients_appointments():
    db.endo.truncate()
    db.colors.truncate()
    db.payments.truncate()
    db(db.images.id>0).delete()
    db.images.truncate()
    db.pre_existing_dental_works.truncate()
    db.dental_record.truncate()
    db.therapy_plan_works.truncate()
    db.therapy_plan.truncate()
    db.contacts.truncate()
    db.dental_labs.truncate()
    db.dental_labs.insert(lastname=T('LAB'), firstname='1')
    db.dental_labs.insert(lastname=T('LAB'), firstname='2')
    db.patients.truncate()
    db.patients.insert(lastname=T('Patient'), firstname=T('Default'), notes=T('Default patient'))
    session.current_id = db(db.patients.id>0).select(orderby=~db.patients.id).first().id
    db.appointments.truncate()
    redirect(URL('danger_zone'))

def backup():
    import gluon.contenttype
    import StringIO
    s = StringIO.StringIO()
    db.export_to_csv_file(s)
    response.headers['Content-Type'] = gluon.contenttype.contenttype('.csv')
    response.headers['Content-disposition'] = 'attachment; filename=backup_dental_db.csv'
    return s.getvalue()

def restore():
    formcsv = FORM( INPUT(_type='submit',_value=T('RESTORE!!!'), _class="btn btn-red"),
                    str(T('Select file for restore:'))+" ",   
                    INPUT(_type='file',_name='csvfile', _style='width:260px;'),)
    if formcsv.process().accepted:
        try:
            for table in db.tables: db[table].truncate()
            db.import_from_csv_file(request.vars.csvfile.file)
            response.flash = T('data uploaded')
        except Exception, e:
            response.flash = DIV(T('unable to parse csv file'),PRE(str(e)))
    return dict(formcsv=formcsv)

def index_dental_work():
    table_title=T('Dental Works')
    grid=SQLFORM.grid(db.dental_works, editable=True, deletable=True, create=True, details=True, user_signature=False)
    return dict(grid=grid, table_title=table_title)

def index_material():
    table_title=T('Materials')
    grid=SQLFORM.grid(db.dental_work_materials, editable=True, deletable=True, create=True, details=True, user_signature=False)
    return dict(grid=grid, table_title=table_title)

def index_graphic():
    table_title=T('Graphics for Dental Works')
    grid=SQLFORM.grid(db.dental_work_graphics, editable=True, deletable=True, create=True, details=True, user_signature=False)
    return dict(grid=grid, table_title=table_title)

def help():
    return locals()

def about():
    import os
    filename = os.path.join(request.folder, T('ABOUT', lazy=False))
    return response.render(dict(license=MARKMIN(read_file(filename))))

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

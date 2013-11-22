# -*- coding: utf-8 -*-

import datetime, os


#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
#
#teeth = ('11','12','13','14','15','16','17','18','21','22','23','24','25','26','27','28',
#    '31','32','33','34','35','36','37','38','41','42','43','44','45','46','47','48',
#    T('ΟΛΟΣ Ο ΦΡΑΓΜΟΣ'),T('ΑΝΩ ΓΝΑΘΟΣ'), T('ΚΑΤΩ ΓΝΑΘΟΣ'), T('ΠΡΟΣΘΙΑ ΑΝΩ'), T('ΠΡΟΣΘΙΑ ΚΑΤΩ'), T('ΠΙΣΩ ΑΝΩ ΑΡΙΣΤΕΡΑ'),T('ΠΙΣΩ ΑΝΩ ΔΕΞΙΑ'),
#    T('ΠΙΣΩ ΚΑΤΩ ΑΡΙΣΤΕΡΑ'), T('ΠΙΣΩ ΚΑΤΩ ΔΕΞΙΑ'),T('ΑΝΩ ΔΕΞΙΑ ΤΕΤΑΡΤΗΜΟΡΙΟ'), T('ΑΝΩ ΑΡΙΣΤΕΡΑ ΤΕΤΑΡΤΗΜΟΡΙΟ'), T('ΚΑΤΩ ΔΕΞΙΑ ΤΕΤΑΡΤΗΜΟΡΙΟ'),
#    T('ΚΑΤΩ ΑΡΙΣΤΕΡΑ ΤΕΤΑΡΤΗΜΟΡΙΟ'))
    
LENGTH_CHOICES=(('9','9'),('9.5','9.5'),('10','10'),('10.5','10.5'),('11','11'),('11.5','11.5'),
        ('12','12'),('12.5','12.5'),('13','13'),('13.5','13.5'),('14','14'),('14.5','14.5'),('15','15'),
        ('15.5','15.5'),('16','16'),('16.5','16.5'),('17','17'),('17.5','17.5'),('18','18'),('18.5','18.5'),
        ('19','19'),('19.5','19,5'),('20','20'),('20.5','20.5'),('21','21'),('21.5','21.5'),('22','22'),
        ('22.5','22.5'),('23','23'),('23.5','23.5'),('24','24'),('24.5','24.5'),('25','25'),('25.5','25.5'),
        ('26','26'),('26.5','26.5'),('27','27'))
DIEYR_CHOICES=(('15','15'),('20','20'),('25','25'),('30','30'),('35','35'),('40','40'),
        ('45','45'),('50','50'),('55','55'),('60','60'),('70','70'),('80','80'),('90','90'))
TAPER_CHOICES=(('.02','.02'),('.04','.04'),('.06','.06'),('.08','.08'),('.10','.10'),('.12','.12'))

db = DAL('sqlite://storage.db')

db.define_table('medical_conditions', 
    Field('name', label = T('Condition'), requires=IS_UPPER()),
    singular=T('Medical Condition'), plural = T('Medical Conditions'),
    format='%(name)s'
) 

db.define_table('patients', 
#   Field('lastname', label=T('Lastname'),requires=IS_UPPER(), represent=lambda value,row:A(value,_href=URL('patient_update',args=row.id)) ),
    Field('lastname', label=T('Lastname'),requires=IS_UPPER()),
    Field('firstname', label=T('Firstname'), requires=IS_UPPER()),
    Field('address', label=T('Address'),requires=IS_UPPER()),
    Field('city', label=T('City'), requires=IS_UPPER()),
    Field('zipcode', label=T('Zip Code')),
    Field('birthday', 'date', label=T('Date of Birth')),
    Field('telhome', label=T('Home Phone')),
    Field('telwork', label=T('Office Phone')),
    Field('telmobile', label=T('Mobile')),
    Field('sex', length=1, label=T('Sex')),
    Field('profession', label=T('Profession'), requires=IS_UPPER()),
    Field('fathername', label=T("Father's Name"), requires=IS_UPPER()),
    Field('balance', 'decimal(7,2)', label=T('Balance')),
    Field('datefirstvisit', 'date', label=T('First Visit'), default=datetime.date.today()),
    Field('datelastvisit', 'date', label=T('Last Visit'), default=datetime.date.today()),
    Field('daterecall', 'date', label=T('Recall Date')),
    Field('insurance', label=T('Insurance'), requires=IS_UPPER()),
    Field('notes', 'text', label=T('Notes'), requires=IS_UPPER()),
    Field('referredby', label=T('Referred by'), requires=IS_UPPER()),
    Field('referredby_tel', label=T('Telephone of referrer')),
    Field('medical_record', 'list:reference medical_conditions', label=T('Medical Record'), widget = SQLFORM.widgets.checkboxes.widget),
    Field('medicalhistnotes', 'text', label=T('Medical Record details'), requires=IS_UPPER()),
    Field('email', label='e-mail'),
    Field('contact', 'boolean', label=T('Add to contacts')),
    singular=T('Patient'), plural=T('Patients'),
    format='%(lastname)s %(firstname)s'
)

db.patients.sex.requires=IS_EMPTY_OR(IS_IN_SET({'M': 'Male', 'F': 'Female'}))
db.patients.birthday.requires = IS_EMPTY_OR(IS_DATE(format=T('%Y-%m-%d')))
db.patients.birthday.represent = lambda value, row: "" if not row.birthday else value.strftime(T("%Y-%m-%d", lazy=False))
db.patients.datefirstvisit.requires = IS_EMPTY_OR(IS_DATE(format=T('%Y-%m-%d')))
db.patients.datefirstvisit.represent = lambda value, row: "" if not row.datefirstvisit else value.strftime(T("%Y-%m-%d", lazy=False))
db.patients.datelastvisit.requires = IS_EMPTY_OR(IS_DATE(format=T('%Y-%m-%d')))
db.patients.datelastvisit.represent = lambda value, row: "" if not row.datelastvisit else value.strftime(T("%Y-%m-%d", lazy=False))
db.patients.daterecall.requires = IS_EMPTY_OR(IS_DATE(format=T('%Y-%m-%d')))
db.patients.daterecall.represent = lambda value, row: "" if not row.daterecall else value.strftime(T("%Y-%m-%d", lazy=False))

#class MyVirtualFields(object):
#    def age(self):
#        return int((datetime.now() - self.patients.birthday).days/360.25)
#db.patients.virtualfields.append(MyVirtualFields())
#db.patients.age = Field.Virtual(lambda row: int((datetime.date.today() - row.patients.birthday).days/360))    
            
db.define_table('dental_work_categories', 
    Field('name', label=T('Dental Work Category')),
    singular=T('Dental Work Category'), plural=T('Dental Work Categories'),
    format='%(name)s'
)

db.define_table('dental_work_materials', 
    Field('name', label=T('Material'), requires=IS_UPPER()),
    singular=T('MATERIAL'), plural=T('MATERIALS'),
    format='%(name)s'
)

db.define_table('dental_labs', 
    Field('lastname', label=T('Lastname'), requires=IS_UPPER()),
    Field('firstname', label=T('Firstname'), requires=IS_UPPER()),
    Field('address', label=T('Address'), requires=IS_UPPER()),
    Field('city', label=T('City'), requires=IS_UPPER()),
    Field('zipcode', label=T('Zip Code')),
    Field('tel1', label=T('Telephone 1')),
    Field('tel2', label=T('Telephone 2')),
    Field('telmobile', label=T('Mobile')),
    Field('email', label='e-mail', requires = IS_EMPTY_OR(IS_EMAIL(error_message=T('invalid email!')))
),
    Field('notes', 'text', label=T('Notes'), requires=IS_UPPER()),
    singular=T('DENTAL LAB'), plural=T('DENTAL LABS'),
    format='%(lastname)s %(firstname)s'
)

db.define_table('dental_work_graphics', 
    Field('title', label=T('Title'), requires=IS_UPPER()),
    Field('file', 'upload', uploadfolder=os.path.join(request.folder,'static','images', 'dentworks')),
    singular=T('Graphic'), plural=T('Graphics'),
    format='%(title)s'
)
   
db.define_table('separation',
    #Type of mouth separation used by tooth(=mouth_area) table
    #and dental_works table, e.g.
    #1.Tooth
    #2.Jaws
    #3.Mouth Quarters
    #4.Full Mouth
    #5.Front, RearLeft,RearRight
    #
    Field('separation_name', label=T('Type of Mouth Separation'), requires=IS_UPPER()),
    format='%(separation_name)s'
)    
    
db.define_table('dental_works', 
    #Graphic Category:
    #Category 1 Dental Works - full dentures
    #Category 2 Dental Works  - extractions
    #Category 3 Dental Works - works on any tooth
    #Category 4 Dental Works - works on non-extracted teeth
    #FULL MOUTH - Category 5 Dental Works - works on the whole mouth
    Field('name', label=T('Name'), requires=IS_UPPER()),
    Field('category', db.dental_work_categories),
    Field('graphic', db.dental_work_graphics),
    Field('graphic_category', 'integer', label=u'Κατηγορία Απεικόνισης', requires=IS_EMPTY_OR(IS_IN_SET((1,2,3,4,5)))),
    Field('separation', db.separation),
    #Field('show_as_doable', 'boolean'), #0:not doable, 1:doable
    Field('price','decimal(7,2)', label=T('Price')),
    singular=T('Dental Work'), plural=T('Dental Works'),
    format='%(name)s'
)

db.dental_works.separation.requires=IS_IN_DB(db, 'separation.id', '%(separation_name)s', zero=None)

db.define_table('teeth', 
    Field('tooth', label=T('Tooth'), requires=IS_UPPER()),
    Field('upper', 'boolean'),
    Field('permanent', 'boolean'),
    Field('separation', db.separation),
    Field('x1', 'integer'),
    Field('y1', 'integer'),
    Field('x2', 'integer'),
    Field('y2', 'integer'),
    Field('horizontal_offset_for_source', 'integer', default = 0),
    singular=T('Tooth'), plural=T('Teeth'),
    #format='%(tooth)s'
    format=lambda r: DIV(r.tooth, _style='text-align:center;')
)
        
db.define_table('pre_existing_dental_works',
    Field('patient', db.patients),
    Field('dental_work', db.dental_works,label=T('DENTAL WORK')),
    Field('material', db.dental_work_materials, label=T('MATERIAL')),
    Field('tooth', db.teeth, label=T('TOOTH/AREA')),
    singular=T('Pre existing Dental Record'), plural=T('Pre existing Dental Works'),
    format='%(name)s'
)

db.pre_existing_dental_works.material.requires=IS_EMPTY_OR(IS_IN_DB(db, 'dental_work_materials.id', '%(name)s'))
db.pre_existing_dental_works.dental_work.requires=IS_IN_DB(db, 'dental_works.id', '%(name)s', zero=None)
db.pre_existing_dental_works.material.represent = lambda value, row: "" if not row.material else row.material.name

db.define_table('dental_record',
    Field('patient', db.patients, ondelete='NO ACTION'), #
    Field('dental_work', db.dental_works, label=T('DENTAL WORK')),
    Field('dental_lab', db.dental_labs, label=T('DENTAL LAB')),
    Field('material', 'list:reference dental_work_materials', label=T('MATERIAL')),
    Field('dental_work_date', 'date', label=T('DATE'), default=datetime.date.today()),
    Field('tooth', db.teeth, label=T('TOOTH/AREA')),
    Field('price', 'decimal(7,2)', label=T('PRICE'), readable=False, writable=False),
    Field('charge', 'decimal(7,2)', label=T('CHARGE')),
    Field('done', 'boolean', default=False),
    singular=T('Dental Record'), plural=T('Dental Records'),
    format='%(dental_work)s %(dental_work_date)s'
)
db.dental_record.dental_work.requires=IS_IN_DB(db, 'dental_works.id', '%(name)s', zero=None)
db.dental_record.dental_lab.requires=IS_EMPTY_OR(IS_IN_DB(db, 'dental_labs.id', '%(lastname)s %(firstname)s'))
db.dental_record.material.requires=IS_EMPTY_OR(IS_IN_DB(db, 'dental_work_materials.id', '%(name)s'))
db.dental_record.charge.represent = lambda value, row: DIV('€ %0.2f' % (0.00 if value == None else value), _style='text-align: right;color:green')
db.dental_record.material.represent = lambda value, row: "" if not row.material else row.material[0].name
db.dental_record.dental_lab.represent = lambda value, row: "" if not row.dental_lab else "%s %s" %(row.dental_lab.lastname, row.dental_lab.firstname)
db.dental_record.dental_work_date.requires = IS_DATE(format=T('%Y-%m-%d'))
db.dental_record.dental_work_date.represent = lambda value, row: value.strftime(T("%Y-%m-%d", lazy=False))

db.define_table('therapy_plan',
    Field('patient', db.patients, readable=False, writable=False, ondelete='NO ACTION'),
    Field('tp_date', 'date', label=T('DATE'), default=datetime.date.today()),
    Field('tp_name', label=T('Plan name'), requires=IS_UPPER()),
    singular=T('Therapy Plan'), plural=T('Therapy Plans'),
    format='%(tp_date)s  %(tp_name)s'
)
db.therapy_plan.tp_date.requires = IS_DATE(format=T('%Y-%m-%d'))
db.therapy_plan.tp_date.represent = lambda value, row: value.strftime(T("%Y-%m-%d", lazy=False))

    
db.define_table('therapy_plan_works',
    Field('tpw_date', 'date', label=T('DATE'), default=datetime.date.today()),
    Field('therapy_plan', db.therapy_plan, label=T('THERAPY PLAN')),
    Field('dental_work', db.dental_works,label=T('DENTAL WORK')),
    Field('dental_lab', db.dental_labs),
    Field('material', 'list:reference dental_work_materials'),
    Field('tooth', db.teeth, label=T('TOOTH/AREA')),
    Field('price', 'decimal(7,2)', label=T('PRICE'), readable=False, writable=False),
    Field('charge', 'decimal(7,2)', label=T('CHARGE')),
    singular=T('Candidate Dental Work'), plural=T('Candidate Dental Works'),
    format='%(dental_work.name)s %(tpw_date)s'
)

db.therapy_plan_works.dental_lab.requires=IS_EMPTY_OR(IS_IN_DB(db, 'dental_labs.id', '%(lastname)s %(firstname)s'))
db.therapy_plan_works.material.requires=IS_EMPTY_OR(IS_IN_DB(db, 'dental_work_materials.id', '%(name)s'))
db.therapy_plan_works.dental_work.requires=IS_IN_DB(db, 'dental_works.id', '%(name)s', zero=None)
db.therapy_plan_works.charge.represent = lambda value, row: DIV('€ %0.2f' % (0.00 if value == None else value), _style='text-align: right;color:green')
db.therapy_plan_works.material.represent = lambda value, row: "" if not row.material else row.material[0].name
db.therapy_plan_works.dental_lab.represent = lambda value, row: "" if not row.dental_lab else "%s %s" %(row.dental_lab.lastname, row.dental_lab.firstname)
db.therapy_plan_works.tpw_date.requires = IS_DATE(format=T('%Y-%m-%d'))
db.therapy_plan_works.tpw_date.represent = lambda value, row: value.strftime(T("%Y-%m-%d", lazy=False))

db.define_table('colors',
    Field('tooth', db.teeth, label=T('TOOTH')),
    Field('date', 'date', label=T('DATE'), default=datetime.date.today()),
    Field('patient', db.patients, writable=False ),
    Field('n_color', label=T('NECK'), requires=IS_UPPER()),
    Field('i_color', label=T('INCISAL'), requires=IS_UPPER()),
    Field('m_color', label=T('MESIAL'), requires=IS_UPPER()),
    Field('d_color', label=T('DISTAL'), requires=IS_UPPER()),
    singular=T('Color'), plural=T('Colors')
)
db.colors.tooth.requires=IS_IN_DB(db, 'teeth.id', '%(tooth)s')
db.colors.date.requires = IS_DATE(format=T('%Y-%m-%d'))
db.colors.date.represent = lambda value, row: value.strftime(T("%Y-%m-%d", lazy=False))

db.define_table('payments',
    Field('patient', db.patients, ondelete='NO ACTION', writable=False ),
    Field('date', 'date', label=T('DATE'), default=datetime.date.today()),
    Field('amount', 'decimal(7,2)', label=T('AMOUNT')),
    Field('receipt_no', label=T('RECEIPT NO')),  
    Field('receipt_amount','decimal(7,2)', label=T('RECEIPT AMOUNT')),
    singular=T('Payment'), plural=T('Payments')
)

db.payments.date.requires = IS_DATE(format=T('%Y-%m-%d'))
db.payments.date.represent = lambda value, row: value.strftime(T("%Y-%m-%d", lazy=False))

db.define_table('endo',
    Field('patient', db.patients, ondelete='NO ACTION', writable=False ),
    Field('date', 'date', label=T('DATE'), default=datetime.date.today()),
    Field('tooth', db.teeth, label=T('TOOTH')),
    Field('notes', 'text', label=T('Notes'),requires=IS_UPPER()),
    Field('eplength',label=u'Μήκος Εγγύς Παρειακού', requires=IS_EMPTY_OR(IS_IN_SET(LENGTH_CHOICES))),
    Field('aplength',label=u'Μήκος Άπω Παρειακού', requires=IS_EMPTY_OR(IS_IN_SET(LENGTH_CHOICES))),
    Field('eglength',label=u'Μήκος Εγγύς Γλωσσικού', requires=IS_EMPTY_OR(IS_IN_SET(LENGTH_CHOICES))),
    Field('aglength',label=u'Μήκος Άπω Γλωσσικού', requires=IS_EMPTY_OR(IS_IN_SET(LENGTH_CHOICES))),
    Field('ylength',label=u'Μήκος Υπερώιου', requires=IS_EMPTY_OR(IS_IN_SET(LENGTH_CHOICES))),
    Field('epdieyr',label=u'Διεύρυνση Εγγύς Παρειακού', requires=IS_EMPTY_OR(IS_IN_SET(DIEYR_CHOICES))),
    Field('apdieyr',label=u'Διεύρυνση Άπω Παρειακού', requires=IS_EMPTY_OR(IS_IN_SET(DIEYR_CHOICES))),
    Field('egdieyr',label=u'Διεύρυνση Εγγύς Γλωσσικού', requires=IS_EMPTY_OR(IS_IN_SET(DIEYR_CHOICES))),
    Field('agdieyr',label=u'Διεύρυνση Άπω Γλωσσικού', requires=IS_EMPTY_OR(IS_IN_SET(DIEYR_CHOICES))),
    Field('ydieyr',label=u'Διεύρυνση Υπερώιου', requires=IS_EMPTY_OR(IS_IN_SET(DIEYR_CHOICES))),
    Field('eptaper',label=u'Κωνικότητα Διεύρυνσης Εγγύς Παρειακού', requires=IS_EMPTY_OR(IS_IN_SET(TAPER_CHOICES))),
    Field('aptaper',label=u'Κωνικότητα Διεύρυνσης Άπω Παρειακού', requires=IS_EMPTY_OR(IS_IN_SET(TAPER_CHOICES))),
    Field('egtaper',label=u'Κωνικότητα Διεύρυνσης Εγγύς Γλωσσικού', requires=IS_EMPTY_OR(IS_IN_SET(TAPER_CHOICES))),
    Field('agtaper',label=u'Κωνικότητα Διεύρυνσης Άπω Γλωσσικού', requires=IS_EMPTY_OR(IS_IN_SET(TAPER_CHOICES))),
    Field('ytaper',label=u'Κωνικότητα Διεύρυνσης Υπερώιου', requires=IS_EMPTY_OR(IS_IN_SET(TAPER_CHOICES))),
    singular=T('Endodontic Therapy'), plural=T('Endodontic Therapies')
)

db.endo.tooth.requires=IS_IN_DB(db, 'teeth.id', '%(tooth)s')
db.endo.date.requires = IS_DATE(format=T('%Y-%m-%d'))
db.endo.date.represent = lambda value, row: value.strftime(T("%Y-%m-%d", lazy=False))

db.define_table('contacts', 
    Field('lastname', label=u'Επώνυμο', requires=IS_UPPER()),
    Field('firstname', label=u'Όνομα', requires=IS_UPPER()),
    Field('address', label=u'Διεύθυνση', requires=IS_UPPER()),
    Field('city', label=u'Πόλη', requires=IS_UPPER()),
    Field('zipcode', label=u'Ταχ. Κώδικας'),
    Field('telhome', label=u'Τηλέφωνο 1'),
    Field('telwork', label=u'Τηλέφωνο 2'),
    Field('telmobile', label=u'Κινητό'),
    Field('email', label=u'E-mail'),
    Field('property', label=u'Ιδιότητα', requires=IS_UPPER()),
    Field('notes', 'text', label=u'Σημειώσεις', requires=IS_UPPER()),
    singular=T('Contact'), plural=T('Contacts'),
    format='%(lastname)s %(firstname)s'
)

db.define_table('images', 
    Field('date', 'date', label=T('DATE'), default=datetime.date.today()),
    Field('patient', db.patients, writable=False, ondelete='NO ACTION'),
    Field('notes', 'text', label=T('Notes'), requires=IS_UPPER()),
    Field('img_file', 'upload', autodelete=True, required=True, label=T('File') ),
    singular=T('Image/Xray'), plural=T('Images/Xrays'),
    format='%(name)s'
)
 
db.images.date.requires = IS_DATE(format=T('%Y-%m-%d'))
db.images.date.represent = lambda value, row: value.strftime(T("%Y-%m-%d", lazy=False))
    
db.define_table('appointments', 
    Field('ap_start', 'datetime', label=T('START')),
    Field('ap_end', 'datetime', label=T('END')),
    Field('title', label=T('TITLE'), requires=IS_UPPER()),
    Field('patient', db.patients, ondelete='NO ACTION'),
    Field('notes', 'text', label=T('NOTES'), requires=IS_UPPER()),
    singular=T('Appointment'), plural=T('Appointments'),
    format='%(name)s'
)

db.appointments.patient.requires = IS_EMPTY_OR(IS_IN_DB(db,'patients.id','%(lastname)s %(firstname)s')) 
db.appointments.ap_start.requires = IS_DATETIME(format=T('%Y-%m-%d %H:%M:%S'))
db.appointments.ap_start.represent = lambda value, row: value.strftime(T("%Y-%m-%d %H:%M:%S", lazy=False))
db.appointments.ap_end.requires = IS_DATETIME(format=T('%Y-%m-%d %H:%M:%S'))
db.appointments.ap_end.represent = lambda value, row: value.strftime(T("%Y-%m-%d %H:%M:%S", lazy=False))

#from gluon.contrib.populate import populate
#if db(db.patients).count()<100:
#    populate(db.patients,10)

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

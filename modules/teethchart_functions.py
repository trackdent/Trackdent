from gluon import *

#{tooth:(x1,y1,x2,y2)} 
 
#teethrect = {
#              11:(269,0,313,148),
#              12:(237,0,268,148),
#              13:(200,0,236,148),
#              14:(166,0,199,148),
#              15:(129,0,165,148),
#              16:(87,0,128,148),
#              17:(44,0,86,148),
#              18:(9,0,43,148),
#              21:(314,0,358,148),
#              22:(314,0,358,148),
#              23:(390,0,427,148),
#              24:(428,0,462,148),
#              25:(463,0,497,148),
#              26:(498,0,539,148),
#              27:(540,0,582,148),
#              28:(583,0,619,148),
#              31:(314,149,341,296),
#              32:(342,149,372,296),
#              33:(373,149,406,296),
#              34:(406,149,437,296),
#              35:(438,149,470,296),
#              36:(471,149,514,296),
#              37:(515,149,557,296),
#              38:(558,149,604,296),
#              41:(285,149,313,296),
#              42:(256,149,284,296),          
#              43:(221,149,255,296),
#              44:(190,149,221,296),             
#              45:(156,149,189,296),
#              46:(112,149,155,296),
#              47:(69,149,111,296),
#              48:(25,149,68,296),
#              51:(269,0,313,148),
#              52:(237,0,268,148),
#              53:(200,0,236,148),
#              54:(157,0,199,148),
#              55:(113,0,156,148),
#              61:(314,0,358,148),
#              62:(359,0,389,148),
#              63:(390,0,427,148),
#              64:(424,0,466,148),
#              65:(466,0,509,148),
#              71:(314,149,341,296),
#              72:(342,149,371,296),
#              73:(372,149,406,296),
#              74:(407,149,448,296),
#              75:(449,149,493,296),
#              81:(285,149,313,296),
#              82:(256,149,284,296),
#              83:(221,149,255,296),
#              84:(175,149,220,296),
#              85:(132,149,174,296),
#              1020:(0,0,622,148),
#              4030:(0,149,622,296),
#              1234:(0,0,622,296)
#              }
        
def get_dental_works(db, patient_id, dw_type, permanent):
    dental_works = ()
    upper_denture_flag = False
    lower_denture_flag = False
    extracted_teeth = []
    if dw_type == 1:
        query = (db.dental_record.patient == patient_id) & (db.dental_record.done == True) & (db.teeth.id == db.dental_record.tooth) & (db.teeth.permanent == permanent)
        rows = db(query).select(db.dental_record.ALL)
    elif dw_type == 2:
        query = (db.dental_record.patient == patient_id) & (db.dental_record.done == False) & (db.teeth.id == db.dental_record.tooth) & (db.teeth.permanent == permanent)
        rows = db(query).select(db.dental_record.ALL)
        #id1 = db(db.therapy_plan.patient==patient_id).select().first().id
        #rows = db(db.therapy_plan_works.therapy_plan == id1).select()
    elif dw_type == 3:
        query = (db.pre_existing_dental_works.patient == patient_id) & (db.teeth.id == db.pre_existing_dental_works.tooth) & (db.teeth.permanent == permanent)
        rows = db(query).select(db.pre_existing_dental_works.ALL)
    rows_by_category = sorted(rows, key=lambda x: x.dental_work.graphic_category, reverse=False)
    for row in rows_by_category:
        if row.dental_work.graphic_category==1:
            if row.tooth.upper:
                upper_denture_flag = True
            else:
                lower_denture_flag = True
            dental_works = add_dental_work_to_drawable(row, dental_works)
        if row.dental_work.graphic_category==2:
            if (row.tooth.upper and not upper_denture_flag) or (not row.tooth.upper and not lower_denture_flag):
                extracted_teeth.append(row.tooth)
                dental_works = add_dental_work_to_drawable(row, dental_works)
        if row.dental_work.graphic_category==3:
            if (row.tooth.upper and not upper_denture_flag) or (not row.tooth.upper and not lower_denture_flag):
                dental_works = add_dental_work_to_drawable(row, dental_works)
        if row.dental_work.graphic_category==4:
            if (row.tooth.upper and not upper_denture_flag) or (not row.tooth.upper and not lower_denture_flag):
                #if row.tooth.upper<>upper_denture_flag or row.tooth.upper==lower_denture_flag:
                if row.tooth not in extracted_teeth:
                    dental_works = add_dental_work_to_drawable(row, dental_works)
        if row.dental_work.graphic_category==5:
            if not (upper_denture_flag and lower_denture_flag):
                dental_works = add_dental_work_to_drawable(row, dental_works)             
    return dental_works       
                        
def add_dental_work_to_drawable(row, dental_works):
    x_from = row.tooth.x1 + row.tooth.horizontal_offset_for_source
    x_to = row.tooth.x1 
    y = row.tooth.y1
    w = row.tooth.x2 - row.tooth.x1
    h = row.tooth.y2 - row.tooth.y1
    dental_works = dental_works + ({"img_src":URL("static","images/dentworks/" + row.dental_work.graphic.file), "s_x":x_from, "s_y":y, "s_w":w, "s_h":h, "d_x":x_to, "d_y":y, "d_w":w, "d_h":h},)
    return dental_works
        
def get_tooth_from_coordinates( db, x, y, separation, perm ): 
    query = (db.teeth.x1 < x) & (db.teeth.x2 > x) & (db.teeth.y1 < y) & (db.teeth.y2 > y) & (db.teeth.separation == separation) & (db.teeth.permanent == perm)    
    tooth = db(query).select().first().id
    return tooth

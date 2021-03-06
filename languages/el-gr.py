# coding: utf8
{
'  Cancel': 'Άκυρο',
'  CANCEL': '  ΑΚΥΡΟ',
'  New': '  Νέος',
'  NEW': '  ΝΕΟΣ',
'  New Patient': ' Νέος Ασθενής',
'  SAVE': 'ΚΑΤΑΧΩΡΗΣΗ',
'  Save': 'Καταχώρηση',
' **Category:** \n ------- \n Select in which button in dental diagram this Dental Work will appear for selection e.g. Diagnosis, Dentures etc. \n -------- \n **Graphic:** \n -------- \n Select how the dental work will appear in dental diagram. You must select one of the available graphics in the database in table dental_work_graphic. Of course you can add your own graphics in the database, they must be of certain specifications though. A Dental Work may have no graphic. \n -------- \n **Graphic Category:** \n ------- \n For full dentures, this should be 1. \n ------- \n ------- \n For extractions, this should be 2. \n ------- \n ------- \n For Dental Works that should appear on any tooth in diagram, even it is not present any more (e.g. a pontic of a bridge), this should be 3. \n ------- \n ------- \n For Dental Works that should appear only on present teeth, this should be 4. \n ------- \n ------- \n For Dental Works that should appear full mouth, this should be 5. \n ------- \n ------- \n This field has to do only about how the graphics appear and nothing more. If it is set wrong, the only bad thing that can happen is an abnormal dental diagram (e.g. teeth missing from a full denture when they shouldnt). It can be left empty. \n -------- \n **Separation:** \n ------- \n Area of the mouth this Dental Work is about. Tooth, jaw, half jaw, full mouth etc. \n ------- \n ------- \n Seperations are ways to divide a mouth. These ways are set in the database in table separations. You can add your own in table separations before you can use them in dental works. Separation affects the way graphics are rendered on the diagram . ': '  **Category:** \r\n             ------- \r\n            Καθορίζει σε ποιά κατηγορία θα εμφανιστεί η εργασία στα μενού αριστερά από  το διάγραμμα, π.χ. ΟΔΟΝΤΟΣΤΟΙΧΙΕΣ κλπ.\r\n             -------- \r\n             **Graphic:** \r\n             -------- \r\n             Επιλογή γραφικού για την εργασία από τα διαθέσιμα στην βάση δεδομένων. Βρίσκονται στον πίνακα dental_work_graphic. Μπορείτε να προσθέσετε τα δικά σας, αρκεί να είναι σύμφωνα με κάποιες προδιαγραφές. Μία εργασία μπορεί να μην έχει γραφικό.\r\n             -------- \r\n             **Graphic Category:** \r\n             ------- \r\n             Για οδοντοστοιχίες, βάλτε 1. \r\n             ------- \r\n             ------- \r\n             Για εξαγωγές, βάλτε 2. \r\n             ------- \r\n             ------- \r\n             Για εργασίες που πρέπει να εμφανίζονται ασχέτως αν υπάρχει ή όχι το δόντι στον φραγμό (π.χ. ενδιάμεσα γεφυρών), βάλτε 3. \r\n             ------- \r\n             ------- \r\n             Για εργασίες που πρέπει να εμφανίζονται μόνο σε υπάρχοντα δόντια, βάλτε 4. \r\n             ------- \r\n             ------- \r\n             Για εργασίες που πρέπει να εμφανίζονται σε όλον τον φραγμό, βάλτε 5.. \r\n             ------- \r\n             ------- \r\n            Το πεδίο αυτό έχει σχέση μόνο με το πώς εμφανίζονται τα γραφικά στο διάγραμμα. Εάν μπει λάθος τιμή, το μόνο λάθος που μπορεί να γίνει είναι να φαίνεται κάποιο λάθος στο διάγραμμα (π.χ. να λείπουν δόντια από μια οδοντοστοιχία). Μπορεί να είναι κενό.         \r\n     -------- \r\n     \r\n             **Separation:** \r\n             ------- \r\n            Περιοχή του στόματος στην οποία αναφέρεται η εργασία (δόντι, γνάθος, μισή γνάθος κλπ.).\r\n             ------- \r\n             ------- \r\n             Το πεδίο αυτό είναι ο τρόπος με τον οποίο χωρίζουμε το στόμα σε περιοχές.  Μπορείτε να προσθέσετε την δική σας διαμερισματοποίηση πριν την χρησιμοποιήσετε για τις εργασίες σας. Το πεδίο αυτό επηρεάζει το πως θα απεικονίζονται τα γραφικά των εργασιών πάνω στο διάγραμμα.           ',
' ------- \n Here you can add your own graphics for  use in your dental works. \n------- \n ------- \n Dimensions should be WIDTH 623 pixels  X HEIGHT 297 pixels \n ------- \n ------- \n Recommended type of image file is PNG. \n ------- \n ------- \n You can look for images DONTIA.png and NEOGILA.png and use them as a guide for teeth positions, for designing your own graphics. \n The former is for permanent and the latter for deciduous teeth. \n You can find them in the folder static/images/dentworks/. ': ' ----------\r\n             Προσθέστε τα δικά σας γραφικά για να τα χρησιμοποιείτε στις εργασίες σας.\r\n            ------- \r\n             ------- \r\n            Οι διαστάσεις πρέπει να είναι ΠΛΑΤΟΣ 623 pixel  X ΥΨΟΣ 297 pixel\r\n             ------- \r\n             ------- \r\n             Συνιστώμενο είδος αρχείου εικόνας  PNG. \r\n             ------- \r\n             ------- \r\n          Βρείτε τις εικόνες DONTIA.png  και NEOGILA.png και χρησιμοποιείστε τις σαν οδηγό για τις ακριβείς θέσεις των δοντιών, εάν σχεδιάσετε τα δικά σας γραφικά. Το πρώτο είναι για τα μόνιμα δόντια και το δεύτερο για τα νεογιλά. Θα τα βρείτε στον κατάλογο  static/images/dentworks/.    ',
' New': 'Νέος',
' New Endo': 'Νέα Ενδοδοντική Θεραπεία',
'!=': '!=',
'!langcode!': 'el-gr',
'!langname!': 'el-gr',
'"update" is an optional expression like "field1=\'newvalue\'". You cannot update or delete the results of a JOIN': '"update" is an optional expression like "field1=\'newvalue\'". You cannot update or delete the results of a JOIN',
'%(nrows)s records found': '%(nrows)s εγγραφές',
'%s %%{row} deleted': '%s %%{row} διαγράφηκε',
'%s %%{row} updated': '%s %%{row} ενημερώθηκε',
'%s selected': '%s selected',
'%Y-%m-%d': '%d-%m-%Y',
'%Y-%M-%D': '%D-%M-%Y',
'%Y-%m-%d %H:%M:%S': '%d-%m-%Y %H:%M:%S',
'(filtered from _MAX_ total records)': '(επιλογή από _MAX_ total records)',
'<': '<',
'<=': '<=',
'=': '=',
'>': '>',
'>=': '>=',
'@markmin\x01Number of entries: **%s**': 'Αριθμός εγγραφών: **%s**',
'AARE YOU SUUURE?': 'Είστε σίγουρος;',
'About': 'Περί',
'ABOUT': 'ABOUT-gr',
'About ': 'Περί',
'About TrackDent': 'Περί TrackDent',
'Access Control': 'Έλεγχος Πρόσβασης',
'Add': 'Προσθήκη',
'Add a medical condition:': 'Προσθήκη κατάστασης ιατρικού ιστορικού:',
'Add a new condition': 'Προσθήκη κατάστασης',
'Add Images': 'Προσθήκη εικόνων',
'Add this Therapy Plan to Current': 'Προσθήκη Σχεδίου Θεραπείας στο Τρέχον...',
'Add to contacts': 'Προσθήκη στις επαφές',
'ADDRESS': 'ΔΙΕΥΘΥΝΣΗ',
'Address': 'Διεύθυνση',
'Adjust Sum': 'Προσαρμογή Συνολικού Ποσού',
'Adjusted Sum': 'Προσαρμοσμένο Σύνολο',
'Administration': 'Διαχείριση',
'Administrative Interface': 'Administrative Interface',
'Age': 'Ηλικία',
'AIDS': 'AIDS',
'Ajax Recipes': 'Ajax Recipes',
'All': 'Όλα',
'ALL CERAMIC CROWN': 'ΟΛΟΚΕΡΑΜΙΚΗ ΣΤΕΦΑΝΗ',
'Amount': 'Ποσό',
'AMOUNT': 'ΠΟΣΟ',
'And': 'And',
'Antimicrobial prophylaxis': 'Χημειοπροφύλαξη',
'appadmin is disabled because insecure channel': 'appadmin is disabled because insecure channel',
'Appointment': 'Ραντεβού',
'Appointments': 'Ραντεβού',
'Are you sure you want to delete this object?': 'Are you sure you want to delete this object?',
'Are You Sure?': 'Είστε σίγουρος;',
'Are you sure?': 'Είστε σίγουρος;',
'AREA': 'ΠΕΡΙΟΧΗ',
'Area': 'Περιοχή',
'Associate': 'Συνεργάτης',
'Author: Dimitris Trifonopoulos': 'Author: Dimitris Trifonopoulos',
'Available Databases and Tables': 'Διαθέσιμες βάσεις δεδομένων και πίνακες',
'Back': 'Back',
'Back up': 'Back up',
'Balance': 'Υπόλοιπο',
'BIG DISTAL BLUE 1': 'ΑΝΑΣΥΣΤ ΑΠΩ ΜΑΣ ΜΠΛΕ 1',
'BIG DISTAL BLUE 2': 'ΑΝΑΣΥΣΤ ΑΠΩ ΜΑΣ ΜΠΛΕ 2',
'BIG DISTAL YELLOW': 'ΑΝΑΣΥΣΤ ΑΠΩ ΜΑΣ ΚΙΤΡΙΝΟ',
'BIG MESIAL BLUE': 'ΑΝΑΣΥΣΤ ΕΓΓΥΣ ΜΠΛΕ',
'BIG MESIAL RED': 'ΑΝΑΣΥΣΤ ΕΓΓΥΣ ΚΟΚΚΙΝΟ',
'BIG MESIAL YELLOW': 'ΑΝΑΣΥΣΤ ΕΓΓΥΣ ΚΙΤΡΙΝΟ',
'Buy this book': 'Buy this book',
'Cache': 'Cache',
'cache': 'cache',
'Cache Keys': 'Cache Keys',
'Calendar': 'Ημερολόγιο',
'CANAL': 'ΡΙΖ. ΣΩΛΗΝΑΣ',
'Canal': 'Ριζ. Σωλήνας',
'CANCEL': 'ΑΚΥΡΟ',
'Cancel': 'Άκυρο',
'Candidate Dental Work': 'Υποψήφια Οδοντιατρική Εργασία',
'Candidate Dental Works': 'Υποψήφιες Οδοντιατρικές Εργασίες',
'Cannot be empty': 'Δεν μπορεί να είναι άδειο',
'Cant load server data yet': 'Cant load server data yet',
'Cant serialize lists and dicts yet': 'Cant serialize lists and dicts yet',
'CAST POST': 'ΧΥΤΟΣ ΑΞΟΝΑΣ',
'Category': 'Category',
'Caution!': 'Προσοχή!',
'CERVICAL BLUE 1': 'ΑΥΧΕΝΙΚΟ ΜΠΛΕ 1',
'CERVICAL BLUE 2': 'ΑΥΧΕΝΙΚΟ ΜΠΛΕ 2',
'CERVICAL FILLING': 'ΑΥΧΕΝΙΚΗ ΕΜΦΡΑΞΗ',
'CERVICAL GREEN': 'ΑΥΧΕΝΙΚΟ ΠΡΑΣΙΝΟ',
'CERVICAL PINK': 'ΑΥΧΕΝΙΚΟ ΡΟΖ',
'CERVICAL RED 1': 'ΑΥΧΕΝΙΚΟ ΚΟΚΚΙΝΟ 1',
'CERVICAL RED 2': 'ΑΥΧΕΝΙΚΟ ΚΟΚΚΙΝΟ 2',
'CERVICAL YELLOW': 'ΑΥΧΕΝΙΚΟ ΚΙΤΡΙΝΟ',
'CHARGE': 'ΧΡΕΩΣΗ',
'Charge': 'Χρέωση',
'Check to delete': 'Check to delete',
'CITY': 'ΠΟΛΗ',
'City': 'Πόλη',
'CLEANING': 'ΚΑΘΑΡΙΣΜΟΣ',
'Clear': 'Clear',
'Clear CACHE?': 'Clear CACHE?',
'Clear DISK': 'Clear DISK',
'Clear RAM': 'Clear RAM',
'Client IP': 'Client IP',
'Close': 'Άκυρο',
'COLOR': 'ΧΡΩΜΑ',
'Color': 'Χρώμα',
'Colors': 'Χρώματα',
'Community': 'Community',
'Components and Plugins': 'Components and Plugins',
'Condition': 'Κατάσταση',
'Contact': 'Επικοινωνία',
'Contacts': 'Επαφές',
'Contacts List': 'Λίστα Επαφών',
'contains': 'contains',
'Controller': 'Controller',
'Copy': 'Αντιγραφή',
'Copy Dental Work to...': 'Αντιγραφή Εργασίας προς...',
'Copy to Therapy Plan': 'Αντιγραφή σε Σχέδιο Θεραπείας',
'Created By': 'Created By',
'Created On': 'Created On',
'CROWN': 'ΣΤΕΦΑΝΗ',
'CSV': 'CSV',
'CSV (hidden cols)': 'CSV (hidden cols)',
'Current request': 'Current request',
'Current response': 'Current response',
'Current session': 'Current session',
'Current Therapy Plan': 'Τρέχον Σχέδιο Θεραπείας ',
'Cut': 'Αποκοπή',
'DANGER ZONE!': 'ΕΠΙΚΙΝΔΥΝΗ ΖΩΝΗ!',
'Danger Zone!!!': 'Επικίνδυνη Ζώνη!!!',
'data uploaded': 'data uploaded',
'Database': 'Βάση Δεδομένων',
'Database %s select': 'Database %s select',
'DATE': 'ΗΜ/ΝΙΑ',
'Date': 'Ημ/νία',
'DATE OF BIRTH': 'ΗΜ/ΝΙΑ ΓΕΝΝΗΣΗΣ',
'Date of Birth': 'Ημ/νία Γέννησης',
'Date:': 'Ημ/νία:',
'db': 'db',
'DB Model': 'DB Model',
'Deciduous': 'Νεογιλά',
'Default': '1',
'Default patient': 'ΑΣΘΕΝΗΣ',
'Delete': 'Διαγραφή',
'DELETE': 'ΔΙΑΓΡΑΦΗ',
'delete': 'διαγραφή',
'Delete  Patient': 'Διαγραφή Ασθενούς',
'DELETE ALL PATIENT DATA, LABS, CONTACTS, APPOINTMENTS!!!': 'ΔΙΑΓΡΑΦΗ ΟΛΩΝ ΤΩΝ ΑΣΘΕΝΩΝ, ΕΡΓΑΣΤΗΡΙΩΝ, ΕΠΑΦΩΝ, ΡΑΝΤΕΒΟΥ!!!',
'DELETE ALL PATIENTS, THEIR DATA AND ALL APPOINTMENTS!!!': 'ΔΙΑΓΡΑΦΗ ΟΛΩΝ ΤΩΝ ΑΣΘΕΝΩΝ, ΤΩΝ ΔΕΔΟΜΕΝΩΝ ΤΟΥΣ ΚΑΙ ΤΩΝ ΡΑΝΤΕΒΟΥ!!!',
'DELETE ALL PATIENTS, THEIR DATA, LABS, CONTACTS AND ALL APPOINTMENTS!!!': 'ΔΙΑΓΡΑΦΗ ΟΛΩΝ ΤΩΝ ΑΣΘΕΝΩΝ, ΤΩΝ ΔΕΔΟΜΕΝΩΝ ΤΟΥΣ, ΤΩΝ ΕΡΓΑΣΤΗΡΙΩΝ, ΕΠΑΦΩΝ  ΚΑΙ ΟΛΩΝ ΤΩΝ ΡΑΝΤΕΒΟΥ!!!',
'Delete Patient': 'Διαγραφή Ασθενή',
'Delete:': 'Διαγραφή:',
'Demo': 'Demo',
'Dental History/Plan': 'Οδοντιατρικό Ιστορικό/Σχέδιο Θεραπείας',
'Dental Lab': 'Οδοντοτεχν. Εργαστήριο',
'DENTAL LAB': 'ΟΔΟΝΤΟΤΕΧΝ. ΕΡΓΑΣΤΗΡΙΟ',
'DENTAL LABS': 'ΟΔΟΝΤΟΤΕΧΝ. ΕΡΓΑΣΤΗΡΙΑ',
'Dental Labs': 'ΟΔΟΝΤΟΤΕΧΝΙΚΑ ΕΡΓΑΣΤΗΡΙΑ',
'Dental Office Management Application': 'Εφαρμογή Διαχείρισης Οδοντιατρείου',
'Dental Record': 'Οδοντιατρικό Ιστορικό',
'Dental Records': 'Οδοντιατρικό Ιστορικό',
'DENTAL WORK': 'ΟΔΟΝΤΙΑΤΡΙΚΗ ΕΡΓΑΣΙΑ',
'Dental Work': 'Οδοντιατρική Εργασία',
'Dental Work Categories': 'Κατηγορίες Οδοντιατρικών Εργασιών',
'Dental Work Category': 'Κατηγορία Οδοντιατρικών Εργασιών',
'Dental Work Selection': 'Επιλογή Οδοντιατρικής Εργασίας',
'Dental Works': 'Οδοντιατρικές Εργασίες',
'Dental Works List': 'Dental Works List',
'DENTURE': 'ΟΔΟΝΤΟΣΤΟΙΧΙΑ',
'DENTURE TEETH': 'ΔΟΝΤΙΑ ΟΔΟΝΤΟΣΤΟΙΧΙΑΣ',
'DENTURES': 'ΟΔΟΝΤΟΣΤΟΙΧΙΕΣ',
'Deployment Recipes': 'Deployment Recipes',
'Description': 'Description',
'design': 'design',
'Details': 'Λεπτομέρειες',
'Diabetes': 'ΔΙΑΒΗΤΗΣ',
'DIAGNOSTICS': 'ΔΙΑΓΝΩΣΗ',
'Diagram': 'Διάγραμμα',
'dimtrif@gmail.com': 'dimtrif@gmail.com',
'DIRECT RESTOR.': 'ΑΜΕΣΕΣ ΑΠΟΚΑΤΑΣΤΑΣΕΙΣ',
'DISK': 'DISK',
'Disk Cache Keys': 'Disk Cache Keys',
'Disk Cleared': 'Disk Cleared',
'Display _MENU_ entries': 'Display _MENU_ entries',
'Distal': 'Άπω',
'DISTAL': 'ΑΠΩ',
'DISTAL BLUE 1': 'ΑΠΩ ΜΠΛΕ 1',
'DISTAL BLUE 2': 'ΑΠΩ ΜΠΛΕ 2',
'DISTAL FILLING': 'ΕΜΦΡΑΞΗ ΑΠΩ',
'DISTAL OCCL. BLUE 1': 'ΑΠΩ ΜΑΣ ΜΠΛΕ 1',
'DISTAL OCCL. BLUE 2': 'ΑΠΩ ΜΑΣ ΜΠΛΕ 2',
'DISTAL OCCL. YELLOW': 'ΑΠΩ ΜΑΣ ΚΙΤΡΙΝΟ',
'DISTAL OCCL.FILLING': 'ΕΜΦΡΑΞΗ ΑΠΩ ΜΑΣΗΤΙΚΗ',
'DISTAL YELLOW': 'ΑΠΩ ΜΑΣΗΤ',
'Distobuccal': 'Άπω Παρειακός',
'Distolingual': 'Άπω Γλωσσικός',
'Documentation': 'Documentation',
"Don't know what to do?": "Don't know what to do?",
'done!': 'done!',
'Download': 'Download',
'Duration': 'Διάρκεια',
'Duration in minutes': 'Διάρκεια σε λεπτά',
'E-mail': 'E-mail',
'Economics': 'Οικονομικά',
'Edit': 'Επεξεργασία',
'Edit current record': 'Edit current record',
'Email and SMS': 'Email and SMS',
'End': 'Τέλος',
'END': 'ΤΕΛΟΣ',
'ENDO': 'ΕΝΔΟΔΟΝΤΙΑ',
'Endodontic Therapies': 'Ενδοδοντικές Θεραπείες',
'Endodontic Therapy': 'Ενδοδοντική Θεραπεία',
'Endodontics': 'Ενδοδοντία',
'enter a number between %(min)g and %(max)g': 'enter a number between %(min)g and %(max)g',
'enter an integer between %(min)g and %(max)g': 'enter an integer between %(min)g and %(max)g',
'enter date and time as %(format)s': 'enter date and time as %(format)s',
'enter date as %(format)s': '',
'Errors': 'Errors',
'Errors in form, please check it out.': 'Errors in form, please check it out.',
'EXAMINATION-DIAGNOSIS': 'ΕΞΕΤΑΣΗ-ΔΙΑΓΝΩΣΗ',
'export as csv file': 'Εξαγωγή σε αρχείο csv',
'Export:': 'Export:',
'EXTRACTION': 'ΕΞΑΓΩΓΗ',
'EXTRACTION SIMPLE': 'ΑΠΛΗ ΕΞΑΓΩΓΗ',
'EXTRACTION SURGICAL': 'ΧΕΙΡΟΥΡΓΙΚΗ ΕΞΑΓΩΓΗ',
'FAQ': 'FAQ',
"Father's Name": 'Όνομα Πατέρα',
'File': 'Αρχείο',
'FILE': 'ΑΡΧΕΙΟ',
'file': 'αρχείο',
'Find Patient...': 'Εύρεση ασθενή...',
'First': 'First',
'First name': 'Όνομα',
'First Visit': 'Πρώτη Επίσκεψη',
'FIRSTNAME': 'ΟΝΟΜΑ',
'Firstname': 'Όνομα',
'FIXED PROSTH.': 'ΑΚΙΝΗΤΗ ΠΡΟΣΘ.',
'For this, as well as any suggestion you may have, you can contact the author in this email address:': 'For this, as well as any suggestion you may have, you can contact the author in this email address:',
'Forms and Validators': 'Forms and Validators',
'Free Applications': 'Free Applications',
'FRONT-BACK LEFT-BACK RIGHT': 'ΠΡΟΣΘΙΑ-ΠΙΣΩ ΑΡΙΣΤ-ΠΙΣΩ ΔΕΞΙΑ',
'FULL MOUTH': 'ΟΛΟΣ Ο ΦΡΑΓΜΟΣ',
'General': 'Γενικά',
'GINGIVITIS THERAPY': 'ΘΕΡΑΠΕΙΑ ΟΥΛΙΤΙΔΑΣ',
'Graphic': 'Graphic',
'Graphic Category': 'Graphic Category',
'Graphics': 'Graphics',
'Graphics for Dental Works': 'Σχήματα για Οδοντιατρικές Εργασίες',
'Group ID': 'Group ID',
'Groups': 'Groups',
'Heart': 'ΚΑΡΔΙΑ',
'Help': 'Βοήθεια',
'Help for Dental Works Table': 'Βοήθεια για τις Οδοντιατρικές Εργασίες',
'Help for Graphics for Dental Works': 'Βοήθεια για τα Σχήματα Οδοντιατρικών Εργασιών',
'Hepatitis': 'ΗΠΑΤΙΤΙΔΑ',
'Home': 'Σπίτι',
'Home Phone': 'Τηλέφωνο Σπιτιού',
'HTML': 'HTML',
'Id': 'Id',
'Image': 'Εικόνα',
'Image/Xray': 'Εικόνα/Ακτινογραφία',
'Images': 'Εικόνες',
'Images/Xrays': 'Εικόνες/Ακτινογραφίες',
'import': 'import',
'Import/Export': 'Import/Export',
'in': 'in',
'Incisal': 'Κοπτικό',
'INCISAL': 'ΚΟΠΤΙΚΟ',
'Information:': 'Πληροφορίες:',
'Initial Condition': 'Αρχική Κατάσταση',
'Initial Sum': 'Αρχικό Σύνολο',
'Insurance': 'Ασφάλεια',
'Internal State': 'Internal State',
'Introduction': 'Introduction',
'Invalid datasource for DATATABLES plugin': 'Invalid datasource for DATATABLES plugin',
'Invalid email': 'Λάθος email',
'invalid email!': 'λάθος email!',
'Invalid Query': 'Invalid Query',
'invalid request': 'invalid request',
'Is Active': 'Is Active',
'JAW': 'ΓΝΑΘΟΣ',
'JSON': 'JSON',
'Key': 'Key',
'LAB': 'ΕΡΓΑΣΤΗΡΙΟ',
'Label 2': 'Label 2',
'Labs': 'Εργαστήρια',
'Labs List': 'Λίστα Εργαστηρίων',
'LARGE DISTAL FILLING': 'ΑΝΑΣΥΣΤΑΣΗ ΑΠΩ',
'LARGE MESIAL FILLING': 'ΑΝΑΣΥΣΤΑΣΗ ΕΓΓΥΣ',
'Last': 'Last',
'Last name': 'Επώνυμο',
'Last Visit': 'Τελευταία Επίσκεψη',
'LAST VISIT': 'ΤΕΛΕΥΤΑΙΑ ΕΠΙΣΚΕΨΗ',
'LASTNAME': 'ΕΠΩΝΥΜΟ',
'Lastname': 'Επώνυμο',
'Layout': 'Layout',
'Layout Plugins': 'Layout Plugins',
'Layouts': 'Layouts',
'Length': 'Μήκος',
'LENGTH': 'ΜΗΚΟΣ',
'Live Chat': 'Live Chat',
'Login': 'Login',
'Lost Password': 'Lost Password',
'Lost password?': 'Lost password?',
'LOWER JAW': 'ΚΑΤΩ ΓΝΑΘΟΣ',
'Manage Cache': 'Manage Cache',
'MATERIAL': 'ΥΛΙΚΟ',
'Material': 'Υλικό',
'MATERIALS': 'ΥΛΙΚΑ',
'Materials': 'Υλικά',
'Medical': 'Ιατρικά',
'Medical condition': 'Ιατρική Κατάσταση',
'Medical Condition': 'Ιατρική Κατάσταση',
'Medical Conditions': 'Ιατρικές Καταστάσεις ',
'Medical Record': 'Ιατρικό Ιστορικό',
'Medical Record details': 'Λεπτομέρειες Ιατρικού Ιστορικού',
'Menu Model': 'Menu Model',
'MES-DIST-OCCL BLUE 1': 'ΕΓΓΥΣ-ΑΠΩ-ΜΑΣ ΜΠΛΕ 1',
'MES-DIST-OCCL BLUE 2': 'ΕΓΓΥΣ-ΑΠΩ-ΜΑΣ ΜΠΛΕ 2',
'MES-DIST-OCCL YELLOW': 'ΕΓΓΥΣ-ΑΠΩ-ΜΑΣ ΚΙΤΡΙΝΟ',
'MES-OCCL-DIST FILLING': 'ΕΜΦΡΑΞΗ ΕΓΓΥΣ ΑΠΩ ΜΑΣΗΤ.',
'MESIAL': 'ΕΓΓΥΣ',
'Mesial': 'Εγγύς',
'MESIAL BLUE 1': 'ΕΓΓΥΣ ΜΠΛΕ 1',
'MESIAL BLUE 2': 'ΕΓΓΥΣ ΜΠΛΕ 2',
'MESIAL FILLING': 'ΕΜΦΡΑΞΗ ΕΓΓΥΣ',
'MESIAL OCCL. BLUE 1': 'ΕΓΓΥΣ ΜΑΣΗΤ. ΜΠΛΕ 1',
'MESIAL OCCL. BLUE 2': 'ΕΓΓΥΣ ΜΑΣΗΤ. ΜΠΛΕ 2',
'MESIAL OCCL. YELLOW': 'ΕΓΓΥΣ ΜΑΣΗΤ. ΚΙΤΡΙΝΟ',
'MESIAL OCCL.FILLING': 'ΕΜΦΡΑΞΗ ΕΓΓΥΣ ΜΑΣΗΤ.',
'MESIAL YELLOW ': 'ΕΓΓΥΣ ΚΙΤΡΙΝΟ',
'Mesiobuccal': 'Εγγύς Παρειακός',
'Mesiolingual': 'Εγγύς Γλωσσικός',
'Mobile': 'Κινητό',
'Modified By': 'Modified By',
'Modified On': 'Modified On',
'MOUTH QUARTER': 'ΤΕΤΑΡΤΗΜΟΡΙΑ',
'Move Dental Work to...': 'Μεταφορά Εργασίας προς...',
'Move to Therapy Plan': 'Μεταφορά σε Σχέδιο Θεραπείας',
'my comment': 'my comment',
'My Sites': 'My Sites',
'Name': 'Όνομα',
'Name:': 'Όνομα:',
'Neck': 'Αυχένας',
'NECK': 'ΑΥΧΕΝΑΣ',
'New': 'Νέο',
'NEW': 'ΝΕΟ',
'New Color': 'Νέα Χρωματοληψία',
'New Dental Work': 'New Dental Work',
'New Graphic for Dental Works': 'New Graphic for Dental Works',
'New Material': 'New Material',
'New Medical Condition': 'Νέα Κατάσταση Ιατρικού Ιστορικού',
'New Patient': 'Νέος Ασθενής',
'New Payment': 'Νέα Πληρωμή',
'New Record': 'New Record',
'new record inserted': 'new record inserted',
'New Therapy Plan': 'Νέο Σχέδιο Θεραπείας',
'Next': 'Next',
'next 100 rows': 'next 100 rows',
'No databases in this application': 'No databases in this application',
'No records found': 'No records found',
'None': 'None',
'not in': 'not in',
'Notes': 'Σημειώσεις',
'NOTES': 'ΣΗΜΕΙΩΣΕΙΣ',
'Nothing found - sorry': 'Nothing found - sorry',
'Object or table name': 'Object or table name',
'OCCL. BLUE 1': 'ΜΑΣΗΤ ΜΠΛΕ 1',
'OCCL. BLUE 2': 'ΜΑΣΗΤ ΜΠΛΕ 2',
'OCCL. YELLOW': 'ΜΑΣΗΤ ΚΙΤΡΙΝΟ',
'OCCLUSAL FILLING': 'ΕΜΦΡΑΞΗ ΜΑΣΗΤΙΚΑ',
'Office': 'Γραφείο',
'Office Phone': 'Τηλέφωνο Γραφείου',
'OK': 'OK',
'Online examples': 'Online examples',
'Or': 'Or',
'or import from csv file': 'or import from csv file',
'Origin': 'Origin',
'Other Contacts': 'Άλλες Επαφές',
'Other Plugins': 'Other Plugins',
'Other Recipes': 'Other Recipes',
'Overview': 'Overview',
'Palatal': 'Υπερώιος',
'PARTIAL DENTURE': 'ΜΕΡΙΚΗ ΟΔΟΝΤΟΣΤΟΙΧΙΑ',
'PARTIAL DENTURE TOOTH': 'ΔΟΝΤΙ ΜΕΡΙΚΗΣ ΟΔΟΝΤΟΣΤΟΙΧΙΑΣ',
'Password': 'Password',
'Paste': 'Επικόλληση',
'Patient': 'Ασθενής',
'Patient List': 'Λίστα Ασθενών',
'Patient Name': 'Όνομα Ασθενούς',
'Patient:': 'Ασθενής:',
'Patients': 'Ασθενείς',
'PATIENTS': 'ΑΣΘΕΝΕΙΣ',
'Patients List': 'Λίστα Ασθενών',
'Patients:': 'Ασθενείς:',
'Payment': 'Πληρωμη',
'Payments': 'Οικονομικά',
'People': 'People',
'PERIO': 'ΠΕΡΙΟ',
'PERIODONTITIS THERAPY': 'ΘΕΡΑΠΕΙΑ ΠΕΡΙΟΔΟΝΤΙΤΙΔΑΣ',
'PLAN': 'Σχέδιο Θεραπείας',
'Plan name': 'Όνομα Σχεδίου Θεραπείας',
'Plugins': 'Plugins',
'PORCELAIN-FUSED-TO-METAL CROWN': 'ΣΤΕΦΑΝΗ ΜΕΤΑΛΟΠΟΡΣΕΛΑΝΗ',
'Pre existing Dental Record': 'Pre existing Dental Record',
'Pre existing Dental Works': 'Pre existing Dental Works',
'PREFABRICATED POST': 'ΠΡΟΚΑΤΑΣΚΕΥΑΣΜΕΝΟΣ ΑΞΟΝΑΣ',
'Preface': 'Preface',
'Preview': 'Προεπισκόπηση',
'PREVIEW': 'ΠΡΟΕΠΙΣΚΟΠΗΣΗ',
'Previous': 'Previous',
'previous 100 rows': 'previous 100 rows',
'Price': 'Τιμή',
'PRICE': 'ΤΙΜΗ',
'Proceed with caution.': 'Προχωρείστε με προσοχή.',
'Processing...': 'Processing...',
'Profession': 'Επάγγελμα',
'Python': 'Python',
'Query Not Supported: %s': 'Query Not Supported: %s',
'Query:': 'Query:',
'Quick Examples': 'Quick Examples',
'RAM': 'RAM',
'RAM Cache Keys': 'RAM Cache Keys',
'Ram Cleared': 'Ram Cleared',
'Recall Date': 'Ημ/νία Επανεξέτασης',
'Receipt Amount': 'Ποσό Απόδειξης',
'RECEIPT AMOUNT': 'ΠΟΣΟ ΑΠΟΔ.',
'RECEIPT NO': 'ΑΡΙΘΜ. ΑΠΟΔΕΙΞΗΣ',
'Receipt No': 'Αριθμός Απόδειξης',
'Recipes': 'Recipes',
'Record': 'Record',
'Record %s': 'Record %s',
'record does not exist': 'record does not exist',
'Record ID': 'Record ID',
'Record id': 'Record id',
'Referred by': 'Παραπομπή από',
'Register': 'Register',
'Registration identifier': 'Registration identifier',
'Registration key': 'Registration key',
'Remember me (for 30 days)': 'Remember me (for 30 days)',
'Rename Medical Condition': 'Μετονομασία Ιατρικής Κατάστασης',
'Reset Password key': 'Reset Password key',
'Restore': 'Restore',
'RESTORE!!!': 'RESTORE!!!',
'Role': 'Role',
'ROOT CANAL ANTERIOR': 'ΕΝΔΟΔΟΝΤΙΚΗ ΘΕΡΑΠΕΙΑ ΠΡΟΣΘΙΟΥ',
'ROOT CANAL POSTERIOR': 'ΕΝΔΟΔΟΝΤΙΚΗ ΘΕΡΑΠΕΙΑ ΟΠΙΣΘΙΟΥ',
'Rows in Table': 'Rows in Table',
'Rows selected': 'Rows selected',
'SAVE': 'ΚΑΤΑΧΩΡΗΣΗ',
'Save': 'Καταχώρηση',
'Save changes': 'Καταχώρηση Μεταβολής',
'Search': 'Εύρεση',
'Search in %s': 'Search in %s',
'Search:': 'Εύρεση:',
'Select file for restore:': 'Select file for restore:',
'Select Patient': 'Επιλογή Ασθενή',
'Semantic': 'Semantic',
'Separation': 'Separation',
'Services': 'Services',
'Set this Therapy Plan as Current': 'Κάνε αυτό το Σχέδιο Θεραπείας Τρέχον...',
'Sex': 'Φύλο',
'Showing 0 to 0 of 0 records': 'Showing 0 to 0 of 0 records',
'Showing _START_ to _END_ of _TOTAL_ records': 'Showing _START_ to _END_ of _TOTAL_ records',
'Size': 'Μέγεθος',
'SIZE': 'ΜΕΓΕΘΟΣ',
'Size of cache:': 'Size of cache:',
'Start': 'Start',
'START': 'START',
'starts with': 'starts with',
'state': 'state',
'Statistics': 'Statistics',
'Stylesheet': 'Stylesheet',
'Submit': 'Καταχώρηση',
'submit': 'καταχώρηση',
'Success!': 'Success!',
'Sum': 'Σύνολο',
'Support': 'Support',
'SURGICAL': 'ΧΕΙΡΟΥΡΓΙΚΑ',
'Table': 'Table',
'TAPER': 'ΚΩΝΙΚΟΤΗΤΑ',
'Taper': 'Κωνικότητα',
'Teeth': 'Δόντια',
'Tel Home': 'Τηλ. Σπιτιού',
'Tel Mobile': 'Κινητό',
'Tel Work': 'Τηλ. Εργασίας',
'Telephone 1': 'Τηλέφωνο 1',
'Telephone 2': 'Τηλέφωνο 2',
'Telephone of referrer': 'Τηλέφωνο συστήσαντα',
'The "query" is a condition like "db.table1.field1==\'value\'". Something like "db.table1.field1==db.table2.field2" results in a SQL JOIN.': 'The "query" is a condition like "db.table1.field1==\'value\'". Something like "db.table1.field1==db.table2.field2" results in a SQL JOIN.',
'The author will be happy to hear this target has been accomplished, even partially.': 'The author will be happy to hear this target has been accomplished, even partially.',
'The Core': 'The Core',
'The Views': 'The Views',
'THERAPY PLAN': 'ΣΧΕΔΙΟ ΘΕΡΑΠΕΙΑΣ',
'Therapy Plan': 'Σχέδιο Θεραπείας',
'Therapy Plans': 'Σχέδια Θεραπείας',
'there are errors!': 'there are errors!',
'This App': 'This App',
'This email already has an account': 'This email already has an account',
'This Field was edited': 'This Field was edited',
'This is a virtual tooltip for record %s': 'This is a virtual tooltip for record %s',
'This option allows you to restore your data to a previous state from a file. WARNING!!! ALL YOUR CURRENT DATA WILL BE LOST!!!': 'This option allows you to restore your data to a previous state from a file. WARNING!!! ALL YOUR CURRENT DATA WILL BE LOST!!!',
'This option will delete all patient data and all appointments, resetting the database to its initial state. Possible dental works and graphics will stay as is.': 'This option will delete all patient data and all appointments, resetting the database to its initial state. Possible dental works and graphics will stay as is.',
'This option will delete all patient data, contacts and all appointments, resetting the database to its initial state. Possible dental works and graphics will stay as is.': 'This option will delete all patient data, contacts and all appointments, resetting the database to its initial state. Possible dental works and graphics will stay as is.',
'This option will delete all patient data, contacts, dental labs and all appointments. POSSIBLE DENTAL WORKS, DENTAL WORKS CATEGORIES AND MEDICAL CONDITIONS WILL STAY AS IS. One necessary sample patient will be inserted.': 'This option will delete all patient data, contacts, dental labs and all appointments. POSSIBLE DENTAL WORKS, DENTAL WORKS CATEGORIES AND MEDICAL CONDITIONS WILL STAY AS IS. One necessary sample patient will be inserted.',
'This option will delete all patient data, contacts, dental labs, all appointments, possible dental works, dental works categories and medical conditions. Some sample data will be inserted, resetting the database to its initial state.': 'This option will delete all patient data, contacts, dental labs, all appointments, possible dental works, dental works categories and medical conditions. Some sample data will be inserted, resetting the database to its initial state.',
'This page allows you to do dangerous actions for your data, such as resetting your database and loosing all your patients data for ever. Proceed with caution.': 'Εδώ μπορείτε να κάνετε επικίνδυνες ενέργειες για την ασφάλεια των δεδομένων σας, όπως να αδειάσετε όλη την βάση και να χάσετε όλα τα δεδομένα των ασθενών σας για πάντα. Προχωρείστε με προσοχή.',
'This page allows you to do dangerous actions, such as resetting your database and loosing all your patients data for ever.': 'Εδώ μπορείτε να κάνετε επικίνδυνες ενέργειες για την ασφάλεια των δεδομένων σας, όπως να αδειάσετε όλη την βάση και να χάσετε όλα τα δεδομένα των ασθενών σας για πάντα.',
'This page allows you to do dangerous actions, such as resetting your database and loosing all your patients data for ever. Proceed with caution.': 'Εδώ μπορείτε να κάνετε επικίνδυνες ενέργειες για την ασφάλεια των δεδομένων σας, όπως να αδειάσετε όλη την βάση και να χάσετε όλα τα δεδομένα των ασθενών σας για πάντα. Προχωρείστε με προσοχή.',
'This software is a volunteer effort hoping to help dentists to run their offices in a more organized way.': 'This software is a volunteer effort hoping to help dentists to run their offices in a more organized way.',
'This software is a volunteer effort hoping to help dentists to run their offices in a more organized way. The author will be happy to hear this target has been accomplished, even partially. For this, as well as any suggestion you may have, you can contact the author in this email address: dimtrif@gmail.com': 'This software is a volunteer effort hoping to help dentists to run their offices in a more organized way. The author will be happy to hear this target has been accomplished, even partially. For this, as well as any suggestion you may have, you can contact the author in this email address: dimtrif@gmail.com',
'Time in Cache (h:m:s)': 'Time in Cache (h:m:s)',
'Time:': 'Time:',
'Timestamp': 'Timestamp',
'Title': 'Title',
'TITLE': 'TITLE',
'Today': 'Today',
'TOOTH': 'ΔΟΝΤΙ',
'Tooth': 'Δόντι',
'TOOTH/AREA': 'ΔΟΝΤΙ/ΠΕΡΙΟΧΗ',
'Tooth:': 'Δόντι:',
'TOTALLY RESET DATABASE!!!': 'ΟΛΙΚΗ ΕΠΑΝΑΦΟΡΑ ΒΑΣΗΣ ΔΕΔΟΜΕΝΩΝ!!!',
'TrackDent Help': 'Βοήθεια TrackDent',
'Transfer': 'Μεταφορά',
'TSV (Excel compatible)': 'TSV (Excel compatible)',
'TSV (Excel compatible, hidden cols)': 'TSV (Excel compatible, hidden cols)',
'Twitter': 'Twitter',
'Type of Mouth Separation': 'Διαμερισματοποίηση Στοματικής Κοιλότητας',
'unable to parse csv file': 'unable to parse csv file',
'Unknown': 'Unknown',
'Update:': 'Update:',
'UPPER JAW': 'ΑΝΩ ΓΝΑΘΟΣ',
'Use (...)&(...) for AND, (...)|(...) for OR, and ~(...)  for NOT to build more complex queries.': 'Use (...)&(...) for AND, (...)|(...) for OR, and ~(...)  for NOT to build more complex queries.',
'User %(id)s Logged-in': 'User %(id)s Logged-in',
'User ID': 'User ID',
'value not in database': 'value not in database',
'Videos': 'Videos',
'View': 'Επισκόπηση',
'Welcome': 'Welcome',
'X-RAY': 'ΑΚΤΙΝΟΓΡΑΦΙΑ',
'XML': 'XML',
'yyyy-MM-dd HH:mm:ss': 'dd-MM-yyyy HH:mm:ss',
'yyyy/MM/dd': 'dd/MM/yyyy',
'Zip Code': 'Τ.Κ.',
'ΑΝΩ ΑΡΙΣΤΕΡΑ ΤΕΤΑΡΤΗΜΟΡΙΟ': 'ΑΝΩ ΑΡΙΣΤΕΡΑ ΤΕΤΑΡΤΗΜΟΡΙΟ',
'ΑΝΩ ΓΝΑΘΟΣ': 'ΑΝΩ ΓΝΑΘΟΣ',
'ΑΝΩ ΔΕΞΙΑ ΤΕΤΑΡΤΗΜΟΡΙΟ': 'ΑΝΩ ΔΕΞΙΑ ΤΕΤΑΡΤΗΜΟΡΙΟ',
'ΚΑΤΩ ΑΡΙΣΤΕΡΑ ΤΕΤΑΡΤΗΜΟΡΙΟ': 'ΚΑΤΩ ΑΡΙΣΤΕΡΑ ΤΕΤΑΡΤΗΜΟΡΙΟ',
'ΚΑΤΩ ΓΝΑΘΟΣ': 'ΚΑΤΩ ΓΝΑΘΟΣ',
'ΚΑΤΩ ΔΕΞΙΑ ΤΕΤΑΡΤΗΜΟΡΙΟ': 'ΚΑΤΩ ΔΕΞΙΑ ΤΕΤΑΡΤΗΜΟΡΙΟ',
'ΟΛΟΣ Ο ΦΡΑΓΜΟΣ': 'ΟΛΟΣ Ο ΦΡΑΓΜΟΣ',
'ΠΙΣΩ ΑΝΩ ΑΡΙΣΤΕΡΑ': 'ΠΙΣΩ ΑΝΩ ΑΡΙΣΤΕΡΑ',
'ΠΙΣΩ ΑΝΩ ΔΕΞΙΑ': 'ΠΙΣΩ ΑΝΩ ΔΕΞΙΑ',
'ΠΙΣΩ ΚΑΤΩ ΑΡΙΣΤΕΡΑ': 'ΠΙΣΩ ΚΑΤΩ ΑΡΙΣΤΕΡΑ',
'ΠΙΣΩ ΚΑΤΩ ΔΕΞΙΑ': 'ΠΙΣΩ ΚΑΤΩ ΔΕΞΙΑ',
'ΠΡΟΣΘΙΑ ΑΝΩ': 'ΠΡΟΣΘΙΑ ΑΝΩ',
'ΠΡΟΣΘΙΑ ΚΑΤΩ': 'ΠΡΟΣΘΙΑ ΚΑΤΩ',
}

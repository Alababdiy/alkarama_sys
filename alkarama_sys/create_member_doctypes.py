# Member Applicant Doctype definition
member_applicant = {
    "doctype": "DocType",
    "name": "Member Applicant",
    "fields": [
        {"fieldname": "family_members", "label": "أفراد الأسرة", "fieldtype": "Table", "options": "Family Member"},
        {"fieldname": "national_id_images", "label": "صور الأرقام الوطنية", "fieldtype": "Attach Image", "multiple": 1},
        {"fieldname": "member_images", "label": "صور أفراد الأسرة", "fieldtype": "Attach Image", "multiple": 1},
        {"fieldname": "whatsapp_number", "label": "رقم الواتساب", "fieldtype": "Data"},
        {"fieldname": "call_number", "label": "رقم المكالمات", "fieldtype": "Data"},
        {"fieldname": "current_residence", "label": "مكان الإقامة الحالي", "fieldtype": "Section Break"},
        {"fieldname": "state", "label": "الولاية", "fieldtype": "Data"},
        {"fieldname": "city", "label": "المدينة", "fieldtype": "Data"},
        {"fieldname": "locality", "label": "المحلية", "fieldtype": "Data"},
        {"fieldname": "gps_address", "label": "عنوان تفصيلي (GPS)", "fieldtype": "Data", "reqd": 0},
        {"fieldname": "income_source", "label": "مصدر الدخل الحالي", "fieldtype": "Data"},
        {"fieldname": "monthly_income", "label": "متوسط الدخل الشهري الحالي (بالجنيه)", "fieldtype": "Currency"},
        {"fieldname": "bank_account", "label": "رقم الحساب البنكي للأسرة", "fieldtype": "Data"},
        {"fieldname": "account_holder", "label": "اسم صاحب الحساب", "fieldtype": "Data"},
        {"fieldname": "bank_name", "label": "اسم البنك", "fieldtype": "Data"},
        {"fieldname": "martyr_section", "label": "بيانات الشهيد", "fieldtype": "Section Break"},
        {"fieldname": "martyr_name", "label": "اسم الشهيد (رباعي)", "fieldtype": "Data"},
        {"fieldname": "martyr_date", "label": "تاريخ الاستشهاد", "fieldtype": "Date"},
        {"fieldname": "martyr_place", "label": "مكان الاستشهاد", "fieldtype": "Data"},
        {"fieldname": "martyr_unit", "label": "الفرقة أو المتحرك", "fieldtype": "Data"},
        {"fieldname": "martyr_national_id_image", "label": "صورة الرقم الوطني", "fieldtype": "Attach Image"},
        {"fieldname": "martyr_personal_image", "label": "صورة شخصية", "fieldtype": "Attach Image"},
        {"fieldname": "martyr_military_card", "label": "صورة البطاقة العسكرية", "fieldtype": "Attach Image", "reqd": 0},
        {"fieldname": "martyr_death_certificate", "label": "صورة شهادة الوفاة / إفادة استشهاد", "fieldtype": "Attach Image"},
    ]
}

# Family Member Doctype definition
family_member = {
    "doctype": "DocType",
    "name": "Family Member",
    "fields": [
        {"fieldname": "member_name", "label": "اسم الفرد", "fieldtype": "Data"},
        {"fieldname": "gender", "label": "النوع", "fieldtype": "Select", "options": "ذكر\nأنثى"},
        {"fieldname": "relation_to_martyr", "label": "صلة القرابة بالشهيد", "fieldtype": "Data"},
        {"fieldname": "is_guardian", "label": "ولي أمر الأسرة", "fieldtype": "Check"},
        {"fieldname": "national_id_image", "label": "صورة الرقم الوطني", "fieldtype": "Attach Image"},
        {"fieldname": "member_image", "label": "صورة الفرد", "fieldtype": "Attach Image"},
    ]
}

# Methods to create doctypes in Frappe
import frappe

def create_family_member_doctype():
    doctype_name = "Family Member"
    try:
        doc = frappe.get_doc("DocType", doctype_name)
        existing_fields = {f.fieldname for f in doc.fields}
        new_fields = [f for f in family_member["fields"] if f["fieldname"] not in existing_fields]
        if new_fields:
            for field in new_fields:
                doc.append("fields", field)
            doc.save()
            frappe.db.commit()
        return doc
    except frappe.DoesNotExistError:
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": doctype_name,
            "module": "Alkarama Sys",
            "fields": family_member["fields"]
        })
        doc.insert(ignore_if_duplicate=True)
        frappe.db.commit()
        return doc

def create_member_applicant_doctype():
    doctype_name = "Member Applicant"
    try:
        doc = frappe.get_doc("DocType", doctype_name)
        existing_fields = {f.fieldname for f in doc.fields}
        new_fields = [f for f in member_applicant["fields"] if f["fieldname"] not in existing_fields]
        if new_fields:
            for field in new_fields:
                doc.append("fields", field)
            doc.save()
            frappe.db.commit()
        return doc
    except frappe.DoesNotExistError:
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": doctype_name,
            "module": "Alkarama Sys",
            "fields": member_applicant["fields"]
        })
        doc.insert(ignore_if_duplicate=True)
        frappe.db.commit()
        return doc

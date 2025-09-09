# Copyright (c) 2025, team@ratina.co and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MemberApplicant(Document):
	def autoname(self):
		if hasattr(self, 'martyr_name') and self.martyr_name:
			self.name = f"اسرة الشهيد {self.martyr_name}"
		else:
			self.name = "اسرة الشهيد"
